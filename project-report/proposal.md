# Spam Email Classifier.

## Dataset
The dataset we will be working with is a collection of emails from University of California Irvine. The emails are classified as either spam or not spam, and each entry contains attributes, such as the percentage of the email that matches a certain keyword, and the average length of uninterrupted sequences of capital letters. There are a total of 57 features of the emails in this dataset to work with.

The dataset for this project is located at https://archive.ics.uci.edu/ml/datasets/spambase.

## Machine Learning Implementation
Our project will be a naive Bayes binary classifier that predicts whether a given email is spam or not. In terms of workflow, we will use a REST service to upload an email from the user to our server. The server will take the given email, decipher important features relevant to the dataset above, and use the trained model to predict whether or not the given email is spam. The server will send use REST to return the result to the user.

## Research Question
By the term "spam email", we refer to emails that are sent with malicious intent against the receiver. We are exploring the possibility of predicting this malicious intent in a given email. The goal is to create a classifier for spam emails with the lowest possible misclassification rate.

## Who cares?
Classifying a malicious email can prevent harmful situations for users that do not know the dangers of phishing. In a system that takes a spam classification and removes these emails, a low misclassification rate is also important so as to not remove important emails erroneously.
