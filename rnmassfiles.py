#!/usr/bin/env python
#programmer Matthew Deig
#idealy made for linux but it should work in windows by giving \\ instead

import os,glob,sys

def getdirlisting(path,ext):
	return glob.glob(path+os.sep+"*."+ext)
	
def changingExt(listing, ext, newext):
	for filename in listing:
		newfilename = filename.split(".")
		
		if newfilename[1] == ext:
			newfilename[1] = "."+newext
			os.rename(filename,newfilename[0]+newfilename[1])

	
if __name__ == "__main__":
	filepath = ""
	ext = ""
	newext = ""
	x=0
	for args in sys.argv:
		if args == "-p" or args == "--path":
			filepath = sys.argv[x+1]
		elif args == "-e":
			ext = sys.argv[x+1]
		elif args == "-ne":
			newext = sys.argv[x+1]
		x+=1
			
	if filepath != "" and ext != "" and newext != "":
		listing = getdirlisting(filepath,ext)
		changingExt(listing, ext, newext)
	else:
		print("usage -p for the path to the maps\n-e is the old extension\n-ne is the new extension")
