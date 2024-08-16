import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=1000, regularization="l2", lambda_reg=0.1):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.regularization = regularization
        self.lambda_reg = lambda_reg
        self.weights = None

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _cost_function(self, X, y):
        m = X.shape[0]
        predictions = self._sigmoid(np.dot(X, self.weights))
        # Log Loss
        error = (-y * np.log(predictions)) - ((1 - y) * np.log(1 - predictions))
        cost = (1 / m) * sum(error)

        if self.regularization == "l2":
            cost += (self.lambda_reg / (2 * m)) * (np.sum(self.weights ** 2))
        elif self.regularization == "l1":
            cost += (self.lambda_reg / m) * (np.sum(np.abs(self.weights)))

        return cost

    def _gradient_descent(self, X, y):
        m = X.shape[0]
        self.cost_history = []

        for i in range(self.iterations):
            predictions = self._sigmoid(np.dot(X, self.weights))
            errors = predictions - y

            if self.regularization == "l2":
                gradient = np.dot(X.T, errors) / m + (self.lambda_reg/m) * self.weights
            elif self.regularization == "l1":
                gradient = np.dot(X.T, errors) / m + (self.lambda_reg/m) * np.sign(self.weights)

            self.weights -= self.learning_rate * gradient
            self.cost_history.append(self._cost_function(X, y))

    def fit(self, X, y):
        bias = np.ones((X.shape[0], 1))
        X_bias = np.concatenate((bias, X), axis=1)
        self.weights = np.zeros(X_bias.shape[1])
        self._gradient_descent(X_bias, y)

    def predict(self, X):
        bias = np.ones((X.shape[0], 1))
        X_bias = np.concatenate((bias, X), axis=1)
        predictions = self._sigmoid(np.dot(X_bias, self.weights))
        return [1 if x >= 0.5 else 0 for x in predictions]

if __name__ == "__main__":
    # Example usage with synthetic data
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, n_clusters_per_class=1, random_state=1)

    model = LogisticRegression(learning_rate=0.01, iterations=1000, regularization="l2", lambda_reg=0.1)
    model.fit(X, y)
    predictions = model.predict(X)

    print("Predictions snippet:", predictions[:10])
    # You can plot model.cost_history to evaluate the optimization process
