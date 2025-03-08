import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load Data
df = pd.read_csv("data/fitness_data.csv")

# Select Features & Target
X = df[["steps", "calories", "water_intake", "workouts"]]
y = df["calories"]  # Example target

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
with open("models/ml_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully in models/ml_model.pkl")
