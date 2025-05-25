# Patient-Health-Records-Management-and-Consultation-Booking-Application_Devops_Assignment
It is a internship assignment
health_records_app/
├── app.py
├── api.py
├── utils.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
├── data/
│   ├── patients.json
│   └── appointments.json
├── uploads/
│   └── [record files]
# 🏥 Patient Health Records Management & Consultation Booking App

A secure, role-based healthcare web application where patients can upload medical records, doctors can view trends and schedule appointments, and admins can manage access — all with encryption and privacy in mind.

---

## 🚀 Features

### 👤 Patient
- Upload and manage health records (PDFs, images, text).
- Approve/revoke doctor access.
- View scheduled appointments.

### 👨‍⚕️ Doctor
- Search/filter patients by ID, condition, or date.
- Analyze health trends (e.g., blood pressure over time).
- Book appointments with patients.

### 🛡️ Security
- Role-based access (Patient, Doctor, Admin).
- AES encryption for sensitive data.
- Patient-controlled access (HIPAA/GDPR-style).
- Access logs maintained.

---

## 🧩 Tech Stack

- **Frontend:** Streamlit (Gradio optional)
- **Backend:** Python
- **Security:** Cryptography (Fernet AES)
- **Storage:** JSON files (can be extended to SQLite/Firestore)
- **Deployment:** Hugging Face Spaces / Vercel (FastAPI required)

---

## ⚙️ Setup Instructions

### 📁 Clone the Repo

```bash
git clone https://github.com/your-username/health-records-app.git
cd health-records-app
# Patient Health Records & Booking App

## 🚀 Features
- Secure record uploads by patients.
- Doctors can access records and book appointments.
- Role-based dashboards.
- Data encryption & HIPAA-style access control.

## 🛠 Setup
```bash
pip install -r requirements.txt
streamlit run app.py

