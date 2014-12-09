import argparse
import os
import re
import sys, getopt
def main(argv):

	inputfile=''
	outputfile=''

	try:
		opts,args = getopt.getopt(argv,"hi:o:",["inputfile=","outputfile="])

	except getopt.GetoptError:
		print "format.py -i -o"
		sys.exit(2)

	for opt, arg in opts:
		if opt=='-h':
			print "format.py -i -o"
			sys.exit()

		elif opt in ("-i","--inputfile"):
			inputfile=arg
		elif opt in ("-o","--outputfile"):
			outputfile=arg
	print inputfile
	print outputfile
	try:
		ifile =open(inputfile, 'r')
		ofile = open(outputfile, 'w')	
	except Exception, e:
			print "cannot read file"
			sys.exit()

	linecount=0
	wordcount=0
	
	for line in ifile:
		newline=''
		
		linecount +=1
		if(linecount==1):
			continue
		if(linecount>= 10000):
			break;
		wordcount=0
		linewords = line.split(",")
		if(linewords[-1].rstrip() =='0'):
			newline+= '0'
		else:
			newline+= '1'
		for word in linewords[1:-1]:
			newline+=" "+str(wordcount)+":"+word
			wordcount+=1

		
		ofile.write(newline+"\n")
	ifile.close()
	ofile.close()
	print "done!"
	sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])



