import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class SalesPredictor:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self._preprocess()
        self._train_model()

    def _preprocess(self):
        self.df["temperature"] = pd.to_numeric(self.df["temperature"], errors='coerce')
        self.df["promotions"] = pd.to_numeric(self.df["promotions"], errors='coerce')
        self.df["sales"] = pd.to_numeric(self.df["sales"], errors='coerce')
        self.df.dropna(subset=["temperature", "promotions", "sales"], inplace=True)

    def _train_model(self):
        X = self.df[["temperature", "promotions"]]
        y = self.df["sales"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)

        self.metrics = {
            "r2": r2_score(y_test, y_pred),
            "mse": mean_squared_error(y_test, y_pred),
            "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
            "mae": mean_absolute_error(y_test, y_pred),
            "intercept": self.model.intercept_,
            "coefficients": self.model.coef_.tolist()
        }

    def predict(self, temperature, promotions):
        X_new = np.array([[temperature, promotions]])
        sales_pred = self.model.predict(X_new)
        return sales_pred[0]
