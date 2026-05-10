#Data Visualization II :  Use the inbuilt dataset 'titanic' as used in the above problem. Plot a box plot for distribution of age with respect to each gender along with the information about whether they survived or not. (Column names : 'gender' and 'age').Write observations on the inference from the above statistics. 
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

