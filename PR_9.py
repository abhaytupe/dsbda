# Step_1
import seaborn as sns
import matplotlib.pyplot as plt

# Step_2
df=sns.load_dataset('titanic')
df

# Step_3
sns.boxplot(x='sex',y='age',hue='survived',data=df)
plt.title('Age Distribution by Gender and Survival Status')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()

