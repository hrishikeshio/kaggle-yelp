import csv
import sys

with open(sys.argv[1]) as f:
	fr=csv.reader(f)
	with open(sys.argv[2], "wb") as fo:
		fw=csv.writer(fo, delimiter="	")
		for i in fr:
			fw.writerow(i)
