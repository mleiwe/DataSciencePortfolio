'''
This is the train function, this file will read the data.csv which contains the wisconsin cancer data set. Training for a logistic regression classifier undergoes the following steps
1) Drop the 'Unnamed: 32' column
2) Normalise with the SkLearn MinMaxScaler
3) FeatureEngineer with a 10dim PCA
4) Evaluate the logistic regressor on the training data set with 5 folds
5) Train the model on the whole data set
6) Save it as a binary file using pickle

Inputs:
Input variables are listed below in the "Input Variables" Section
data_file: file path for the csv
Model_Params: The parameter settings that have been calculated from the grid search in Notebook.ipynb
Model_Filename: The filename of the output file

Output:
Binary file of the model

Requirements
* pandas
* numpy
* scikit-learn
'''
### Libraries Needed 
import pandas as pd
import numpy as np
import pickle

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score

### Input Variables
data_file = "data.csv"
Model_Params = {
    'class_weight': None, 
    'dual': False, 
    'fit_intercept': True, 
    'intercept_scaling': 1,
    'max_iter': 200, #Increased from the 15 to stop a warning 
    'multi_class': 'ovr', 
    'n_jobs': None, 
    'penalty': None, 
    'random_state': 42, 
    'solver': 'lbfgs', 
    'tol': 0.0001, 
    'verbose': 0, 
    'warm_start': False
} #NB because no penalty C and L1_ratio are not needed
Model_Filename = 'model.bin'

## Load the whole dataset
print('Reading in training data...')
df = pd.read_csv(data_file)
## Split into variables
X = df.drop(labels=['id','diagnosis','Unnamed: 32'], axis=1)
y = df['diagnosis'].replace(['M','B'],[1,0])

print('Scaling data...')
## MinMaxScaler
mms = MinMaxScaler()
mms.fit(X)
X_norm = mms.transform(X)

## PCA
print('Performing dimension reduction...')
pca = PCA(n_components=10)
Xt = pca.fit_transform(X_norm)

## Get some stats about the fit by doing K-Folds
print('Evaluating model performance...')
kf = KFold(n_splits=5, shuffle=True, random_state=42)
f1_scores = np.zeros(5)
c = 0
for train, test in kf.split(Xt):
    X_train = Xt[train,:]
    X_test = Xt[test,:]
    y_train = y[train]
    y_test = y[test]
    
    lrc = LogisticRegression(**Model_Params)
    lrc.fit(X_train,y_train)
    y_pred = lrc.predict(X_test)
    f1 = f1_score(y_test,y_pred)
    f1_scores[c] = f1
    result = f'Fold Number: {c+1}, F1 score: {np.round(f1,4)}'
    print(result)
    c += 1
result = f'Mean F1 Score: {np.mean(f1_scores)}'
print(result)
      
## Now train the final model
print('Training final model...')
lrc = LogisticRegression(**Model_Params)
lrc.fit(Xt,y)

print('Saving final model...')
with open(Model_Filename, 'wb') as f_out: # 'wb' means write-binary
    pickle.dump((mms, pca, lrc, Model_Params), f_out)

print('Model saved.')