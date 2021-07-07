import NL
import serial
#import time
import subprocess
import json

COM_PortName = '/dev/ttyS0'					# наименование порта
t = 0.5								# таймаут ожидания ответа
cmd = '#01\n'

COM_Port = serial.Serial(COM_PortName)                          # открытие порта
#print(COM_Port)
#print(COM_PortName,'Opened')
#print('Connected:', COM_Port.isOpen())
if COM_Port.isOpen():                                          	# проверка открытия порта
	print('\nПорт {} открыт'.format(COM_PortName))
	subprocess.call("./config_rs485.sh")                    # конфигурация порта на уровн>
	answer = NL.query_ch(COM_Port, cmd, t)			# вызов функции запроса
	try:
		answer = json.loads(answer)			# попытка конвертации JSON
	except ValueError as e:
		print(answer)					# в случае неудачи вывод ответа от устройства
		COM_Port.close()                                # закрытие порта
	else:
		#print('\n')
		print('\nДавление: {} В\nТемпература: {} В'.format(answer["ch2"], answer["ch3"]))
		#print('\n')
		#print(NL.query_ch(COM_Port, cmd, t))		# вызов функции запроса
		COM_Port.close()                                # закрытие порта
else:
	print('\nНе удается открыть порт {}'.format(COM_PortName))

