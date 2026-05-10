# Step_1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create a dataset
data={
    'student_id':[1,2,3,4,5,6,7,8,9,10],
    'math':[78, 85, np.nan, 90, 120, 65, 70, 200, 88, 76],
    'science':[80, 88, 92, np.nan, 85, 60, 75, 95, 89, 77],
    'english':[75, 82, 78, 85, 90, np.nan, 72, 88, 91, 79],
    'attendence':[85, 90, 95, 80, 105, 70, 75, 60, np.nan, 88]
}
df=pd.DataFrame(data)
df

# Step_2
df.isnull().sum()

# Step_3
df.fillna(df.mean(numeric_only=True),inplace=True)
df

# Step_4
df['math']=df['math'].clip(0,100)
df

# Step_5
df.boxplot()
plt.show()

# Step_6
newdf=df[(df['science']>65) & (df['attendence']>75)]
newdf.boxplot()
plt.show()

# Step_7
#decresing skewness
df['attendence_log']=np.log(df['attendence'])
df


