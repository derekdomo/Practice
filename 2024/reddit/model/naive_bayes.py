# fit
# : This method takes the training data X and corresponding labels y as input and computes the class priors, class means, and class variances for each feature.
# _predict
# : This is a helper method that predicts the label for a single test example x. It calculates the posterior probability for each class by summing the logarithm of the prior probability and the likelihood probability, and returns the class with the highest posterior probability.
# predict: This method takes a set of test examples X as input and predicts the labels for all examples using the 

# _calculate_probability
# : This is a helper method that calculates the likelihood probability for a given test example x and a specific class. It uses the Gaussian probability density function to calculate the probability based on the class mean and variance.

import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.num_classes = len(self.classes)
        self.num_features = X.shape[1]
        self.priors = np.zeros(self.num_classes)
        self.means = np.zeros((self.num_classes, self.num_features))
        self.variances = np.zeros((self.num_classes, self.num_features))

        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            self.priors[i] = X_c.shape[0] / X.shape[0]
            self.means[i] = X_c.mean(axis=0)
            self.variances[i] = X_c.var(axis=0)

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        posteriors = []

        for i, c in enumerate(self.classes):
            prior = np.log(self.priors[i])
            likelihood = np.sum(np.log(self._calculate_probability(x, i)))
            posterior = prior + likelihood
            posteriors.append(posterior)

        return self.classes[np.argmax(posteriors)]

    def _calculate_probability(self, x, class_index):
        mean = self.means[class_index]
        variance = self.variances[class_index]
        exponent = np.exp(-(x - mean) ** 2 / (2 * variance))
        return (1 / np.sqrt(2 * np.pi * variance)) * exponent
