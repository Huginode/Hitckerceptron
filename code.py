import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# created dataset
X, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=0)

# ofc reshape y
y = y.reshape((y.shape[0], 1))

#graph plotting
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='summer')

# def init function
def init(X):
    W = np.random.randn(X.shape[1], 1)
    b = np.random.randn(1)
    return (W, b)

# def the model
def model(X, W, b):
    Z = X.dot(W) + b
    A = 1/(1 + np.exp(-Z))
    return A

# def cost function
def logLoss(A, y):
    return 1 / len(y) * np.sum(-y * np.log(A) - (1 - y) * np.log(1 - A) )


# def gradient function
def gradients (A, x, y):
     dW = 1 / len(y) * np.dot(X.T, A - y)
     db = 1 / len(y) * np.sum(A - y)
     return (dW, db)

# update function
def update(dW, db, W, b, learningRate):
    W = W - learningRate * dW
    b = b - learningRate * db
    return (W, b)

# True algorithm
def artificialNeuron(X, y, learningRate=0.1, nIter=100):
    # init W and b parameters
    W, b = init(X)
    loss = []

    for i in range(nIter):
        A = model(X, W, b)
        Loss = loss.append(logLoss(A, y))
        dW, db = gradients(A, X, y)
        W, b = update(dW, db, W, b, learningRate)

artificialNeuron(X, y)

plt.plot(Loss)
plt.show()