#Data Visualization III : Download the Iris flower dataset or any other dataset into a DataFrame. (e.g., https://archive.ics.uci.edu/ml/datasets/Iris ). Scan the dataset and give the inference as: 1. List down the features and their types (e.g., numeric, nominal) available in the dataset. 2.Create a histogram for each feature in the dataset to illustrate the feature distributions.3.Create a box plot for each feature in the dataset. 4.Compare distributions and identify outliers. 
#step 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#step 2
df=pd.read_csv("Iris.csv")
df

#step 3
df.info()

#step 4
# using seaborn
for i in df.columns[:-1]:
    plt.figure(figsize=(6,4))
    sns.histplot(df[i],kde=True,bins=10)

#step 5
for col in df.columns[1:-1]:
    plt.figure(figsize=(6,4))
    sns.boxplot(y=df[col])
    plt.show()

