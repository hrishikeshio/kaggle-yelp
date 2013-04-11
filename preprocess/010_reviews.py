"""
Tokenize reviews
"""
import nltk
import csv
import sys
from nltk.tokenize import *
from nltk.corpus import stopwords
stemmer=nltk.stem.PorterStemmer()
stems = nltk.probability.FreqDist()
corpus=[]
input_file=sys.argv[1]
output_file=sys.argv[2]
#with open("../data/test_review_stemmed.csv","wb") as fo:
#with open("../data/train_review_stemmed.csv","wb") as fo:

if "test" in input_file:
	Test=True
else:
	Test=False
with open(output_file,"wb") as fo:
	fow=csv.writer(fo)
	#with open("../raw/yelp_test_set_review.csv","rb") as f:
	#with open("../raw/yelp_academic_dataset_review.csv","rb") as f:
	with open(input_file,"rb") as f:
		fr=csv.reader(f)
		header=fr.next()
		if not Test:
			fow.writerow(header)
		for i in fr:
			review="".join(i[4].strip().splitlines())
			review= WhitespaceTokenizer().tokenize(review)
			review_stem=""
			for word in review:
				if word.lower() in stopwords.words("english"):
					continue
				review_stem+=(stemmer.stem_word(word.lower()))+" "
			fow.writerow(i[:4]+[review_stem]+i[5:]+[0,0,0])



print "Tokenization done"