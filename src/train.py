import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os
# Read csv-file
data = pd.read_csv(os.path.join('data', 'mpg-train.csv'), sep=";")

# print(data)

# # Shuffle data
data = data.sample(frac=1)

# # 'class'-column
y_variable = data['mpg']

# # all columns that are not the 'class'-column -> all columns that contain the attributes
x_variables = data.loc[:, data.columns != 'mpg']


x_train, x_test, y_train, y_test = train_test_split(
    x_variables, y_variable, test_size=0.2)

regressor = LinearRegression()

regressor = regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

# todo: display mean squared error

file_to_write = open(os.path.join('data', 'models', 'baummethoden_lr.pickle'), "wb")
pickle.dump(regressor, file_to_write)
