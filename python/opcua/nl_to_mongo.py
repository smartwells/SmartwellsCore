#!/usr/bin python3

import NL
import serial
import sched, time
import subprocess
import json
from pymongo import MongoClient
import urllib.parse

def get_database(dbname):						# функция связи с БД
	username = urllib.parse.quote_plus('admin')
	password = urllib.parse.quote_plus('16551655')
	CONNECTION_STRING = 'mongodb://%s:%s@127.0.0.1:27017'%(username, password) # строка подключения
	client = MongoClient(CONNECTION_STRING)				# создание подключения
	db = client[dbname]                             		# подключение к БД
	return db


def query(COM_Port, cmd, t, postsdb):					# функция запроса
        answer = NL.query_ch(COM_Port, cmd, t)	                	# вызов функции запроса
        try:
                answer = json.loads(answer)                     	# попытка конвертации JSON
        except ValueError as e:
                print(answer)                                   	# в случае неудачи вывод ответа от устройства
                COM_Port.close()                                	# закрытие порта
        else:
                #print('\n')
                #print('\nВремя: {}\nДавление: {} В\nТемпература: {} В'.format(answer["time"], answer["ch2"], answer["ch3"]))
                #print('\n')
                #print(NL.query_ch(COM_Port, cmd, t))           	# вызов функции запроса
		#post_data['_id'] = answer['time']			# запись даты в id сообщения БД
                postsdb.insert_one(answer)				# запись данных в БД
                #print(answer['_id'])

def main():

	COM_PortName = '/dev/ttyS0'                             	# наименование порта
	t = 0.5                                                 	# таймаут ожидания ответа
	cmd = '#01\n'                                           	# команда, отправляемая на устройство
	s = sched.scheduler(time.time, time.sleep)              	# планировщик
	dbname = 'nl'							# наименование БД

	COM_Port = serial.Serial(COM_PortName)                  	# открытие порта
	#print(COM_Port)
	#print(COM_PortName,'Opened')
	#print('Connected:', COM_Port.isOpen())
	if COM_Port.isOpen():                                   	# проверка открытия порта
		print('\nПорт {} открыт'.format(COM_PortName))
		subprocess.call("./config_rs485.sh")            	# конфигурация порта на уровне ОС

		db = get_database(dbname)                               # подключение БД
		postsdb = db[dbname]                                    # связка с данными в БД

		#i = 0
		starttime=time.time()
		while True:
			query(COM_Port, cmd, t, postsdb)
			time.sleep(1.0 - ((time.time() - starttime) % 1.0))
		'''
		for i in range(90):					# итерация посекундно, вызов функции query с аргументами
			s.enter(i,
				1,
				query,
				(COM_Port, cmd, t, postsdb))		# вызов запроса
			#i += 1
			#s.run()
		s.run()							# запуск залпанированных событий
		'''
		COM_Port.close()                                	# закрытие порта
	else:
		print('\nНе удается открыть порт {}'.format(COM_PortName))

if __name__ == "__main__":
	main()

