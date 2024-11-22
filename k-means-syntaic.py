import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

n_samples = 300
n_features = 2
n_clusters = 3
random_state = 42

X, y_true = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, cluster_std=1.2, random_state=random_state)

plt.scatter(X[:, 0], X[:, 1], c='gray', s=30, label='Data points')
plt.title("Synthetic Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30, label='Clustered data points')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("K-means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

print("Cluster Centers:\n", centroids)
