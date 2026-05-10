# step1:import the files
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score

# step 2: read the dataset
df = pd.read_csv("Social_Network_Ads[1].csv")
df

# step 3: change the gender to numeric datatype
df["Gender"]=df["Gender"].map({"Male":1,"Female":0})
df

# step 4: create x and y variables for test and train a model
x = df[["User ID","Gender","Age","EstimatedSalary"]]
y = df["Purchased"]
x

# step 5: split the dataset into testing and training variables 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=29)

# step 6: create a model
model = LogisticRegression()
model.fit(x_train,y_train)

# step 7: find out the predicted values
y_pred = model.predict(x_test)
y_pred

# step 8 : Find out the all values asked in the question
model.score(x_train,y_train)
model.score(x,y)

cm = confusion_matrix(y_test,y_pred)
cm

a = accuracy_score(y_test,y_pred)
a

e = 1-a
e

p = precision_score(y_test,y_pred)
p

r = recall_score(y_test, y_pred)
r