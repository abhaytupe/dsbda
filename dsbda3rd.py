#step 1
import pandas as pd
import zipfile

with zipfile.ZipFile("iris.zip") as z:
    df = pd.read_csv(z.open("iris.data"), header=None)

df
#step 2
df.columns
#step 3
df[4]
#step 4
df[4].value_counts()
#step 5
df.describe()
#step 6
df[4].describe()
#step 7
df[3].describe()
#step 8
df.groupby(4).describe()
#step 9
df.groupby(4).describe().sum()

