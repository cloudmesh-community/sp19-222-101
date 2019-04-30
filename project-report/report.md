# Spam Analysis with Spamalot


| Eric Bower, Tyler Zhang
| epbower@iu.edu, tjzhang@iu.edu
| Indiana University Bloomington
| hid: sp19-222-101
| Github: [:cloud:](https://github.com/cloudmesh-community/sp19-222-101/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/sp19-222-101/tree/master/project-code)

---

Keywords: Spam

---


## Abstract

Spam emails are an issue in cybersecurity because they can contain phishing
scams or malware that can steal private information from the user, which can
often lead to identity theft. These emails are particularly dangerous because
many are seemingly innocuous. We are exploring the possibility of predicting
malicious intent in emails by using a machine learning algorithm. We chose to
use the Support Vector Machines (SVM) algorithm to classify spam emails due to
its superior classification performance over another commonly used
classification model, the Naive Bayes algorithm. Successfully classifying a
malicious email can prevent harmful situations for users.

## Introduction

The goal is the creation of a service that can classify spam emails. By the term
"spam email", we refer to emails that are sent with malicious intent against the
recipient. Emails without malicious intent will be referred to as a "ham email".
Common forms of malicious intent that steal or restrict a user's personal data
include phishing and malware.

Phishing describes a process in which an attacker impersonates a trustworthy
third party in an attempt to obtain sensitive information
[@jagatic2007social]. In a recent phishing attack, a link was sent to Snapchat
users telling them to enable two-step authentication. This link collected the
login information of more than 50,000 Snapchat users. Users were under the
impression that they were making their private information more secure, but they
instead exposed their personal information to hackers, demonstrating how
phishing attacks can be particularly deceptive.

Spam emails can also have dangerous attachments that contain malware. When these
attachments are downloaded, the malware is unloaded onto the computer system. A
common example of malware is called ransomware, which encrypts local files and
network files, effectively preventing the user from accessing their own
files. The ransomware will ask the user to pay in exchange for decrypting their
files. Even if the user pays, the attacker still has control over the user's
data, which may lead to identity theft [@bridges2008changing].

An email classifier can prevent users from being hit by phishing scams and
malware. We used a machine learning algorithm to classify malicious emails. An
important consideration for the user is to minimize misclassification
errors. When creating our service, we need to be careful to minimize the number
of spam emails that are erroneously labeled as ham and the number of ham emails
that are erroneously labeled as spam. If misclassification occurs, the user is
at risk of opening dangerous spam emails and missing important ones.

## The Algorithm

We considered the Naive Bayes and Support Vector Machine (SVM) algorithms for
our implementation of spam classification. Naive Bayes and SVM are both
supervised learning algorithms, which means that they are trained with data that
is already labeled. Both algorithms have strengths and weaknesses. The Naive
Bayes algorithm generally is faster and less computationally complex
[@zhang2004optimality]. SVM is slower than Naive Bayes but typically tends to be
more statistically robust [@sculley2007relaxed]. We experimented with both
algorithms and chose which one to use based on their performance and respective
statistics.

### Naive Bayes

Naive Bayes classifiers are very commonly used for spam filtering and document
classification problems [@khorsi2007overview]. The Naive Bayes algorithm relies
on Bayes' probability theorem, which expresses a relationship between the
probability of the occurrence of an event $c$ given the occurrence of other
events, $x_1$ through $x_n$ [@zhang2004optimality]. Representing $E$ as $(x_1,
x_2, ... x_n)$, the probability of an event $c$ given $E$ is given in
@eq:equation1 from [@zhang2004optimality].

$$P(c|E)=\frac{P(E|c)P(c)}{P(E)}$${#eq:equation1}

In terms of classification, the vector $E$ would be the features of the data
point, and $c$ is the classification of that data point (either ham or spam). To
create a binary classifier, with two classifications being $c=spam$ and $c=ham$,
the classification of a data point with a feature vector $E$ is given in
@eq:equation2 from [@zhang2004optimality].

$$f_b(E)=\frac{P(c=spam|E)}{P(c=ham|E)}>=1$${#eq:equation2}

The terms $P(c=spam|E)$ and $P(c=ham|E)$ are both calculated using
@eq:equation1. The classification is spam if $f_b(E)$ is greater than or equal
to one, and ham if $f_b(E)$ is less than one. Other researchers have found that
the Naive Bayes classification model has decent precision and recall values when
classifying spam emails. The following @fig:nb_example_results shows the results
of such an experiment of a Naive Bayes classifier run on a data set of 2893
total messages:

![NB Ling-Spam Results[@androutsopoulos2000evaluation]](images/NB_LS_Results.png){#fig:nb_example_results}

#### Metrics

In @fig:nb_example_results, two important performance metrics of the Naive Bayes
algorithm were recall and precision, which are both standard metrics used to
evaluate the effectiveness of a model. Recall is defined as the number of true
positives divided by the sum of true positives and false negatives. To put that
definition in the context of a spam classifier, recall measures the ratio of
spam emails correctly identified as spam compared to the number of actual spam
emails in the data set.

Precision is defined as the number of true positives divided by the sum of true
positives and false positives. To put that definition in the context of a spam
classifier, precision measures the ratio of spam emails correctly identified as
spam compared to the number of emails the classifier thinks are spam. For both
metrics, higher percentages show a superior model. The figure
@fig:nb_example_results demonstrates decently high percentages for recall and
precision when using Naive Bayes as a spam email classifier.

### Support Vector Machines (SVM)

SVM is also used to work in text classification [@khorsi2007overview]. SVM
models construct hyper-planes in the feature space of the dataset which can be
used for classification. The hyperplane is chosen by finding the optimal plane
that maximizes its margins of separation between points of all classes
[@gunn1998support]. In other words, data points are separated from the others
based on their features in an optimal manner.

To better illustrate how SVM works, one can imagine all points of a data set
plotted based on their attributes. The data points that belong to a certain
classification will generally be plotted together in regions because they
normally have similar attributes. A hyperplane is an imaginary divider between
these classification regions that is mathematically calculated based on
distance. The following figure @fig:svm_2D_example shows a visualization of a
two-dimensional hyperplane:

![SVM 2D Visualization[@gunn1998support]](images/SVM_2D_example.png){#fig:svm_2D_example}

This figure shows a divider between general regions of points classified as blue
and points classified as red. Notice that the hyperplane is imperfect; there are
some red points on the blue side of the hyperplane, and there are some blue
points on the red side. Such error is inevitable, but it can be minimized
mathematically. To make a classification on a new piece of data, the algorithm
plots the attributes of a new point and makes a prediction based on which side
of the hyperplane the point falls on.

SVM algorithms are very effective classifiers when working with datasets that
utilize a large number of features [@gunn1998support]. In the case of emails, we
can calculate the frequency of words contained in the email, which will be a
vector with a large number of features [@khorsi2007overview]. As a result, SVM
is an appropriate model to classify spam emails due to the high dimensional
dataset.

## The Data Set

The data set used to train the machine learning algorithm is taken from a
project that tested the effectiveness of five different variations of Naive
Bayesian classifiers on classifying spam emails. It contains the text of ham and
spam messages from a member of Enron corpus with random ham-spam ratio
[@metsis2006spam]. These emails are all labeled as ham or spam.

The raw messages of each email generally contain too much information to be
considered useful to train the classifier. In particular, raw email message text
has many characters that contribute little to the classification of the
email. To counteract this, we removed all non-alphabetical characters from the
data set. Also, we removed any words that were only one character long, such as
'a' and 'I'. Finally, we removed all instances of the word 'the', which turned
out to be one of the most common words in all the training emails.

It has been shown that the process of lemmatization improves classification
performance for spam filtering [@androutsopoulos2000evaluation]. Lemmatization
is the process of grouping together variations of the same root word. For
instance, a lemmatizer would group all instances of the words "include",
"includes", and "included" in the same category. The data set that we used to
train our algorithm was already lemmatized, so we did not need to go through
this process ourselves.

Once the email texts were filtered, we then created vectors of word frequencies
from each email. These are treated as the features for the machine learning
model. Our dataset was already labeled as "spam" or "ham", making it possible to
train the SVM and Naive Bayes supervised learning models. We shuffled the list
of word frequency vectors from the dataset and randomly chose 80% of these
vectors to train both the SVM and Naive Bayes models. We used the remaining 20%
of these vectors to assess the quality of each model.

## Model Results

The confusion matrix generated from the Naive Bayes algorithm is represented in
@fig:nb-conf-mat.

![NB Confusion Matrix](images/NB_Confusion_Matrix.png){#fig:nb-conf-mat}

The confusion matrix generated from the SVM algorithm is represented in
@fig:svm-conf-mat.

![SVM Confusion Matrix](images/SVM_Confusion_Matrix.png){#fig:svm-conf-mat}

We can use the above confusion matrices to obtain metrics for each model. Recall
measures the ratio of spam emails correctly identified as spam compared to the
number of actual spam emails in the data set. For the Naive Bayes model, this
value is $\frac{193}{203+193}=0.487$. For the SVM model, this value is
$\frac{343}{53+343}=0.866$.

Precision measures the ratio of spam emails correctly identified as spam
compared to the number of emails the classifier thinks are spam. For the Naive
Bayes model, this value is $\frac{193}{18+193}=0.915$. For the SVM model, this
value is $\frac{343}{136+343}=0.716$.

Although the Naive Bayes method has higher precision than the SVM, it has
significantly lower recall. The impact this would have on the user is dangerous:
the confusion matrix @fig:nb-conf-mat shows that the Naive Bayes model flags a
great number of spam emails as ham, exposing the user to more malicious
emails. On the other hand, the SVM method has a significantly higher recall
value, but at a lower precision value. The consequences of this are not as dire
for the user: the confusion matrix @fig:svm-conf-mat shows the SVM model flags
more ham emails as spam. While this is inconvenient for the user, the SVM method
is safer because it would expose fewer malicious emails to the user, at the cost
of flagging benign emails as spam more often. For this reason, we decided to use
the SVM model for our classification method.

## Implementation

### The Server

We used Swagger OpenAPI to create our server. This package lets us conveniently
define our server's endpoints and REST API operations in a concise YAML file. In
addition to Swagger OpenAPI, we also greatly utilized the Flask package. In our
YAML file, our server has one endpoint called 'upload', which acts as a REST
POST operation. The upload() function corresponding to this endpoint is defined
in a file called gatherData.py. From the Flask package, upload() uses
Flask.request() to read in a user's text file. Once the file has been accepted,
the text file is processed and the classification occurs. The results of the
classification are then returned and displayed to the user as an HTML page using
Flask.render_template(). The upload() function and the classification process is
explained in more detail in the next section.

It should be noted that the 'upload' endpoint cannot be reached directly by URL;
it can only be accessed by pressing a JavaScript button on the home page of the
server, which then calls the Flask.request() function and starts the
classification process. If a user attempts to access the 'upload' endpoint via
URL instead of clicking the button, they will be taken to an error page. Once a
user successfully sees the classification results, they are given the option to
return to the home page via another JavaScript button, where they can upload
another email for classification.

We created a Dockerfile and a Makefile that contains all the necessary commands
needed to host the server. This Dockerfile runs Ubuntu and runs commands to
clone files from our Github to get the service running. Running the server in a
container such as Docker is beneficial because the installation will not
interfere with the host system, and the container is easy to remove once
installed.

The following diagram @fig:classification-workflow shows the basic workflow of
our server:

![Classification Flowchart](images/classification_workflow.png){#fig:classification-workflow}

### The Upload Function and Classification

The upload() function handles file uploading and makes other function calls to
perform classification. The file is first retrieved by utilizing the
Flask.request() function from the Flask package. This file must have a '.txt'
extension and should contain the body of the email to be classified.

Once the file is uploaded, upload() sends the file to a function called
extract_features(). The extract_features() function converts the email text into
a word frequency vector. This vector is treated as the features of the email and
is used as an input for the SVM model to classify the email as spam or ham.

Our server contains a previously-trained SVM model file, so it will not need to
retrain the model each time a user uploads a new file. We used the sklearn
package to train an SVM model on a large number of emails, creating a large
database of word frequency vectors and their corresponding labels. Using the
pickle package, we saved this model as a file on the server. When the
extract_features() function successfully returns a feature vector for the user's
uploaded email, the server uses the pickle package to load the saved SVM model
and labels the user's email as ham or spam.

The final pieces of information that the upload() function calculates are
performance statistics for the SVM model to create a confusion matrix, from
which the user can calculate model metrics such as precision and recall. This
gives the user insight on the performance of the SVM model. Once the server has
made a prediction and has performance statistics, it calls
Flask.render_template() to display an HTML file with the returned
variables. This is the page the user sees after uploading their email file.

### Specification

```
swagger: "2.0"
info: 
  version: "0.0.1"
  title: "spamInfo"
  description: "An intelligent system to determine whether a given email is spam or not"
  contact: 
    name: "Spamalot"
  license: 
    name: "Apache"
host: "localhost:8080"
basePath: "/"
schemes: 
  - "http"
consumes: 
  - "application/json"
produces: 
  - "text/html"
paths: 
  /upload:
    post:
      operationId: py_scripts.gatherData.upload
      description: "Uploads a file"
      responses:
        "201":
          description: "Upload"  
```

## Conclusion

Our implementation of a spam email classifier is a building block for a more
sophisticated spam filter. Currently, our service is only capable of making
predictions on one email at a time, and each prediction requires the user to
upload a new file containing the email text. A more sophisticated spam filter
would be integrated into an email app and could automatically classify incoming
emails as spam. Additionally, our service's classification ability is
imperfect. As seen in @fig:nb_example_results, other researchers achieve
superior classification performance using Naive Bayes, so there is room for
improvement.

In its current state, our implementation is best suited for single users. But
with some further development, such as adding the ability to classify multiple
emails at once and improving our service's classification performance, a spam
filter would be a useful tool for company employees. Our service could prevent
employees from opening dangerous emails that could steal company information.
