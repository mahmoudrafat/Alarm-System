import serial
import os 
import RPi.GPIO as GPIO 
import time 
pin = 3
a=0       
x = 'Amplitude='
while True:
	graph_data = open ('/home/pi/Desktop/scanLog.txt','r').read()
	lines = graph_data.split('\n')
	file = os.path.expanduser('/home/pi/Desktop/scanLog.txt')
	for line in lines:
		if x in line:
			y= (line[line.find(x) + len(x) :])
			if float(y) > 0:		
					print "power=",y, "Motion  detected!!"
					GPIO.setmode(GPIO.BOARD)
					GPIO.setup(pin,GPIO.OUT)
					GPIO.output(pin, GPIO.HIGH)
					for c in range (10):
						print (c)
						time.sleep(1)
					os.remove(file)
					os.mknod(file)
					fd = os.open ("/home/pi/Desktop/scanLog.txt",os.O_RDWR)
					ref = os.write (fd,"Amplitude=0")
					#time.sleep(5)
					GPIO.cleanup()
					print "RESET"
			else :
					print "NOOOOO"
					GPIO.setmode(GPIO.BOARD)
					GPIO.setup(pin,GPIO.OUT)
					GPIO.output(pin, GPIO.LOW)
					time.sleep(1)
					GPIO.cleanup()
					os.remove(file)
					os.mknod("/home/pi/Desktop/scanLog.txt")
					fd = os.open ("/home/pi/Desktop/scanLog.txt",os.O_WRONLY)
					#ref = os.write (fd,"Amplitude=")
					
			#fd = os.open ("/home/pi/Desktop/scanLog.txt",os.O_WRONLY)
			#ref = os.write (fd,"Amplitude=\n")
				
		
