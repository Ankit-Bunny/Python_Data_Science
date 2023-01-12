import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

tc = tips.corr()
print(tc)

sns.heatmap(tc, annot=True)
plt.show()

fpt = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(fpt, linecolor='white', linewidths=1)
plt.show()

sns.clustermap(fpt, standard_scale=1)
plt.show()
