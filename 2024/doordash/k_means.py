import numpy as np
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k=3, max_iters=300, tol=1e-4):
        self.k = k
        self.max_iters = max_iters
        self.tol = tol
        self.centroids = None
        self.inertia = None

    def fit(self, X):
        self.X = X
        self.centroids = self._initialize_centroids(X)
        for i in range(self.max_iters):
            self.labels = self._assign_clusters(self.centroids)
            new_centroids = self._update_centroids()
            diff = np.linalg.norm(new_centroids - self.centroids)
            if diff < self.tol:
                print(f'Converged in {i} iterations')
                break
            self.centroids = new_centroids
        self.inertia = self._compute_inertia()

    def predict(self, X):
        labels = self._assign_clusters(self.centroids, X)
        return labels

    def _initialize_centroids(self, X):
        indices = np.random.choice(X.shape[0], self.k, replace=False)
        centroids = X[indices]
        return centroids

    def _assign_clusters(self, centroids, X=None):
        if X is None:
            X = self.X
        distances = np.zeros((X.shape[0], self.k))
        for i, centroid in enumerate(centroids):
            distances[:, i] = np.linalg.norm(X - centroid, axis=1)
        return np.argmin(distances, axis=1)

    def _update_centroids(self):
        centroids = np.zeros((self.k, self.X.shape[1]))
        for i in range(self.k):
            cluster_points = self.X[self.labels == i]
            if len(cluster_points) > 0:
                centroids[i] = cluster_points.mean(axis=0)
        return centroids

    def _compute_inertia(self):
        inertia = 0
        for i in range(self.k):
            cluster_points = self.X[self.labels == i]
            inertia += np.sum((cluster_points - self.centroids[i]) ** 2)
        return inertia
