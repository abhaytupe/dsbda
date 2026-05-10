# step 1 : import the libraries
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

#step 2: load the dataset
df=sns.load_dataset('titanic')
df

#step 3:
df.info()

#step 4:
df.describe()

#step 5:
df.columns

# step 6:
sns.countplot(x='survived',data=df)
plt.title('servival count')
plt.show()

# step 7:
sns.countplot(x='sex',hue='survived',data=df)
plt.title("servival by gender")
plt.show()

# step 8:
sns.histplot(df['fare'],bins=30,kde=True)
plt.title("distribution of tickit Fare")
plt.xlabel("Fare")
plt.ylabel("Frequecy")
plt.show()