#!/usr/bin/python3

import os
import sys
from sys import exit

def main():
	directory = ""
	if len(sys.argv) > 1:
		for i in range(len(sys.argv)):
			
			if sys.argv[i] == "-v" or sys.argv[i] == "--version":
				print("v0.1")
				exit()
			
			if sys.argv[i] == "-d":
				if os.path.exists(sys.argv[i+1]):
					directory = sys.argv[i+1]
					sys.argv[i+1] = ""
				else:
					os.system("mkdir -p " + sys.argv[i+1])
					if os.path.exists(sys.argv[i+1]):
						print("dir created")
						directory = sys.argv[i+1]
						sys.argv[i+1] = ""
					else:
						print("error")
						exit()
			if i != 0:
				if os.path.exists(sys.argv[i]):
					uncompress(sys.argv[i], directory)
	else:
		print("""dumpress
		Use:
		dumpress <file>   uncompress
		dumpress -d <folder> <file> uncompress on folder""")
			
def uncompress(File, Dir):
	END=len(File)
	if File[END-4:END] == ".tar":
		if Dir != "":
			Dir = " -C " + Dir
		os.system("tar -xvf " + File + Dir)
	elif File[END-7:END] == ".tar.gz" or File[END-4:END] == ".tgz":
		if Dir != "":
			Dir = " -C " + Dir
		os.system("tar -xvf " + File + Dir)
	elif File[END-8:END] == ".tar.bz2" or File[END-4:END] == ".tbz" or File[END-5:END] == ".tbz2" or File[END-4:END] == ".tb2":
		if Dir != "":
			Dir = " -C " + Dir
		os.system("tar -xvf " + File + Dir)
	elif File[END-6:END] == ".tar.Z" or File[END-4:END] == ".taz" or File[END-3:END] == ".tz":
		if Dir != "":
			Dir = " -C " + Dir
		os.system("tar -xvf " + File + Dir)
	elif File[END-7:END] == ".tar.lz" or File[END-9:END] == ".tar.lzma" or File[END-4:END] == ".tlz":
		if Dir != "":
			Dir = " -C " + Dir
		os.system("tar -xvf " + File + Dir)
	elif File[END-7:END] == ".tar.xz" or File[END-4:END] == ".txz":
		if Dir != "":
			Dir = " -C " + Dir
		os.system("tar -xvf " + File + Dir)
	elif File[END-4:END] == ".zip":
		if Dir != "":
			Dir = " -d " + Dir
		os.system("unzip " + File + Dir)
if __name__=="__main__":
	main()
