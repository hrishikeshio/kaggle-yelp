import csv
import sys

if not sys.argv[1]:
	print "input,column,value,output"
inputff=sys.argv[1]
inputf=open(inputff,"rb")


column=sys.argv[2]
value=sys.argv[3]
outputf=open(sys.argv[4],"wb")

#Write header
ic=csv.reader(inputf)
ic.next()
oc=csv.writer(outputf)
#oc.writerow(ic.next()+[column])
for i in ic:
	oc.writerow(i+[value,value,value])
