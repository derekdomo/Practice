import numpy as np

class DecisionTreeClassifier:
    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = {}

    def gini(self, y):
        classes, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        gini = 1 - np.sum(probabilities**2)
        return gini

    def _entropy(self, y):
        classes = np.unique(y)
        entropy = 0.0
        for cls in classes:
            p_cls = np.sum(y == cls) / len(y)
            if p_cls > 0:
                entropy -= p_cls * np.log2(p_cls)
        return entropy

    # can also use mse instead of gini
    # def mse(self, y):
    #     return np.mean((y - np.mean(y))**2)

    def split(self, X, y, feature_index, threshold):
        left_mask = X[:, feature_index] <= threshold
        right_mask = X[:, feature_index] > threshold
        X_left, y_left = X[left_mask], y[left_mask]
        X_right, y_right = X[right_mask], y[right_mask]
        return X_left, X_right, y_left, y_right

    def evaluate_split(self, X, y, feature_index, threshold):
        X_left, X_right, y_left, y_right = self.split(X, y, feature_index, threshold)
        gini_left = self.gini(y_left)
        gini_right = self.gini(y_right)
        weighted_gini = (len(y_left) * gini_left + len(y_right) * gini_right) / len(y)
        return weighted_gini

    def find_best_split(self, X, y):
        best_gini = np.inf
        best_feature_index = None
        best_threshold = None

        for feature_index in range(X.shape[1]):
            thresholds = np.unique(X[:, feature_index])
            for threshold in thresholds:
                gini = self.evaluate_split(X, y, feature_index, threshold)
                if gini < best_gini:
                    best_gini = gini
                    best_feature_index = feature_index
                    best_threshold = threshold

        return best_feature_index, best_threshold

    def build_tree(self, X, y, depth=0):
        if depth == self.max_depth or len(y) < self.min_samples_split:
            unique_classes, counts = np.unique(y, return_counts=True)
            majority_class = unique_classes[np.argmax(counts)]
            return majority_class

        feature_index, threshold = self.find_best_split(X, y)
        if feature_index is None or threshold is None:
            unique_classes, counts = np.unique(y, return_counts=True)
            majority_class = unique_classes[np.argmax(counts)]
            return majority_class

        X_left, X_right, y_left, y_right = self.split(X, y, feature_index, threshold)
        self.tree = {
            'feature_index': feature_index,
            'threshold': threshold,
            'left': self.build_tree(X_left, y_left, depth + 1),
            'right': self.build_tree(X_right, y_right, depth + 1)
        }

    def predict_sample(self, x, tree):
        if isinstance(tree, int):
            return tree
        if x[tree['feature_index']] <= tree['threshold']:
            return self.predict_sample(x, tree['left'])
        else:
            return self.predict_sample(x, tree['right'])

    def predict(self, X):
        y_pred = [self.predict_sample(x, self.tree) for x in X]
        return np.array(y_pred)
