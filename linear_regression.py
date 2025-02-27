from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array([[1], [3], [7], [10], [12]])
y = np.array([3, 6, 14, 20, 24])
model = LinearRegression()
model.fit(x, y)
test_data = np.array([[2], [5], [8]])
predictions = model.predict(test_data)
for i, test_point in enumerate(test_data.flatten()):
    print(f"Prediction for input {test_point}: {predictions[i]}")


