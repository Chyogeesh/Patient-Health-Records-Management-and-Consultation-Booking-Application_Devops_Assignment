import json
from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
fernet = Fernet(KEY)

def encrypt_data(data):
    return fernet.encrypt(json.dumps(data).encode()).decode()

def decrypt_data(data):
    return json.loads(fernet.decrypt(data.encode()).decode())

def load_patient_data():
    try:
        with open("data/patients.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_patient_data(data):
    with open("data/patients.json", "w") as f:
        json.dump(data, f, indent=2)
