# 🔐 Encrypted Text Classifier – 20 Newsgroups Cipher Challenge

This project is built for the [Kaggle Ciphertext Challenge](https://www.kaggle.com/competitions/20-newsgroups-ciphertext-challenge), where the goal is to classify encrypted text documents into 20 different newsgroup categories.

🎯 Even without decrypting the text, we trained a character-level machine learning model that achieves over **63% accuracy**.

---

## 📂 Project Structure
cipher-classifier/
├── app.py # Streamlit app
├── cipher_classifier.pkl # Pickled model + vectorizer
├── train.csv # Kaggle training data
├── requirements.txt # Libraries for deployment
└── README.md


---

## 🧠 Model Overview

- **Input:** Ciphertext strings (unreadable encrypted text)
- **Vectorization:** `CountVectorizer` with char-level n-grams (1 to 3)
- **Model:** Logistic Regression (sklearn)
- **Accuracy:** ~63% (without decryption)

---


Example Output
Input (Ciphertext)	Predicted Label
['W')(7x1zay7Hb3...	15
Tx4a8M\HNsyp;HM...	8



📦 Deployment
This app is designed to run on:

🟢 Hugging Face Spaces

🟢 Streamlit Cloud

🔵 GitHub


📌 Kaggle Link
You can download the dataset from the official competition:
👉 Kaggle – 20 Newsgroups Ciphertext Challenge

