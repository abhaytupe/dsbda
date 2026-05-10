#Data Analytics I  :Create a Linear Regression Model using Python to predict home prices using Boston Housing Dataset .
# Step_1
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step_2
df=pd.read_csv("train.csv")
df

# Step_3
df.columns

# Step_4
x=df[['ID', 'crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad',
       'tax', 'ptratio', 'black', 'lstat']]
y=df['medv']

x

# Step_5
y

# Step_6
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)

# Step_7
model=LinearRegression()
model.fit(x_train,y_train)

# Step_8
y_pred=model.predict(x_test)
y_pred

# Step_9
model.score(x_train,y_train)

# Step_10
model.score(x_test,y_test)

# Step_11
np.sqrt(mean_squared_error(y_test,y_pred))
