import serial
import time
import subprocess
import json

#init serial port and bound
# bound rate on two ports must be the same
'''
ser = serial.Serial('/dev/ttyS0', 57600)
print(ser.portstr)
'''

#COM_PortName = input('\n    Enter the COM Port Name ->')
COM_PortName = '/dev/ttyS0'

#Opening the serial port

COM_Port = serial.Serial(COM_PortName) # open the COM port
print('\n')
print(COM_PortName,'Opened')
print('Connected:', COM_Port.isOpen())
'''
COM_Port.baudrate = 57600               # set Baud rate
COM_Port.bytesize = serial.EIGHTBITS                  # Number of data bits = 8
COM_Port.parity   = serial.PARITY_NONE                # No parity
COM_Port.stopbits = serial.STOPBITS_ONE                  # Number of Stop bits = 1
'''

# конфигурация порта на уровне ОС
subprocess.call("./config_rs485.sh")

'''
print('\n    Baud rate = ',COM_Port.baudrate)
print('    Data bits = ',COM_Port.bytesize)
print('    Parity    = ',COM_Port.parity)
print('    Stop bits = ',COM_Port.stopbits)
'''

# посылаемая команда
cmd = '#01\n'
cmdascii = cmd.encode('ascii')

# время ожидания
t = 0.6
#send data via serial port
#time.sleep(t)
COM_Port.write(cmdascii)
'''
time.sleep(1)
COM_Port.write(cmdascii)
time.sleep(1)
COM_Port.write(cmdascii)
time.sleep(1)
COM_Port.write(cmdascii)
time.sleep(1)
'''

print('\nSended command:', cmdascii)
#COM_Port.flush()
print('Timout: {}s ...\n'.format(t))
time.sleep(t)
#subprocess.call("./config_rs485.sh")
answer = COM_Port.readline()
print('Answer in byte:', answer)
answer = answer.decode('ascii')
print('Answer in ASCII:', answer)

# разбор ответа в словарь
answer_json = {}
ch = 1			# номер канала
i = 1			# позиция в строке ответа
answer = answer[1:]	# срез первого символа
print('Ответ после среза:', answer)
val = ""		# строка значений сигнала
for s in answer:
	if (s == '+' or s == '-'):
		if (ch > 1):			# заполнение словаря после прохода первого блока значений
			#print(ch_name, val)
			answer_json[ch_name] = float(val)
			#answer_json.update('{}'.format(ch_name) = float(val))
		ch_name = 'ch' + str(ch)	# формирование имени канала
		#print("ch" + str(ch), answer[i:i + 7])
		ch += 1				# увеличение номера канала
		val = s				# запись знака значения
	else:
		val += s
	#answer_json.update(["ch" + str(i), answer[i:7]])
answer_json[ch_name] = float(val)		# добавление последней пары значений
#print(ch_name, val)
print('\ndict', answer_json)
answer_json = json.dumps(answer_json)
print('\nin JSON', answer_json)

COM_Port.close()
