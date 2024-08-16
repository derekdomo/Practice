import numpy as np


class LogisticRegression:
    def __init__(self, learning_rate=0.01, regularization='l2', iterations=100, lambda_reg=0.1):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.regularization = regularization
        self.lambda_reg = lambda_reg
        self.weights = None

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def cost_function(self, X, Y):
        # logloss -y * log(1-y_hat) (1-y) * log(1-y_hat)
        # num of records in the batch
        m = X.shape[0]
        predictions = self.sigmoid(np.dot(X, self.weights))
        loss = (-Y * np.log(predictions)) - (1 - Y) * np.log(1-predictions)
        return 1 / m * sum(loss)

    def gradient_decent(self, X, Y):
        m = X.shape[0]
        for _ in range(self.iterations):
            predictions = self.sigmoid(np.dot(X, self.weights))
            errors = predictions - Y
            if self.regularization == 'l1':
                gradient = np.dot(X.T, errors) / m + (self.lambda_reg/m) * np.sign(self.weights)
            else:
                gradient = np.dot(X.T, errors) / m + (self.lambda_reg/m) * self.weights
            print(self.weights)
            self.weights -= self.learning_rate * gradient
            # print("Log Loss:", self.cost_function(X, Y))

    def fit(self, X, Y):
        bias = np.ones((X.shape[0], 1))
        X_bias = np.concatenate((X, bias), axis=1)
        self.weights = np.zeros(X_bias.shape[1])
        self.gradient_decent(X_bias, Y)
    
    def predict(self, X, Y):
        bias = np.ones((X.shape[0], 1))
        X_bias = np.concatenate((X, bias), axis=1)
        predictions = self.sigmoid(np.dot(X_bias, self.weights))
        return predictions

if __name__ == "__main__":
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=100, n_features=20,  
                               n_redundant=0, n_clusters_per_class=1, random_state=1)
    model = LogisticRegression(regularization='l1')
    model.fit(X, y)      
