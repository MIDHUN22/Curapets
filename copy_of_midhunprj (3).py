# -*- coding: utf-8 -*-
"""Copy of midhunPrj.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gKUtn0FJf7TZlBtdQvbtdg4ea5PK7CQX
"""

from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
from keras.utils import np_utils

from pandas.core.frame import DataFrame
import pandas as pd
import numpy as np

my_data = pd.read_csv('patients.csv')
my_data = DataFrame(my_data)
my_data.head()

import numpy as np
babesia_after = DataFrame(np.where(my_data['Conditions.babesia'].any()== 1 and my_data['Drugs.doxycyline']== 1 , 1, 0))

babesia_after.head()

np.shape(my_data)

#To Run Code Begins
my_data =[]
from pandas.core.frame import DataFrame
import pandas as pd
my_data = pd.read_csv('patients.csv')
my_data = DataFrame(my_data.iloc[:,[0,2]])
my_data.head()

babesia_after =[]
X = my_data
print(X)

import random
def babesia_after_med(ba, doxy):
  if(ba == 1):
    if doxy == 1:
      return random.randint(0, 9) * 0.1
    else:
      return 1
  return 0

babesia_after =[]
for i in range(len(my_data)):
  babesia_after.append(babesia_after_med(my_data.iloc[i,0], my_data.iloc[i,1]))

Y = babesia_after

my_data['babesia_after'] = Y

print(my_data)

Y = DataFrame(babesia_after)
import numpy as np
X = my_data.iloc[:,[0,1]]
np.shape(X)

from sklearn.model_selection import train_test_split
model = Sequential()
model.add(Dense(10, input_dim=2, activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.35)

model.fit(X_train, y_train,validation_data=(X_test,y_test), epochs=50, batch_size=10)

model.predict(X_test)

! pip install lime

X.columns



import lime
import lime.lime_tabular 

explainer = lime.lime_tabular.LimeTabularExplainer(np.array(X_train), feature_names=X.columns, class_names=Y.columns, discretize_continuous=True)                    # categorical_features=, 
                    # There is no categorical features in this example, otherwise specify them.

lime_test_data = DataFrame(X_test)
lime_test_data

np.array(lime_test_data)[1]

exp = explainer.explain_instance(np.array(lime_test_data)[1], model.predict, num_features=1, top_labels=1)
exp.show_in_notebook(show_table=True, show_all=True)

exp = explainer.explain_instance(np.array(lime_test_data)[0], model.predict, num_features=1, top_labels=1)
exp.show_in_notebook(show_table=True, show_all=True)

exp = explainer.explain_instance(np.array(lime_test_data)[4], model.predict, num_features=1, top_labels=1)

exp = explainer.explain_instance(np.array([1,1]), model.predict, num_features=1, top_labels=1)
exp.show_in_notebook(show_table=True, show_all=True)

exp = explainer.explain_instance(np.array([1,0]), model.predict, num_features=1, top_labels=1)
exp.show_in_notebook(show_table=True, show_all=True)