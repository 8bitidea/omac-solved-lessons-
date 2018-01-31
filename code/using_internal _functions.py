#-------------------------------------------
#One Million Arabic Coder (OMRC)
#patch Full Stack Web Dev .1
#Lisson 13 Problem Solving 
#Please note that i am sharing this code to 
#find  the idea behined the problem not for
#copy and pasting !
#and i wish if you can find a mistake or ha
#ve a better answer let me know or correct 
#me please
#thank you in advance for correcting me ;)
#I'm Byte idea (Say Hi : 8bitidea@gmail.com)
#-------------------------------------------

#this code wil; not run except you using pythos as root user
#becarful when you deal with root user 

import os 


def put_in_file(file_name , command):
	file = open(file_name , "w")
	file.write(command)
	file.close()

def read_from_file(file_name , line):
	file = open(file_name,"r")
	if (int(line) == 0): x= file.read()
	else: x= file.read(line)
	file.close()
	return x

def do_file():
	bashCommand = "sudo chmod +755 x"
	print os.system(bashCommand)
	bashCommand = "./x"
	print os.system(bashCommand)


def init():
	os.chdir(r"/Users/Macintosh")
#	print read_from_file("2.rtf","0")
	put_in_file("x","ls")
	print read_from_file("x","0")
	do_file()


init()