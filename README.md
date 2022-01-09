# AMLS-assignment
AMLS final assignment

# A brief introduction of the task.
The assignment required the training of classification models for an MRI brain tumor dataset. Task A required the training of a binary classifier to classify whether there was a tumor or not in the image. Task B required training a classifier to classify four classes determining whether a tumor was present and what kind of tumor it was.

Task A was completed using traditional machine learning and computer vision methods. This includes features extraction using HOG and 2D-DWT. Additionally, PCA and standard scalers were used to reduce the size and number of features. Finally, the features were classified using SVM, KNN and Random Forest classifiers

Task B used the same code as in task A however modified for multi-class classification. It also included transfer learning using base network architectures or VGG16, Xception and EfficientNetB4. These were all evaluated in the report written.

# A brief description of the organization of the files.
* The dataset will need to be downloaded from the following [link](http://shorturl.at/hquDP) and extracted to a folder called 'dataset' within the AMLS github repository. Within this dataset folder the test dataset will need to be placed and can be found [here](https://moodle.ucl.ac.uk/mod/url/view.php?id=2629488) and needs to be extracted.
* The directories Task A and Task B contain the files necessary to create and train the models for each respective task.
* Additional files present include an initial data exploration file which contains information about the dataset.
* The file structure is shown below.

📦AMLS-assignment <br>
  ┣ 📜.gitignore<br>
  ┣ 📜data_exploration.ipynb<br>
  ┣ 📜LICENSE<br>
  ┣ 📜README.md<br>
  ┣ 📜requirements.txt<br>
  ┣ 📂dataset<br>
  ┃ ┣ 📂image<br>
  ┃ ┣ 📜label.csv<br>
  ┃ ┣ 📂test<br>
  ┃ ┃ ┣ 📂image<br>
  ┃ ┃ ┗ 📜label.csv<br>
  ┣ 📂Task A<br>
  ┃ ┗ 📜main.ipynb<br>
  ┗ 📂Task B<br>
  ┃ ┣ 📜mainB.ipynb<br>
  ┃ ┣ 📜transfer_learning_augmented_task_B.ipynb<br>
  ┃ ┣ 📜transfer_learning_evaluation.ipynb<br>
  ┃ ┗ 📜transfer_learning_Task_B.ipynb<br>


# Required packages
* tensorflow-gpu
* numpy
* pandas
* matplotlib
* opencv-python
* sklearn
* scipy
* scikit-image
* ipykernal
* tqdm

# How to run the code
## Creating environment and installind dependancies
* Download python 3.9.7 and anaconda
* Create a virtual environment in python 3.9.7
* Install requirements.txt into the environment
* Run ipynb in jupyter notebook or IDE of choice
## Data Exploration
* The first file created was [data_exploration.ipynb](data_exploration.ipynb). This file was created to see see what the dataset was like and how it was structured. This was critical to deciding how to approach the data preprocessing for the classifiers to work with.
* To run this file, first activate the environment created earlier and open the file. Then run each cell sequentially.
## Task A
* Activate the environment created above.
* Run [Task A/main.ipynb](Task%20A/main.ipynb). This file contains all the code to preprocess the data, extract features from the images, train a classifier, and evaluate the models.
## Task B
* Activate the environment created.
* Run [Task B/mainB.ipynb](Task%20B/mainB.ipynb). This file contains the same code as in [Task A/main.ipynb](Task%20A/main.ipynb) however it has been adapeted for Task B. The key differences include performing data augmentation on the entire dataset, and changing the labels from binary to multiclass.
* Run [Task B/transfer_learning_Task B.ipynb](Task%20B/transfer_learning_Task%20B.ipynb). This file was the first transfer learning file created. It contains transfer learning methods and trains 3 models.
* Run [Task B/transfer_learning_augmented_task_B.ipynb](Task%20B/transfer_learning_augmented_task_B.ipynb). This file is similar to the file above however it has a data augmentation step to evaluate the same models in the file above on a data augmented training set.
* Run [Task B/transfer_learning_evaluation.ipynb](Task%20B/transfer_learning_evaluation.ipynb). This file was used for the evaluation of the models trained in the two transfer learning files above.
