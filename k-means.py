import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('income.csv')

print("Dataset head:")
print(data.head())


X = data[['Income', 'Age']]

inertia = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(k_range, inertia, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()


optimal_k = 3

kmeans = KMeans(n_clusters=optimal_k, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)


plt.figure(figsize=(10, 8))
sns.scatterplot(x='Income', y='Age', hue='Cluster', data=data, palette='viridis', s=100, marker='o')
plt.title('Clusters of Customers (Income vs Age)')
plt.xlabel('Income')
plt.ylabel('Age')
plt.legend(title='Cluster')
plt.show()


print("Cluster Centers:")
print(kmeans.cluster_centers_)

print("\nData with Cluster Labels:")
print(data.head())
