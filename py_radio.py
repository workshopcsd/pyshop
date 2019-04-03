import serial

arduinoSerialData= serial.Serial('/dev/cu.usbmodem14101',25000)

#file1=open('radio_python.txt','a')

data=[]
hex_data=[]
while 1==1:
	if (arduinoSerialData.inWaiting()>=0):
		myData=arduinoSerialData.readline()
		print hex(int(myData))
		#file1.write(myData)
		if len(data) < 16:
			data.append(myData)
		if len(data) == 16:
			hex_data.append(data)
		print hex(int(hex_data))

serial.close()
