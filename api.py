import json
import os
from datetime import datetime
from utils import encrypt_data, save_patient_data, load_patient_data

DATA_PATH = "data/patients.json"

def upload_record(file, patient_id):
    records = load_patient_data()
    metadata = {
        "Type": file.type,
        "Date": str(datetime.now().date()),
        "Summary": "Uploaded file",
        "Access Granted To": []
    }
    encrypted_data = encrypt_data(metadata)
    records.setdefault(patient_id, {}).setdefault("Records", []).append(encrypted_data)
    save_patient_data(records)

def schedule_appointment(patient_id, doctor_name):
    records = load_patient_data()
    appointment = {
        "Doctor": doctor_name,
        "Date": str(datetime.now().date()),
        "Status": "Confirmed"
    }
    records.setdefault(patient_id, {}).setdefault("Appointments", []).append(appointment)
    save_patient_data(records)

def get_patient_records(patient_id):
    records = load_patient_data()
    return records.get(patient_id, {})
