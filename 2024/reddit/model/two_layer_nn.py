# https://www.kaggle.com/code/ihalil95/building-two-layer-neural-networks-from-scratch

import numpy as np

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

def setParameters(X, Y, hidden_size):
  np.random.seed(3)
  input_size = X.shape[0] # number of neurons in input layer
  output_size = Y.shape[0] # number of neurons in output layer.
  W1 = np.random.randn(hidden_size, input_size)*np.sqrt(2/input_size)
  b1 = np.zeros((hidden_size, 1))
  W2 = np.random.randn(output_size, hidden_size)*np.sqrt(2/hidden_size)
  b2 = np.zeros((output_size, 1))
  return {'W1': W1, 'W2': W2, 'b1': b1, 'b2': b2}

def forwardPropagation(X, params):
  Z1 = np.dot(params['W1'], X)+params['b1']
  A1 = np.tanh(Z1)
  Z2 = np.dot(params['W2'], A1)+params['b2']
  y = sigmoid(Z2)  
  return y, {'Z1': Z1, 'Z2': Z2, 'A1': A1, 'y': y}

# another option to implement forward
# def softmax(self, x):
#     exp_vals = np.exp(x - np.max(x, axis=1, keepdims=True))
#     return exp_vals / np.sum(exp_vals, axis=1, keepdims=True)

# def forward(self, X):
#     self.z1 = np.dot(X, self.W1) + self.b1
#     self.a1 = self.sigmoid(self.z1)
#     self.z2 = np.dot(self.a1, self.W2) + self.b2
#     self.a2 = self.softmax(self.z2)
#     return self.a2

def cost(predict, actual):
  m = actual.shape[1]
  cost__ = -np.sum(np.multiply(np.log(predict), actual) + np.multiply((1 - actual), np.log(1 - predict)))/m
  return np.squeeze(cost__)

def backPropagation(X, Y, params, cache):
  m = X.shape[1]
  dy = cache['y'] - Y
  dW2 = (1 / m) * np.dot(dy, np.transpose(cache['A1']))
  db2 = (1 / m) * np.sum(dy, axis=1, keepdims=True)
  dZ1 = np.dot(np.transpose(params['W2']), dy) * (1-np.power(cache['A1'], 2))
  dW1 = (1 / m) * np.dot(dZ1, np.transpose(X))
  db1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)
  return {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}

def updateParameters(gradients, params, learning_rate = 1.2):
    W1 = params['W1'] - learning_rate * gradients['dW1']
    b1 = params['b1'] - learning_rate * gradients['db1']
    W2 = params['W2'] - learning_rate * gradients['dW2']
    b2 = params['b2'] - learning_rate * gradients['db2']
    return {'W1': W1, 'W2': W2, 'b1': b1, 'b2': b2}
 
 def fit(X, Y, learning_rate, hidden_size, number_of_iterations = 5000):
  params = setParameters(X, Y, hidden_size)
  cost_ = []
  for j in range(number_of_iterations):
    y, cache = forwardPropagation(X, params)
    costit = cost(y, Y)
    gradients = backPropagation(X, Y, params, cache)
    params = updateParameters(gradients, params, learning_rate)
    cost_.append(costit)
  return params, cost_

# Testing the code
import sklearn.datasets
X, Y = sklearn.datasets.make_moons(n_samples=500, noise=.2)
X, Y = X.T, Y.reshape(1, Y.shape[0])
params, cost_ = fit(X, Y, 0.3, 5, 5000)
import matplotlib.pyplot as plt
plt.plot(cost_)

# 随机生成训练样本x, y
N, D_in, H, D_out = 64, 1000, 100, 10
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

# 随机初始化参数w1, w2
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)