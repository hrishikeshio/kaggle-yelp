train<-read.csv("raw/yelp_academic_dataset_review.csv")
results<-read.csv("predictions/p.txt")
hist(exp(-train$votes_useful))