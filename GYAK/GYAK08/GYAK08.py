%load_ext autoreload
%autoreload 2
from LinearRegressionSkeleton import LinearRegression

ln = LinearRegression()

X = df['petal width (cm)'].values
Y = df['sepal length (cm)'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Fitting the function
ln.fit(X_train,y_train)

#Predictions
print(y_test)
ln.predict(X_test)
