# Tokenize
rm data/test_review_stemmed.csv
rm data/train_review_stemmed.csv

python preprocess/010_reviews.py raw/yelp_test_set_review.csv data/test_review_stemmed.csv
echo "Tokenized Test"
python preprocess/010_reviews.py raw/yelp_academic_dataset_review.csv data/train_review_stemmed.csv
echo "Tokenized Train"


# Combine files
rm data/combined.csv
cat data/train_review_stemmed.csv data/test_review_stemmed.csv > data/combined.csv
echo "Combined"
# Convert to vw

rm data/combined.vw
python preprocess/2vw.py data/combined.csv data/combined.vw
echo "Converted"
# Split 


split -l 229907 data/combined.vw 
echo "Splitted"
mv data/xaa data/train.vw
mv data/xab data/test.vw
echo "Renamed"
# Train vw
vw -d data/train.vw -c -f model --passes 20
echo "Trained"
vw -t -d data/test.vw -c -i model -p data/p2.txt
echo "All done"