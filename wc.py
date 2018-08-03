import os 
import sys

def get_file():
	if len(sys.argv) == 2:
		f_name=sys.argv[1]
		return f_name
	else:
		print("Python <script_name> <file_name>")
		exit()

def count_lines(f_name):
	no_letters,no_words,no_lines=0,0,0
	f_dis = open(f_name)

	for line in f_dis():
		print(line)
		words = line.split(' ')

		no_letters += len(line)
		no_words += len(words)
		no_lines += 1
	
	print("The number of letters are : ",no_letters)
	print("The number of words are : ",no_words)
	print("The number of lines are : ",no_lines)
	f_dis.close()

count_lines(get_file())

