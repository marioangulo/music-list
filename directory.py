##
# ver 1.0
# Project Description:
# This is just the start of my project im going to implement using python as a backend to do the functionality 
# then I will implement some type of front end which lets you select and deselect what you want to save to a file.
##
import os

def getDirectoryStructure(path):

	fout = open("musiclist.txt", "w")

	for (path, dirs, files) in os.walk(path):
            fout.write("--------------------------\n")
	    fout.write(path + "\n")
	    for d in dirs:
	    	fout.write("\t" + d + "\n")
		for f in files:
			fout.write("\t\t" + f + "\n")
	    fout.write("--------------------------\n")
	    
	fout.close()
	print "Finished!"


print "Input your music directory path >"
path = raw_input();

getDirectoryStructure(path);