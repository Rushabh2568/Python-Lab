# -*- coding: utf-8 -*-
"""cost prediction of medical insurance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VGQNB1_226g1SDE5piaVwBABEz0_aHn7
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

insurance_dataset = pd.read_csv('/content/insurance.csv')

insurance_dataset.head()

insurance_dataset.shape

insurance_dataset.info()

insurance_dataset.isnull().sum()

insurance_dataset.describe()

sns.set()
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['Age'])
plt.title('Age Distribution')
plt.show()

# Gender column
plt.figure(figsize=(6,6))
sns.countplot(x='Sex', data=insurance_dataset)
plt.title('Sex Distribution')
plt.show()

insurance_dataset['Sex'].value_counts()

plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['BMI'])
plt.title('BMI Distribution')
plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x='Children', data=insurance_dataset)
plt.title('Children')
plt.show()

insurance_dataset['Children'].value_counts()

plt.figure(figsize=(6,6))
sns.countplot(x='Smoker', data=insurance_dataset)
plt.title('smoker')
plt.show()

insurance_dataset['Smoker'].value_counts()

plt.figure(figsize=(6,6))
sns.countplot(x='Region', data=insurance_dataset)
plt.title('region')
plt.show()

insurance_dataset['Region'].value_counts()

plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['Charges'])
plt.title('Charges Distribution')
plt.show()

# encoding sex column
insurance_dataset.replace({'Sex':{'male':0,'female':1}}, inplace=True)

3 # encoding 'smoker' column
insurance_dataset.replace({'Smoker':{'yes':0,'no':1}}, inplace=True)

# encoding 'region' column
insurance_dataset.replace({'Region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

X = insurance_dataset.drop(columns='Charges', axis=1)
Y = insurance_dataset['Charges']
print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print(X.shape, X_train.shape, X_test.shape)

regressor = LinearRegression()

regressor.fit(X_train, Y_train)

training_data_prediction =regressor.predict(X_train)
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R squared vale : ', r2_train)

test_data_prediction =regressor.predict(X_test)
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print('R squared vale : ', r2_test)

input_data = (31,1,25.74,0,1,0)

# changing input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = regressor.predict(input_data_reshaped)
print(prediction)

print('The insurance cost is USD ', prediction[0])