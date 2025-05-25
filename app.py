import streamlit as st
from utils import encrypt_data, decrypt_data, load_patient_data, save_patient_data
from api import upload_record, schedule_appointment, get_patient_records

st.set_page_config(page_title="Health Records App", layout="wide")

role = st.sidebar.selectbox("Login as", ["Patient", "Doctor", "Admin"])

if role == "Patient":
    st.title("Patient Dashboard")

    patient_id = st.text_input("Patient ID")
    uploaded_file = st.file_uploader("Upload Health Record (PDF, JPG, PNG, TXT)", type=["pdf", "jpg", "png", "txt"])

    if uploaded_file and st.button("Upload Record"):
        upload_record(uploaded_file, patient_id)
        st.success("Record uploaded successfully!")

    if st.button("View My Records"):
        records = get_patient_records(patient_id)
        st.json(records)

elif role == "Doctor":
    st.title("Doctor Dashboard")

    patient_id = st.text_input("Search Patient ID")
    if st.button("View Patient Records"):
        records = get_patient_records(patient_id)
        st.json(records)

    if st.button("Schedule Appointment"):
        schedule_appointment(patient_id, "Dr. Smith")
        st.success("Appointment scheduled!")

else:
    st.title("Admin Panel")
    st.info("Coming soon.")
