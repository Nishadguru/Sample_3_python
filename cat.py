import sys
import os

def get_filename():
	if len(sys.argv)>1:
		fname = sys.argv[1]
		return  fname
	else:
		print("Usage: pyhton<scriptname> <filename>")
		sys.exit()

def open_file(fname):
	try:
		r_file = open(fname,)
		return	r_file
	except IOError:
		print("File not present",fname)
		sys.exit()

def file_read(f_dis):
	print(f_dis.read())

def file_readline(f_dis):
	
		line= f_dis.readline()
		if not line:
			pass
		else:
			print(line)

def file_readlines(f_dis):
	for line in f_dis.readlines():
		print(line)

def file_close(f_dis):
	f_dis.close()

def testcode():
	fname= get_filename()
	f_dis = open_file(fname)
	file_read(f_dis)
	#file_readline(f_dis)
	file_readlines(f_dis)
	file_close(f_dis)

if __name__=='__main__':
	testcode()

"""
import sys
import os

def Getname():
    if len(sys.argv) == 2:
        name = sys.argv[1]
        return name
    else:
        print("Program will exit now ")
        exit()

def Printing(name):
    try:
        fp = open(name,'r')
        lines = fp.read()
        print(lines)
    except FileNotFoundError:
        print("File not exists!")
        exit()
"""
