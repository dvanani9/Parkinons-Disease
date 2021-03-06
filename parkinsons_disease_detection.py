# -*- coding: utf-8 -*-
"""Parkinsons Disease Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PVRn73m4_4DQ20y3_nkPxzXeBe0BwWtH
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis"""

#loading the data from csv file to a pandas dataframe
  parkinsons_data = pd.read_csv('/content/parkinsons.csv')

#printing the first five rows of the dataframe
parkinsons_data.head()

#number of rows and cols in the dataframe
parkinsons_data.shape

#getting more information abour dataset
parkinsons_data.info()

#checking for missing values in column 1
parkinsons_data.isnull().sum()

#getting some statistical measures about the data
parkinsons_data.describe()

#distribution of target variable(status)
parkinsons_data['status'].value_counts()

"""1->parkinsons positive
0->Healthy
"""

#goruping the data based on target variable
parkinsons_data.groupby('status').mean()

"""Data pre processing

Seperating thr features and target
"""

X = parkinsons_data.drop(columns=['name', 'status'], axis =1)
Y = parkinsons_data['status']

print(X)

print(Y)

"""Splitting the data to training data to test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

print(X_train)

"""Model Training

Support Vector Machine
"""

model = svm.SVC(kernel ='linear')

#training the SVM model with training data
model.fit(X_train, Y_train)

"""Model Evaulation

Accuracy Score
"""

#accuracy score on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy Score of Training Data:', training_data_accuracy)

#accuracy score on testing data
X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy Score of Testing Data:', testing_data_accuracy)

"""Building the Predictive System"""

input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

# changing input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the data
std_data = scaler.transform(input_data_reshaped)

prediction = model.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print("The person doesnot have parkinsons")
else:
  print("Person has parkinsons")

