import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('position_sal.csv')

X = data[['Level']].values  
y = data['Salary'].values 

scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).flatten()

svm_regressor = SVR(kernel='linear') 
svm_regressor.fit(X_scaled, y_scaled)

y_pred_scaled = svm_regressor.predict(X_scaled)
y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1))

plt.scatter(X, y, color='blue', label='Actual Data')   # Scatter plot of original data
plt.plot(X, y_pred, color='red', label='Linear SVM Regression')  # Line plot of SVM predictions
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.title("Linear SVM Regression")
plt.legend()
plt.show()
