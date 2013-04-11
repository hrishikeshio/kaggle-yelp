# Tokenize
all: data/p2.txt

stanford: data/train_review_stemmed.tsv

# Csv to tsv
data/test_review_stemmed.tsv: data/test_review_stemmed.csv
	@echo "Converting csv to tsv..."
	python preprocess/csv_to_tsv.py data/train_review_stemmed.csv data/train_review_stemmed.tsv
	python preprocess/csv_to_tsv.py data/test_review_stemmed.csv data/test_review_stemmed.tsv
# Run vw
predictions/p2.txt: data/test.vw
	@echo "Running Vowpal Wabbit..."
	vw -d data/train.vw -c -f model --passes 20
	vw -t -d data/test.vw -c -i model -p predictions/p2.txt
# generate vw files
data/test.vw: data/combined.csv 
	@echo "Splitting the file..."
	split -l 229907 data/combined.vw 
	mv xaa data/train.vw
	mv xab data/test.vw
# combine files
data/combined.csv: data/test_review_stemmed.csv
	@echo "Combining Data..."
	cat data/train_review_stemmed.csv data/test_review_stemmed.csv > data/combined.csv
	python preprocess/2vw.py data/combined.csv data/combined.vw
# stemming
data/test_review_stemmed.csv: 
	@echo "Stemming..."
	python preprocess/010_reviews.py raw/yelp_test_set_review.csv data/test_review_stemmed.csv
	python preprocess/010_reviews.py raw/yelp_training_set_review.csv data/train_review_stemmed.csv 
# clean
clean:
	rm data/combined.csv
	rm data/test_review_stemmed.csv
	rm data/train_review_stemmed.csv
	rm model
	rm data/train_review_stemmed.tsv
	rm data/test_review_stemmed.tsv
	rm data/train.vw
	rm data/test.vw

