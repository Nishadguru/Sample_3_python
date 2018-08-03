import sys
import os

def get_file():
	if len(sys.argv) == 2:
		f_name=sys.argv[1]
		return f_name
	else:
		print("Python <script_name> <file_name>")
		exit()

def print_five(f_name):
	f_dis = open(f_name)
	for line in range(0,5):
		txt=f_dis.readline()		
		print(txt,end =' ')
	f_dis.close()

print_five(get_file())

