import matplotlib.pyplot as plt
import seaborn as sns

#load the previous analysed dataset
titanic_df= sns.load_dataset('titanic')
#Display first five rows
head=titanic_df.head()
print(f'First five rows:\n {head}')

#set style fo better visuals
sns.set_style('whitegrid')

#1. Bar plot - survival rate by passanger class
plt.figure(figsize=(8,5))
sns.barplot(x='pclass', y='survived',data=titanic_df,hue='pclass', palette='coolwarm', legend=False)
plt.title('Survival Rate by Passenger class')
plt.xlabel('Passenger class')
plt.ylabel('Survival rate')
plt.show()

#histogram- age distribution
plt.figure(figsize=(8,5))
sns.histplot(titanic_df['age'].dropna(), bins=30, kde=True, color='purple')
plt.title('Age distribution of Titanic Passegeners')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='survived', labels=['No','Yes'])
plt.show()

#3.Count plot-survival by gender
plt.figure(figsize=(8,5))
sns.countplot(x='sex', hue='survived',data=titanic_df, palette='viridis')
plt.title('Survival Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived',labels=['No','Yes'])
plt.show()

