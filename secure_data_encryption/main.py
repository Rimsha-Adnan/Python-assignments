import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import json
import os
import time

# File to store encrypted data
DATA_FILE = "secure_data.json"
LOCKOUT_TIME = 60  # Lockout time in seconds

# Generate or load encryption key
KEY_FILE = "secret.key"
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as file:
        KEY = file.read()
else:
    KEY = Fernet.generate_key()
    with open(KEY_FILE, "wb") as file:
        file.write(KEY)

cipher = Fernet(KEY)

# Load data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_data = json.load(f)
else:
    stored_data = {}

# Global variables
failed_attempts = 0
last_failed_time = 0

# Utility functions
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(stored_data, f)

def hash_passkey(passkey):
    return hashlib.pbkdf2_hmac("sha256", passkey.encode(), b"somesalt", 100000).hex()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

# Streamlit UI
st.title("🔒 Secure Data Encryption System")
menu = ["Home", "Register", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("Use this app to **securely store and retrieve data** using passkeys.")

elif choice == "Register":
    st.subheader("👤 Register User")
    username = st.text_input("Username")
    passkey = st.text_input("Passkey", type="password")

    if st.button("Register"):
        if username and passkey:
            hashed_passkey = hash_passkey(passkey)
            stored_data[username] = {"passkey": hashed_passkey, "data": []}
            save_data()
            st.success("✅ User registered successfully!")
        else:
            st.error("⚠️ All fields are required!")

elif choice == "Store Data":
    st.subheader("📂 Store Data")
    username = st.text_input("Username")
    passkey = st.text_input("Passkey", type="password")
    user_data = st.text_area("Enter Data")

    if st.button("Encrypt & Save"):
        if username in stored_data and user_data and passkey:
            hashed = hash_passkey(passkey)
            if stored_data[username]["passkey"] == hashed:
                encrypted = encrypt_data(user_data)
                stored_data[username]["data"].append(encrypted)
                save_data()
                st.success("✅ Data encrypted and stored!")
            else:
                st.error("❌ Incorrect passkey!")
        else:
            st.error("⚠️ All fields are required or user not found!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Data")
    username = st.text_input("Username")
    passkey = st.text_input("Passkey", type="password")

    # global failed_attempts, last_failed_time

    if failed_attempts >= 3:
        elapsed = time.time() - last_failed_time
        if elapsed < LOCKOUT_TIME:
            st.warning(f"⏳ Too many attempts. Try again in {int(LOCKOUT_TIME - elapsed)} seconds.")
            st.stop()
        else:
            failed_attempts = 0

    if st.button("Retrieve"):
        if username in stored_data and passkey:
            hashed = hash_passkey(passkey)
            if stored_data[username]["passkey"] == hashed:
                failed_attempts = 0
                st.success("✅ Decryption Successful!")
                for d in stored_data[username]["data"]:
                    st.write(decrypt_data(d))
            else:
                failed_attempts += 1
                last_failed_time = time.time()
                st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - failed_attempts}")
        else:
            st.error("⚠️ Username or passkey missing, or user not found!")

elif choice == "Login":
    st.subheader("🔑 Admin Login")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        # global failed_attempts
        if login_pass == "admin123":
            failed_attempts = 0
            st.success("✅ Access granted.")
        else:
            st.error("❌ Incorrect password!")
