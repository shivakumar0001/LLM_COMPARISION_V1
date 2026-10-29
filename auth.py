import streamlit as st
import pandas as pd
import os
import hashlib
USER_FILE = "data/users.csv"
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
def init_user_store():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(USER_FILE):
        df = pd.DataFrame(columns=["username","password"])
        df.to_csv(USER_FILE, index=False)
def load_users():
    init_user_store()
    return pd.read_csv(USER_FILE)
def save_user(username, password):
    users = load_users()
    hashed = hash_password(password)
    users.loc[len(users)] = [username, hashed]
    users.to_csv(USER_FILE, index=False)

