import numpy as np

class RandomForestClassifier:
    def __init__(self, n_estimators=100, max_depth=5, min_samples_split=2):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.trees = []

    def fit(self, X, y):
        num_samples, num_features = X.shape

        for _ in range(self.n_estimators):
            indices = np.random.choice(num_samples, size=num_samples, replace=True)
            bootstrap_X = X[indices]
            bootstrap_y = y[indices]

            tree = DecisionTreeClassifier(max_depth=self.max_depth, min_samples_split=self.min_samples_split)
            tree.build_tree(bootstrap_X, bootstrap_y)
            self.trees.append(tree)

    def predict(self, X):
        y_pred = np.zeros(len(X))

        for tree in self.trees:
            y_pred += tree.predict(X)

        y_pred = np.where(y_pred >= (len(self.trees) / 2), 1, 0)
        return y_pred