import streamlit as st
import pickle

# Başlık
st.title("🧠 Encrypted Text Classifier (20 Newsgroups)")

# Modeli yükle
with open("cipher_classifier.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

# Girdi alanı
text = st.text_area("🔐 Enter encrypted (ciphertext) input:", height=200)

if st.button("🧪 Predict"):
    if text.strip() == "":
        st.warning("Lütfen şifreli bir metin girin.")
    else:
        X_input = vectorizer.transform([text])
        prediction = model.predict(X_input)[0]
        st.success(f"📂 Predicted category: **{prediction}**")
