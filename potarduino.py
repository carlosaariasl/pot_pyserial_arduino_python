import serial,time

arduino=serial.Serial("COM5",9600)
time.sleep(2)

try:
	dato=arduino.readline()
	while True:
		dato=arduino.readline()
		dato=dato.decode('utf-8')
		print(dato)

except KeyboardInterrupt:
	arduino.close()
	print("Fin")