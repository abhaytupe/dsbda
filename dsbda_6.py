#step 1: import the libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score

#step 2: load the csv file
df=pd.read_csv("Iris.csv")
df

#step 3: Separate input features and target variable
# x -> Independent variables (features)
# y -> Dependent variable (target/output class)
x=df[['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y=df['Species']
x

#step 4: split the dataset into training and testing sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=30)

#step 5: create the model 
model=GaussianNB()
model.fit(x_train,y_train)

#step 6: predict the output
y_pred=model.predict(x_test)
y_pred

#step 7: calculate the score
model.score(x_train,y_train)

#step 8: find out the score of original dataset
model.score(x,y)

# step 9: find out the confusion matrix
cm=confusion_matrix(y_test,y_pred)
cm

#step 10: find out the values of fn tn fp tp
total = np.sum(cm)

for i in range(len(cm)):
    TP = cm[i, i]
    FP = np.sum(cm[:, i]) - TP
    FN = np.sum(cm[i, :]) - TP
    TN = total - (TP + FP + FN)
    
    print(f"\nClass {i}: TP={TP}, FP={FP}, FN={FN}, TN={TN}")

#step 11:find out the accuracy
a=accuracy_score(y_test,y_pred)
a

# step 12: error rate
e=1-a
e