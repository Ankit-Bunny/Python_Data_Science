import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())
sns.distplot(tips['total_bill'], kde=False, bins=30)
plt.show()

# kind='hex' or kind='reg' or kind='kde'
sns.jointplot(x='total_bill', y='tip', data=tips)
plt.show()

sns.pairplot(tips, hue='sex')
plt.show()

sns.rugplot(tips['total_bill'])
plt.show()

sns.kdeplot(tips['total_bill'])
plt.show()
