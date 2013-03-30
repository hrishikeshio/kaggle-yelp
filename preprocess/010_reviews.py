import nltk
import csv
print 57
from nltk.tokenize import *
stemmer=nltk.stem.PorterStemmer()
stems = nltk.probability.FreqDist()
corpus=[]
with open("../processed/test_review_stemmed.csv","wb") as fo:
	fow=csv.writer(fo)
	with open("../raw/yelp_test_set_review.csv","rb") as f:
		fr=csv.reader(f)
		fr.next()
		for i in fr:
			review="".join(i[4].strip().splitlines())
			review= WhitespaceTokenizer().tokenize(review)
			review_stem=""
			for word in review:
				review_stem+=(stemmer.stem_word(word.lower()))+" "
			fow.writerow([review_stem])

print len(corpus)
print corpus[:5]