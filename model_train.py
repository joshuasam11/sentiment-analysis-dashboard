# model_train.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from preprocess import clean_text

# Load your dataset
df = pd.read_excel("chatgpt_style_reviews_dataset.xlsx")

# Adjust column names as per your dataset
# (assume 'review' and 'sentiment' are the columns)
df.columns = [col.lower() for col in df.columns]
text_col = 'review' if 'review' in df.columns else df.columns[0]
label_col = 'Sentiment' if 'Sentiment' in df.columns else df.columns[1]

# Clean text
df[text_col] = df[text_col].apply(clean_text)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df[text_col], df[label_col], test_size=0.2, random_state=42)

# TF-IDF
vectorizer = TfidfVectorizer(max_features=3000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# Save model + vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model and vectorizer saved successfully!")