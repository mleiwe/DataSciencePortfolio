# Ml-ZoomCamp_CancerMidTerm
 ML ZoomCamp midterm project. The aim is to create a ML solution to a problem of your choosing.
 
# Introduction
 Tumours are abnormal growths in the body. While not pleasant there are different risks associated with the different types.

 ## Types of Tumours
 There are (very) broadly two types of tumours
 * Benign tumours: These are not necessarily dangerous. Classic examples are skin moles, and lipomas (a small bump of excess fat cells). To cut a long story short they don't cause cancer.
 * Malignant tumours: These are the dangerous ones which cause cancer, and can metastasise (spread) to other parts of the body. In non-clinical terms, these need to be removed ASAP.

 ## Treatment
 Typically these can either be surgically removed, and/or reduced by radiotherapy/chemotherapy.

 While arduous for the patient, these therapies/treatments are most effective when started early. Therefore early and effective diagnosis is essential.

 ## Diagnosis
 Typically biopsies (cutting out a small sample) of the tumour are taken and then imaged using a microscope where the technician determines whether the tumour is benign (safe) or malignant. 
 
 This is an important step, as misclassification as benign (False negative) could delay effective treatment. While misclassifying as malignant (False positive) could put the patient through unnecessary medical procedures.

 ## Challenge
 Manual classification of tumour cells is extremely time-consuming. If we can apply machine learning techniques to increase both speed and accuracy of detection it will improve patient outcomes.

 To this end, the Wisconsin data set has collated tabulated data that describes the spatial properties of both malignant and benign tumour cell nuclei. This will form the basis of our model.

# Dataset
 Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe the characteristics of the cell nuclei present in the image.

 * This is stored as `data.csv` in the repository. 
 * A text description is available as `data_descriptions.md`. 
 * The process of extracting this data is described [here](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)

# Notebook
 ### How to run
 The notebook was originally created as a kaggle notebook, but the key libraries to add are listed below.
 * pandas
 * numpy
 * matplotlib.pyplot
 * seaborn
 * scikit-learn
 * xgboost
 * lightgbm
 * pickle

 ### Key findings
 The data set is nicely curated but with approximately 30 variables is quite large. By utilising principal component analysis (PCA) I engineered 10 features that explain 95% of the variance. Many models were assessed using a gridsearch method, with the scoring metric being the F1 score due to a class imbalance in the dataset. I found that the most effective model on the validation set was a logistic regression classifier on the 10 Principal components. (see figure below)
![ModelEval](https://github.com/mleiwe/Ml-ZoomCamp_CancerMidTerm/assets/29621219/bcad93e2-c776-4959-bfad-da2307cd76f8)

# How to deploy locally
 You can run this service locally using the docker file (provided you have docker installed).
 
 ## Build the machine
 1. Open a terminal
 2. Change the directory to where you have downloaded the app
 3. Build the docker with `docker build -t cancer_prediction .`
 4. Run the docker with `docker run -it --rm -p 9696:9696 cancer_prediction

 ## Query the model
 1. Open a new terminal
 2. Navigate to the directory where the repository was downloaded
 3. Type `python PredictTest.py`
    3. If needed feel free to change the values for the query
 ## Demonstration
 An example of the run can be seen [here](https://drive.google.com/file/d/1GYHSnt4kjrok5_YWjQTfuMpZVzAfncNf/view?usp=drive_link)
