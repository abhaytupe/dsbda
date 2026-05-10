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

