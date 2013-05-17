#!/usr/bin/python

# AniHOME 1.0
# http://www.anikos.org/
# 
# This work is licensed under the Creative Commons License,
# visit: http://creativecommons.org/licenses/by-nc-sa/3.0/.


import time
import RPi.GPIO as GPIO
import cgi,time,string,datetime
from os import curdir, sep, path
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from time import gmtime, strftime
import serial
import struct

# Read Sensors data from USB/Serial connected Arduino

# ser = serial.Serial('/dev/ttyACM1', 19200)
# f = open('results.txt','w')

# while 1:
#        temp=strftime("%Y-%m-%d %H:%M:%S", gmtime())+'\t'+ser.readline()
#        print(temp)
#        f.write(temp)
#        f.close()
#        f = open('results.txt','a')
#        time.sleep(5)
#


# Set GPIO Pins !! Do Not Change !!
c1 = 17
c2 = 22
c3 = 10
c4 = 9
c5 = 11
on = 18
off = 23
a = 24
b = 25
c = 8
d = 7

# Set to use IO No.
GPIO.setmode(GPIO.BCM)


GPIO.setup(a, GPIO.OUT)
GPIO.output(a, False)

GPIO.setup(b, GPIO.OUT)
GPIO.output(b, False)

GPIO.setup(c, GPIO.OUT)
GPIO.output(c, False)

GPIO.setup(d, GPIO.OUT)
GPIO.output(d, False)

GPIO.setup(on, GPIO.OUT)
GPIO.output(on, False)

GPIO.setup(off, GPIO.OUT)
GPIO.output(off, False)

GPIO.setup(c1, GPIO.OUT)
GPIO.output(c1, False)

GPIO.setup(c2, GPIO.OUT)
GPIO.output(c2, False)

GPIO.setup(c3, GPIO.OUT)
GPIO.output(c3, False)

GPIO.setup(c4, GPIO.OUT)
GPIO.output(c4, False)

GPIO.setup(c5, GPIO.OUT)
GPIO.output(c5, False)



class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
        	self.send_response(200)
        	self.send_header('Content-type', 'text/html')
        	self.end_headers()        	
        	
        	datastring = str(self.path).split("request/")[1]        	
        	letter = datastring.split("/")[0]
        	letter = string.upper(letter)
        	status = datastring.split("/")[1]
        	status = string.lower(status)
        	code = datastring.split("/")[2]        	
        	code1 = code[0]
        	code2 = code[1]
        	code3 = code[2]
        	code4 = code[3]
        	code5 = code[4]
        	
        	# Testing
        	#self.wfile.write(datastring)
	       	
	       	if letter != "":
				if letter == "A":
					GPIO.output(a, True)
				elif letter == "B":
					GPIO.output(b, True)
				elif letter == "C":
					GPIO.output(c, True)
				elif letter == "D":
					GPIO.output(d, True)
				
				if status == "on":
					GPIO.output(on, True)
				elif status == "off":
					GPIO.output(off, True)
				
				if code1 == "1":
					GPIO.output(c1, True)
				if code2 == "1":
					GPIO.output(c2, True)
				if code3 == "1":
					GPIO.output(c3, True)
				if code4 == "1":
					GPIO.output(c4, True)
				if code5 == "1":
					GPIO.output(c5, True)
				
				time.sleep(1)
				
				if letter == "A":
					GPIO.output(a, False)
				elif letter == "B":
					GPIO.output(b, False)
				elif letter == "C":
					GPIO.output(c, False)
				elif letter == "D":
					GPIO.output(d, False)
					
				if status == "on":
					GPIO.output(on, False)
				elif status == "off":
					GPIO.output(off, False)
				
				if code1 == "1":
					GPIO.output(c1, False)
				if code2 == "1":
					GPIO.output(c2, False)
				if code3 == "1":
					GPIO.output(c3, False)
				if code4 == "1":
					GPIO.output(c4, False)
				if code5 == "1":
					GPIO.output(c5, False)
				
				time.sleep(0.5)
		return
	except IOError:
		self.send_error(404,'File Not Found: ' + self.path)



def main():
    try:
        srv = HTTPServer(('', 8888), Handler)
        print 'Starting AniHOME server'
        srv.serve_forever()
    except KeyboardInterrupt:
        print 'Stopping AniHOME server'
        srv.socket.close()


if __name__ == '__main__':
  main()

