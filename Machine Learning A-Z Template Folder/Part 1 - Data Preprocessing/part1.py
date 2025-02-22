# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("hello world")
# Data Preprocessing

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#save file then f5


#Importing the dataset

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values
           
np.set_printoptions(threshold = np.nan) 
   
#taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#encoding categorical variables

from sklearn.preprocessing import LabelEncoder
labelencoder_X =  LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
# this isn't quite right as it's categorical data with multiple values
# that is not ordinal

# let's try to create different columns instead
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X =  LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
# it's ok for y as it's binary
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#Splitting the dataset into training set and test set
# deprecated
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""
