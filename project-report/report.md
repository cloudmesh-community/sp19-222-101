:warning: This is in review 

:wave: check how to seed a table and figure

# Spam Analysis with Spamalot

| Eric Bower, Tyler Zhang
| epbower@iu.edu, tjzhang@iu.edu
| Indiana University Bloomington
| hid: sp19-222-101
| github: [:cloud:](https://github.com/cloudmesh-community/sp19-222-101/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/sp19-222-101/tree/master/project-code)

---

Keywords: Spam

---

 

## Abstract

Summarize the question, purpose of the project. 

## Introduction

The goal is the creation of a service that can classify spam emails. By the term
"spam email", we refer to emails that are sent with malicious intent against the
recipient. Emails without malicious intent will be referred to as a "ham email".
We are exploring the possibility of predicting malicious intent in a given email
using a machine learning algorithm.

Classifying malicious emails can prevent harmful situations for users who are
unaware of the dangers of phishing. Spam email often directs users toward dangerous
websites or download malware or other unwanted software to the host computer. An 
example of malware is ...give an example and what it does.

:wave: Give an example of malware and what can be done with phishing emails. 

It is also important to minimize the number of false positives - i.e. minimize
the number of ham emails that are erroneously labeled as spam. This practice
would be quite unfriendly to the user.

:wave: the above sentence is jargony this is called miss classification
you need to discuss why miss classification is bad (i know it is obvious).

:warning: A paragraph needs at least 3-5 sentences keep the intro one paragraph
or make full paragraphs. 

## The Algorithm

We considered the Naive Bayes and Support Vector Machine (SVM) algorithms
for our implementation of spam classification. Naive Bayes
classifiers are typically used for spam filtering and
document classification problems [@khorsi2007overview]. The Naive Bayes
algorithm relies on Bayes' probability theorem, which expresses a relationship
between the probability of the occurence of an event E given the occurence of
other events, $x_1$ through xn [@zhang2004optimality]. In terms of classification,
event E would be the classication of a data point, and x1 through xn are the
features of that data point. The underlying assumption of the Naive Bayes
classifier is that each of the features are independent of the value of the
class variable, which simplifies the calculations significantly. As a result,
this classification method is fast compared to more sophisticated
methods. Despite the "naive" assumptions of the independence of each feature,
the end classification sensitive to the distribution of dependencies between all
features [@zhang2004optimality], which makes this method successful when
classifying trends in natural language situations.

SVM is also used to work with natural language classification
[@khorsi2007overview]. SVM models construct hyper-planes in the feature space of
the dataset which can be used for classification. The hyper-plane is chosen by
finding the optimal plane that maximizes its margins of separation between
points of all classes [@gunn1998support]. In other words, data points are
separated from the others based on their features in an optimal manner. SVM
algorithms are very effective classifiers when working with datasets that
utilize a large number of features [@gunn1998support]. In the case of emails, we
can calculate the frequency of words contained in the email, which will be a
vector with a large number of features [@khorsi2007overview]. As a result, SVM
is an appropriate model to classify spam emails due to the high dimensional
dataset.

Both the machine learning algorithms above are supervised learning
algorithms. Both algorithms have weaknesses. The Naive Bayes algorithm works
best when dependencies distribute evenly in classes [@zhang2004optimality], but
if this is not the case, Naive Bayes will not be optimal. SVM is much slower
than Naive Bayes, but typically tend to be more statistically robust
[@sculley2007relaxed]. We experimented with both algorithms and chose which one
to use based on their performance and respective statistics.

## The Dataset

The dataset used to train the machine learning algorithm is taken from a project
that tested the effectiveness of five different variations of Naive Bayesian
classifiers on classifying spam emails. It contains the text of ham and spam
messages from a member of Enron corpus with random ham-spam ratio
[@metsis2006spam]. These emails are all labeled as ham or spam.

The raw messages of each email generally contain too much information to be
considered useful to train the classifier. We removed punctuation marks and
special characters.

Additionally, previous research has shown the usefulness of lemmatization in
spam filtering [@androutsopoulos2000evaluation], which is the process of
grouping together variations of the same root word. For instance, a lemmatizer
would group all instances of the words "include", "includes", and "included" in
the same category. We ran a lemmatizer on the dataset as well.

The filtered emails were then separated into vectors of word frequencies. These
were treated as the features for the machine learning model, with "spam" or
"ham" being the labels.

As standard general practice, we randomly chose 80% of these vectors to train
both the SVM and Naive Bayes models, and used the remaining 20% of these vectors
to assess the quality of each model.

## Model Results

The following image shows the confusion matrix for the Naive Bayes algorithm:
The confusion matrix generated from the Naive Bayes algoritgm is represensted
in @fig:nb-conf-mat. 

![NB Confusion Matrix](images/NB_Confusion_Matrix.png){#fig:nb-conf-mat}

The following image shows the confusion matrix for the SVM algorithm:
![SVM Confusion Matrix](images/SVM_Confusion_Matrix.png)

Although the Naive Bayes method correctly identified more ham as ham, it also
mislabeled more spam as ham. For the user, this would translate to more
malicious emails being allowed to pass through the filter without being flagged,
which is dangerous. On the other hand, the SVM method correctly identified more
spam as spam. However, it also mislabeled more ham as spam. For the user, this
translates to more benign emails being flagged as spam. Overall, the SVM method
would be considered safer, because it would expose less harmful emails to the
user, at the cost of incorrectly flagging ham emails more often. For this
reason, we decided to use the SVM model for our classification method.

## Implementation

### The Server

We used Swagger OpenAPI to create our server. This package lets us conveniently
define our server's endpoints and REST API operations in a concise YAML file. In
addition to Swagger OpenAPI, we also greatly utilized the Flask package. In our
YAML file, our server has one endpoint called 'upload', which acts as a REST
POST operation. The 'upload' function corresponding to this endpoint is defined
in a file called gatherData.py. It uses Flask.request() to read in a user's text
file. Once the file has been accepted, the text file is processed and the
classification occurs. The results of the classification are then returned and
displayed to the user as an HTML page using Flask.render_template(). The upload
function and the classification process is explained in more detail in the next
section.

It should be noted that the upload endpoint cannot be reached directly by URL;
it can only be accessed by pressing a JavaScript button on the home page of the
server, which then calls the Flask.request() function and starts the
classification process. If a user attempts to access the upload endpoint via URL
instead of clicking the button, they will be taken to an error page. Once a user
successfully sees the classification results, they are given the option to
return to the home page via another JavaScript button, where they can upload
another email for classification.

We created a Dockerfile that contains all the necessary files needed to host the
server. Running the server in a container such as Docker is beneficial because
installation will not interfere with the host system, and the container is easy
to remove once installed.

The following shows the basic workflow of our server:
![Classification Flowchart](images/classification_workflow.png)

### The Upload Function and Classification

The majority of the computation of our service occurs from the function called
upload. This function takes a file from the user as an input and classifies it
as either spam or ham. The file is retrieved by utilizing the request function
in the Flask package. This file must have a .txt extension and must contain the
body of the email to be classified.

Once the file is uploaded, a function called extract_features is applied to the
file. The extract_features function converts the email text into a word
frequency vector. This feature vector is then used as an input for the SVM model
to classify the email as spam or ham.

Our server contains a previously-trained SVM model file, so it will not need to
retrain the model each time a user uploads a new file. Initially, we used
sklearn to train an SVM model on a large number of emails, creating a large
database of word frequency vectors and their corresponding
classifications. Using the pickle package, we saved this model as a file on the
server. Upon calling the upload function and successfully creating a feature
vector for the user's uploaded email, the server uses pickle to load the saved
model and predicts whether the user's email is ham or spam.

The final piece of information that the upload function calculates is a
performance statistics for the SVM model, including accuracy, precision,
sensitivity, recall, and F1 score. This gives the user insight on the
performance of the SVM model. Once the server has made a prediction and has
performance statistics, it uses the render_template function from the Flask
package to display an HTML file with the returned variables. This is what the
user finally sees after uploading their email file.

## Sources

(will remove) * <https://staysafeonline.org/stay-safe-online/online-safety-basics/spam-and-phishing/>
