import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from matplotlib import pyplot as plt
# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df
print(df.describe())
iris.target_names
# Check for missing values
print(df.isnull().sum())
import matplotlib.pyplot as plt
import seaborn as sns

df['target'] = iris.target
sns.pairplot(df,hue='target')
plt.show()
Linear Regression
In statistics, linear regression is a linear approach to modelling the relationship between a dependent variable and one or more independent variables. Let X be the independent variable and Y be the dependent variable. We will define a linear relationship between these two variables as follows:

lin_regThis is the equation for a line that you studied in high school. m is the slope of the line and c is the y intercept.
X = df['petal length (cm)'].values
y = df['petal width (cm)'].values
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
plt.scatter(X_train, y_train)
plt.show()
# Building the model
m = 0
c = 0

L = 0.0001  # The learning Rate
epochs = 1000  # The number of iterations to perform gradient descent

n = float(len(X_train)) # Number of elements in X

# Performing Gradient Descent 
losses = []
for i in range(epochs): 
    y_pred = m*X_train + c  # The current predicted value of Y

    residuals = y_pred - y_train
    loss = np.sum(residuals ** 2)
    losses.append(loss)
    D_m = (-2/n) * sum(X_train * residuals)  # Derivative wrt m
    D_c = (-2/n) * sum(residuals)  # Derivative wrt c
    m = m + L * D_m  # Update m
    c = c + L * D_c  # Update c
    if i % 100 == 0:
        print(np.mean(y_train-y_pred))
    
# Visualize the loss
plt.plot(losses)
# Run the model on the test set
pred = []
for X in X_test:
    y_pred = m*X + c
    pred.append(y_pred)
print(pred)
print(y_test)
 
# Calculate the Mean Absolue Error
print("Mean Absolute Error:", np.mean(np.abs(y_pred - y_test)))

# Calculate the Mean Squared Error
print("Mean Squared Error:", np.mean((y_pred - y_test)**2))
# Making predictions
y_pred = m*X_test + c

plt.scatter(X_test, y_test)
plt.plot([min(X_test), max(X_test)], [min(y_pred), max(y_pred)], color='red') # predicted
plt.show()
%load_ext autoreload
%autoreload 2
from LinearRegressionSkeleton import LinearRegression

X = df['petal width (cm)'].values
y = df['sepal length (cm)'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

ln = LinearRegression()
ln.fit(X_train, y_train)
pred = ln.predict(X_test)
The autoreload extension is already loaded. To reload it, use:
  %reload_ext autoreload
5.809166666666666
3.5664605404142944
2.267586223792104
1.5119126138879924
1.0690035714555222
0.8063106764303264
0.6475858994028542
0.5489627461872929
0.4851993752529476
0.44176634574828655
