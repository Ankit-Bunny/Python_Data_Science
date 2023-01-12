import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')

sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
plt.show()

sns.countplot(x='sex', data=tips)
plt.show()

sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()

sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips)
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
plt.show()

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex')
plt.show()

sns.swarmplot(x='day', y='total_bill', data=tips)
plt.show()

# sns.factorplot(x='day', y='total_bill', data=tips, kind="bar")
plt.show()
