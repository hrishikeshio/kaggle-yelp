import json
import sys
import csv

#f=sys.argv[1]
fi=open("../raw/yelp_academic_dataset_review.json" ,"rb")
first=json.loads(fi.next())
#print first
header=[]
for k,v in enumerate(first):
	header.append(v)
print header

with open("../raw/yelp_academic_dataset_review.csv", "wb") as fo:
	fw=csv.writer(fo)
	for line in fi:
		#print line
		linejson=json.loads(line.strip())
		#print "".join(linejson["text"].splitlines())
		#print linejson["votes"]["funny"]
		row=[linejson["votes"]["funny"],linejson["votes"]["useful"],linejson["votes"]["cool"]]
		for i in  range(1,len(header)):
			try:
				int(i)
			except:
		print (["".join(str(linejson[header[i]]).splitlines()) for i in range(1,len(header))])
		row+=(["".join((linejson[header[i]]).encode("utf-8","ignore").splitlines()) for i in range(1,len(header))])
		fw.writerow(row)

