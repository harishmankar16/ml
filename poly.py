import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error,r2_score

data = {
"Level":[1,2,3,4,5,6,7,8,9,10],
"Salary":[4500,5000,6000,7500,8000,9500,12000,15000,16500,19000]
}

df = pd.DataFrame(data)
x=df["Level"].values.reshape(-1,1)
y=df["Salary"].values

linear_model = LinearRegression()
linear_model.fit(x,y)

poly_features = PolynomialFeatures(degree=3)
x_poly = poly_features.fit_transform(x)

poly_model = LinearRegression()
poly_model.fit(x_poly,y)

y_pred_linear = linear_model.predict(x)
y_pred_poly = poly_model.predict(x_poly)

plt.scatter(x,y,color="green")
plt.plot(x,y_pred_linear,color="blue")
plt.plot(x,y_pred_poly,color="red")
plt.xlabel("Positional Level")
plt.ylabel("Salary")
plt.title("Linear vs Polynomial")
plt.show()