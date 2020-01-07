# sentiment-analysis-using-machine-learning
Sentiment analysis is contextual mining of text which identifies and extracts subjective information in source material, and helping a business to understand the social sentiment of their brand, product or service while monitoring online conversations

Text Classifier — The basic building blocks
Sentiment Analysis
Sentiment Analysis is the most common text classification tool that analyses an incoming message and tells whether the underlying sentiment is positive, negative our neutral.

We have used Bag of Words method to map text into vector representations.Logistic Regression and Suppoer Vector Classifier(LinearSVC) is used as model.

What we do is :

1)We clean the given data.Symbols are not useful for analysis.Also we remove stopwords like "is,are,am,have etc.." because they are not the decideing words of positive or negative sentiment in the text.

2)Represent every text using vector.From training data, we create a large matrix(Sparse matrix) whose column represent every words in those data,and rows are the actual text in the form of 1 and 0. Words of text corrosponds to column is set to 1 and all other columns 
are 0.

3)Feed this data to logistic and svc model ,so it can train itself about which words appear in the positive sentense and negative sentence.It will assign weight to every word if this word is used for positive/negative feedback.

4)Now,find another texts for which we want to find sentiment,clean that data,vectorise it and give it to model.
It will tell us if it is negative or positive.
