import NL
import serial
import sched, time
import subprocess
import json

'''
COM_PortName = '/dev/ttyS0'					# наименование порта
t = 0.5								# таймаут ожидания ответа
cmd = '#01\n'							# команда, отправляемая на устройство
s = sched.scheduler(time.time, time.sleep)			# планировщик
'''

def query(COM_Port, cmd, t):					# функция запроса
        answer = NL.query_ch(COM_Port, cmd, t)                  # вызов функции запроса
        try:
                answer = json.loads(answer)                     # попытка конвертации JSON
        except ValueError as e:
                print(answer)                                   # в случае неудачи вывод ответа от устройства
                COM_Port.close()                                # закрытие порта
        else:
                #print('\n')
                print('\nВремя: {}\nДавление: {} В\nТемпература: {} В'.format(answer["time"], answer["ch2"], answer["ch3"]))
                #print('\n')
                #print(NL.query_ch(COM_Port, cmd, t))           # вызов функции запроса

def main():

	COM_PortName = '/dev/ttyS0'                             # наименование порта
	t = 0.5                                                 # таймаут ожидания ответа
	cmd = '#01\n'                                           # команда, отправляемая на устройство
	s = sched.scheduler(time.time, time.sleep)              # планировщик

	COM_Port = serial.Serial(COM_PortName)                  # открытие порта
	#print(COM_Port)
	#print(COM_PortName,'Opened')
	#print('Connected:', COM_Port.isOpen())
	if COM_Port.isOpen():                                   # проверка открытия порта
		print('\nПорт {} открыт'.format(COM_PortName))
		subprocess.call("./config_rs485.sh")            # конфигурация порта на уровне ОС
		for i in range(10):				# итерация посекундно, вызов функции query с аргументами
			s.enter(i, 1, query, (COM_Port, cmd, t))
		s.run()						# запуск залпанированных событий
		COM_Port.close()                                # закрытие порта
	else:
		print('\nНе удается открыть порт {}'.format(COM_PortName))

if __name__ == "__main__":
	main()

