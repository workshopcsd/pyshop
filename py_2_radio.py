import serial

ser=serial.Serial('/dev/cu.usbmodem14101','25000')

with open('data_radio2.txt','w+') as f:
	while True:
		line=ser.readline()
		f.writelines([line.strip()])
