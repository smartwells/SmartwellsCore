#import serial
import time
#import subprocess
import json

# функция опроса первых 8ми каналов
def query_ch(COM_Port, cmd, t):								# порт, команда, таймаут перепд ответом
	#t = 0.6									# время ожидания ответа, с
	answer_json = {}                        					# словарь для ответа
	ch = 1										# номер канала
	val = ""                							# строка для формирования значений сигнала
	'''
	COM_Port = serial.Serial(COM_PortName) 				# открытие порта
	#print('\n')
	#print(COM_PortName,'Opened')
	#print('Connected:', COM_Port.isOpen())
	if !COM_Port.isOpen():						# проверка открытия порта
		return 'Не удается открыть порт {}'.format(COM_PortName)

	subprocess.call("./config_rs485.sh")				# конфигурация порта на уровне ОС
	'''
	cmdascii = cmd.encode('ascii')							# кодирование команды из ASCII в байткод
	COM_Port.write(cmdascii)							# отправка команды на устройство

	time.sleep(t)									# ожидание перед запросом ответа

	answer = COM_Port.readline()							# чтение ответа
	answer = answer.decode('ascii')							# декодирование ответа из байткода в ASCII

	# разбор ответа в словарь
	answer = answer[1:]								# срез первого символа в ответе
	if (answer[0] != '+' and answer[0] != '-'):					# если ответ с мусором либо отстутсвует
		#return answer[0] != '+'
		return 'Ответ не корректный, либо не содержит показаний каналов: {}'.format(answer)

	answer_json['_id'] = int(time.strftime('%Y%m%d%H%M%S', time.localtime()))	# запись времени регистрации данных

	for s in answer:								# итерация по строке ответа
		if (s == '+' or s == '-'):						# если попадаются + или -
			if (ch > 1):							# заполнение словаря после прохода первого блока значений
				answer_json[ch_name] = float(val)			# заполнение словаря наименованием канала и его значением
			ch_name = 'ch' + str(ch)					# формирование имени канала ch + номер канала
			ch += 1								# увеличение номера канала
			val = s								# запись знака значения
		else:
			val += s							# запись цифр значений
	answer_json[ch_name] = float(val)						# добавление последней пары значений в словарь

	#COM_Port.close()								# закрытие порта

	return json.dumps(answer_json)							# возврат словаря в JSON

