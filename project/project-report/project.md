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

http://www.cs.unb.ca/~hzhang/publications/FLAIRS04ZhangH.pdf
https://scikit-learn.org/stable/modules/naive_bayes.html

SVM is also used to work with natural language classification. SVM models
construct hyper-planes in the feature space of the dataset which can be used
for classification. The hyper-plane is chosen by finding the optimal plane that
maximizes its margins of separation between points of all classes. In other
words, data points are separated from the others based on their features in an
optimal manner. SVM algorithms are very effective classifiers when working with
datasets that utilize a large number of features. In the case of emails, we can
calculate the frequency of words contained in the email, which will be a vector
with a large number of features. As a result, SVM is an appropriate model to
classify spam emails due to the high dimensional dataset.

https://medium.com/machine-learning-101/chapter-2-svm-support-vector-machine-theory-f0812effc72
https://monkeylearn.com/blog/introduction-to-support-vector-machines-svm/

Both the machine learning algorithms above are supervised learning algorithms.

##The Dataset


##Sources
https://staysafeonline.org/stay-safe-online/online-safety-basics/spam-and-phishing/
