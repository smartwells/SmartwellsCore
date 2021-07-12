import serial
serBarCode = serial.Serial('/dev/ttyS0', timeout=1)

serBarCode.baudrate = 57600               # set Baud rate
serBarCode.bytesize = serial.EIGHTBITS                  # Number of data bits = 8
serBarCode.parity   = serial.PARITY_NONE                # No parity
serBarCode.stopbits = serial.STOPBITS_ONE                  # Number of Stop bits = 1

while True:

    #read data from serial port
    dataBarCode = serBarCode.readline()

    #if there is smth do smth
    if len(dataBarCode) >= 1:
        print(dataBarCode.decode(encoding='ascii', errors='ignore'))
