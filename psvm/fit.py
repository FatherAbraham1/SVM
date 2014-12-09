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

	maxfeature=0
	maxline =0
	for line in ifile:
		maxline+=1
		linewords = line.rstrip().split(" ")
		for word in linewords[1:]:
			[a,b] = word.split(":")
			if(int(a)>maxfeature):
				maxfeature = int(a)
	print maxfeature	

	ifile.seek(0)

	linecount=0

	for line in ifile:
		newline=''
		linecount +=1
		featurecount=1

		linewords = line.rstrip().split(" ")
		if(linewords[0]!='1'):
			newline+= '-1'
		else:
			newline+= '1'
		
		for word in linewords[1:]:
			
			try:
				[a,b] =word.split(':')
			except Exception, e:
				print"cannot parse:"
				print word
				print linecount
				sys.exit()

			while (featurecount< int(a)):
				newline+=" "+'0'
				featurecount+=1
			newline+=" "+b
			featurecount+=1

		while(featurecount<=maxfeature):
			newline+=" "+'0'
			featurecount+=1

		if(maxline>linecount):
			ofile.write(newline+"\n")
		else:
			ofile.write(newline)
	ifile.close()
	ofile.close()
	print "done!"
	sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])



