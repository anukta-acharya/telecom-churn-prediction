import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# load dataset
df = pd.read_csv("Telcom_Customer_Churn.csv")
df["TotalCharges"] = df["TotalCharges"].replace(" ", np.nan)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)
df = df.dropna()

# features and target
X = df[['tenure','MonthlyCharges','TotalCharges']]
y = df['Churn']

# split dataset
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=51)

# train model
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

# save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully!")