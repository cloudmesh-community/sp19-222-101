# *py_scripts* directory

### This directory holds the files python files necessary for training the model, receiving a file from flask upload, and returning a prediction for said file.

## gatherData.py
This file includes methods that receive a file, and make a prediction.
### Functions:
#### upload()
Receives the file uploaded from the flask request. Saves this file to the directory */project-code/user_input_files*

Calls the funciton **predict()** from the file trainer.py to acquire a prediction from the model. Finally, it opens a confusion matrix for the model that is saved in */project-code/savedFiles* and sends the prediction, confusion matrix, and other variables back to the web page via **render_template()**

#### findScores()
Opens the previously saved confusion matrix for the model and calculates accuracy, precision, recall, and f1 score from these values and returns these values.


## trainer.py
This file includes methods necessary for training the model and making predictions.
### Functions:
#### make_Dictionary()
Creates a dictionary based on word count in the dataset.
#### extract_features()
Creates a features array which maps each word to the frequency at which it is used.
#### train()
Trains the data using SVM algorithm.
#### randomize()
Randomizes given arrays using the same seed for both arrays.
#### predict()
Makes a prediction from model for the given file. (spam or ham)


***

More info can be found in the project report located at */project-report/report.md*