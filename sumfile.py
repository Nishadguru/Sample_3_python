import sys
import os

def get_file():
	if len(sys.argv) == 2:
		f_name=sys.argv[1]
		return f_name
	else:
		print("Python <script_name> <file_name>")
		exit()

def sum_numbers(f_name):
	f_dis = open(f_name)
	numbers=0
	for line in f_dis:
		numbers+=int(line)	
	print(numbers)
	f_dis.close()

sum_numbers(get_file())

NOT EXECUTING

"""import sys
import os

def get_file():
	if len(sys.argv) == 2:
		f_name=sys.argv[1]
		return f_name
	else:
		print("Python <script_name> <file_name>")
		exit()

def sum_numbers(f_name):
	f_dis = open(f_name)
	f_lines=f_dis.read()
	
	sum_num=0
	list1=[]
	list2=[]
	for i in f_lines:
		if i.isdigit():
			list1.append((i))
		elif i.isalpha():
			list2.append((i))
	#print(list1)		
		sum_num= sum(list1)	
	print("Sum of all numbers in the file: ",sum_num)
	f_dis.close()

sum_numbers(get_file())
"""

