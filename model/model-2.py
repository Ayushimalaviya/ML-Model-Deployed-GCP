#!/usr/bin/env python
# coding: utf-8



import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle



data = pd.read_csv('insurance.csv',na_values='?')


data.head()



X = pd.DataFrame(data[['age','sex','bmi','children','smoker','region']])
y = data['charges']



#onehot encoding
def categoricalValueToInt(word):
    word_dict = {'female': 1, 'male': 2, 'yes':1,'no':2,'southwest':1,'southeast':2,'northwest':3,'northeast':4}
    if word in word_dict:
        return word_dict[word]
    else:
        return 0  # Handle unknown/invalid values with a default encoding

    
X['sex'] = X['sex'].apply(lambda x : categoricalValueToInt(x))
X['smoker'] = X['smoker'].apply(lambda x : categoricalValueToInt(x))
X['region'] = X['region'].apply(lambda x : categoricalValueToInt(x))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

model = LinearRegression()

#Fitting model with trainig data
model.fit(X_train, y_train)

#saving model to disk
pickle.dump(model, open('model.pickle', 'wb'))

