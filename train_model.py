import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_excel("resume_data.xlsx")

X = df["Resume"]
y = df["result"]

# Convert text to numbers
vector = TfidfVectorizer(stop_words="english")
X = vector.fit_transform(X)

# Train AI model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "resume_model.pkl")
joblib.dump(vector, "vector.pkl")

print("AI Model trained and saved successfully!")
