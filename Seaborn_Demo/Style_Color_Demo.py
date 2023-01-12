import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# plt.figure(figsize=(12, 3))
# sns.set_style('ticks')
# sns.set_context('poster')
# sns.countplot(x='sex', data=tips)
# sns.despine()
# palette='seismic'
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm')
plt.show()
