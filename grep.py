import sys
import os

def get_file():
	if len(sys.argv) == 3:
		pattern=sys.argv[2]
		f_name=sys.argv[3]
		return pattern, f_name
	else:
		print("Python <script_name> <pattern> <file_name>")
		exit()

def return_pattern(pattern,f_name):
	pattern=str(input("Enter the String : "))
	f_dis = open(f_name)
	ret_pat=' '
	for line in f_dis:
		if line == pattern:
			ret_pat+= line		
	print(ret_pat)
	f_dis.close()

return_pattern(get_file())

