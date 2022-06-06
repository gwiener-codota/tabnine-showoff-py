from sklearn.datasets import load_iris

# load the iris dataset
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)

# show a scatter-plot of the data with label as color
import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap="viridis", alpha=0.8)
plt.show()

# train-test split
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest classifier on the data
from sklearn.ensemble import RandomForestClassifier
regressor = RandomForestClassifier(n_estimators=100, max_depth=10)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
