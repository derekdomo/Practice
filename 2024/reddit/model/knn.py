class KNN:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X_test):
        predictions = [self._predict(x) for x n X_test]
        return np.array(predictions)
    
    def _predict(self, x):
        neighbors = self._get_neighbors(x)
        most_common = np.bincount(neighbors).argmax()
        return most_common
    
    def _get_neighbors(self, x):
        distances = [self._eucliean_distance(x, x_t) for x_t in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        return self.y_train[k_indices]

    def _euclidean_distnance(self, a, b):
        return np.sqrt(np.sum((a-b) ** 2))

    def score(self, X_test, y_test):
        predictions = self.predict(X_test)
        accuracy = np.mean(predictions == y_test)
        return accuracy
    

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
