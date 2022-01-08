# AMLS-assignment
AMLS final assignment

# A brief introduction of the task.
The assignment required the training of classification models for an MRI brain tumor dataset. Task A required the training of a binary classifier to classify whether there was a tumor or not in the image. Task B required training a classifier to classify four classes determining whether a tumor was present and what kind of tumor it was.

# A brief description of the organization of the files.
The dataset will need to be downloaded from the following link and within this the test dataset will need to be placed inside this directory.
The directories Task A and Task B contain the files necessary to create and train the models for each respective task.
Additional files present include figures used in the report to evaluate the models trained and an initial data exploration file.

# The role of each file.

## data_explotration.ipynb
This file was the first file created and explored the data by seeing how many classes and images were present along with what the images looked like.
## Task A/main.ipynb
This file was used for the binary classification. It has all the trained model along with some data evaluation plotting graphs and inspecting the final results.
## Task B/mainBipynb
This file is almost a copy of the previous file however it has been adapted for the multi-class classification problem. It was used to evaluate the effectiveness of models trained in Task A on Task B.
## Task B/transfer_learning_Task B.ipynb
This file was the first transfer learning file created. It contains transfer learning methods and trains 3 models.
## Task B/transfer_learning_augmented_task_B.ipynb
This file is similar to the file above however it has a data augmentation step to evaluate the same models in the file above on a data augmented training set.
## Task B/transfer_learning_evaluation.ipynb
This file was used for the evaluation of the models trained in the two transfer learning files above.



# How to run your code.
* Download python 3.9.7 and anaconda
* Create a virtual environment in python 3.9.7
* Install requirements.txt into the requirements.txt
* Run ipynb in jupyter notebook or IDE of choice
* Run the jupyter notebooks in the order the files are listed above


# Necessary packages or header files (e.g. numpy, scipy, etc.).
The required files are present in the requirements.txt file