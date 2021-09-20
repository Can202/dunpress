#!/usr/bin/python3

import os
import sys
from sys import exit

def main():
	if len(sys.argv) > 1:
		for i in range(len(sys.argv)):
			if os.path.exists(sys.argv[i]) and i != 0:
				uncompress(sys.argv[i])
			
def uncompress(File):
	print("uncompress " + File)
	END=len(File)
	if File[END-4:END] == ".tar":
		os.system("tar -xvf " + File)
	elif File[END-7:END] == ".tar.gz" or File[END-4:END] == ".tgz":
		os.system("tar -xvf " + File)
	elif File[END-8:END] == ".tar.bz2" or File[END-4:END] == ".tbz" or File[END-5:END] == ".tbz2" or File[END-4:END] == ".tb2":
		os.system("tar -xvf " + File)
	elif File[END-6:END] == ".tar.Z" or File[END-4:END] == ".taz" or File[END-3:END] == ".tz":
		os.system("tar -xvf " + File)
	elif File[END-7:END] == ".tar.lz" or File[END-9:END] == ".tar.lzma" or File[END-4:END] == ".tlz":
		os.system("tar -xvf " + File)
	elif File[END-7:END] == ".tar.xz" or File[END-4:END] == ".txz":
		os.system("tar -xvf " + File)
	elif File[END-4:END] == ".zip":
		os.system("unzip " + File)
if __name__=="__main__":
	main()
