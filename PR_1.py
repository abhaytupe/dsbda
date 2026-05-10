#Data Wrangling, I Using any open source dataset (e.g., data.csv).import all python libraries.load the dataset into pandas data frame.Perform Data Preprocessing ,Data Formatting and Data Normalization and turn categorical variables into quantitative variables in Python.
# Step_1
import pandas as pd

# Step_2
df=pd.read_csv("archive.zip")
df

# # Step_3
df.isnull()

# Step_4
df.isnull().sum()

# Step_5
df.describe()

# Step_6
df.size

# Step_7
df.ndim

# Step_8
df.shape

# Step_9
df.info

# Step_10
df["study_hours_per_week"]=df["study_hours_per_week"].astype(int)
df

# Step_11
df["attendance_rate"]=df["attendance_rate"].astype(int)
df

# Step_12
df["gender"]=df["gender"].replace({"Female":0,"Male":1})
df
