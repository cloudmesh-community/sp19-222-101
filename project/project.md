###Welcome to Spamalot!

##Introduction
The goal of this project is the creation of a service that can classify
spam emails. By the term "spam email", we refer to emails that are sent with
malicious intent against the recipient. Emails without malicious intent will be
referred to as a "ham email". We are exploring the possibility of predicting
malicious intent in a given email using a machine learning algorithm.

Classifying malicious emails can prevent harmful situations for users who are
unaware of the dangers of phishing. Links in these emails can lead to dangerous
websites or download viruses and other unwanted software, so it is important
to classify spam emails accurately.

It is also important to minimize the number of false positives - i.e. minimize
the number of ham emails that are erroneously labeled as spam. This practice 
would be quite unfriendly to the user.

##The Algorithm
We have considered two main algorithms for our implementation of spam
classification: the Naive Bayes and Support Vector Machine (SVM) algorithms.

Classically, Naive Bayes classifiers are typically used for spam filtering and
document classification problems. The Naive Bayes algorithm relies on Bayes'
probability theorem, which expresses a relationship between the probability
of the occurence of an event E given the occurence of other events, x1 through
xn. In terms of classification, event E would be the classication of a data 
point, and x1 through xn are the features of that data point. The underlying
assumption of the Naive Bayes classifier is that each of the features are 
independent of the value of the class variable, which simplifies the
calculations significantly. As a result, this classification method is fast
compared to more sophisticated methods. Despite the "naive" assumptions of the
independence of each feature, the end classification sensitive to the
distribution of dependencies between all features, which makes this method 
successful when classifying trends in natural language situations.



##The Dataset


##Sources
