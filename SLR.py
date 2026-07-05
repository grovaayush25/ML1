import random
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


class SLR:
    def __init__(self):
        self.m = None
        self.c = None

    def fit(self, x_train, y_train):
        x_train = np.asarray(x_train, dtype=float)
        y_train = np.asarray(y_train, dtype=float)

        num = 0
        den = 0
        for i in range(x_train.shape[0]):
            num = num + (x_train[i] - x_train.mean()) * (y_train[i] - y_train.mean())
            den = den + (x_train[i] - x_train.mean()) * (x_train[i] - x_train.mean())
        self.m = num / den
        self.c = y_train.mean() - self.m * x_train.mean()

    def predict(self, x_test):
        x_test = np.asarray(x_test, dtype=float)
        return self.m * x_test + self.c


x = np.array([random.uniform(1e-8, 1e8) for _ in range(1000)], dtype=float)
y = np.array([xi + np.cos(xi - 5) - np.tanh(xi**2) for xi in x], dtype=float)



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
lr = SLR()
lr.fit(x_train, y_train)
output = lr.predict(x_test)

print("Slope (m):", lr.m)
print("Intercept (c):", lr.c)
r2 = r2_score(y_test, output)
print("r2 score", r2)
print("shape of x ", x_train.shape)
print("shape of y ", y_train.shape)
plt.scatter(range(len(y_test)), y_test, color='blue', label='y_test')
plt.scatter(range(len(output)), output, color='red', label='output')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.tight_layout()
plt.show()