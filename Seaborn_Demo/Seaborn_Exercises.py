import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.jointplot(x='fare', y='age', data=titanic)
plt.show()

sns.displot(titanic['fare'])
plt.show()

sns.boxplot(x='class', y='age', data=titanic)
plt.show()

sns.swarmplot(x='class', y='age', data=titanic)
plt.show()

sns.countplot(x='sex', data=titanic)
plt.show()

sns.heatmap(titanic.corr(), cmap='coolwarm')
plt.title('titanic.corr()')
plt.show()

g = sns.FacetGrid(data=titanic, col='sex')
g.map(sns.displot, 'age')
plt.show()
