"""
TFIDF, character 1-5 gram. Borrowed from andreas mueller for insult competition.

"""
from sklearn.feature_selection import SelectPercentile, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline
import csv
import ml_metrics

select = SelectPercentile(score_func=chi2, percentile=18)
clf = LogisticRegression(tol=1e-8, penalty='l2', C=7)
countvect_char = TfidfVectorizer(ngram_range=(1, 5), analyzer="word", binary=False, use_idf=True)
ft = FeatureUnion([("chars", countvect_char) ])
char_model = Pipeline([('vect', ft), ('select', select), ('logr', clf)])

X_train=[]
y_train=[]

with open("data/train_review.csv") as fi:
	fir=csv.reader(fi)
	fir.next()
	for i in fir:
		X_train.append(i[4])
		y_train.append(int(i[9]))
print "Train Data read."
upto=1000
upto2=1500
X_train_s=X_train[:upto]
y_train_s=y_train[:upto]
X_test_s=X_train[upto:upto2]
y_test_s=y_train[upto:upto2]

X_train=[]
y_train=[]
#char_model.fit(X_train_s,y_train_s)
print "training done"
print countvect_char.fit_transform(X_train_s)
#print countvect_char

X_train=[]
y_train=[]

X_test=[]
with open("data/test_review.csv") as fi:
	fir=csv.reader(fi)
	fir.next()
	for i in fir:
		X_test.append(i[4])
print "test data read"

preds = char_model.predict(X_test_s)
print "prediction done"
X_test=[]

#with open("predictions/tfidf_cngram.csv","wb") as fo:
#	fow=csv.writer(fo)
	#fow.writerows(preds)
print "all done"

print ml_metrics.rmsle(preds,y_test_s)