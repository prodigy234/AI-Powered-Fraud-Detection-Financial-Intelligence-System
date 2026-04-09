
# 🚨 Fraud Intelligence System

## 📌 Project Overview
The Fraud Intelligence System is an end-to-end fraud detection and compliance analytics platform designed to simulate real-world banking fraud monitoring.

The system ingests transaction-level data, enriches it with behavioral, geolocation, and device intelligence, applies machine learning models to detect fraud patterns, visualizes risk through interactive dashboards, and enables investigation workflows for compliance teams.

---

## 🎯 Key Features

### 📊 Interactive Dashboard
- Fraud rate analysis
- Transaction distribution
- Country-level fraud insights
- Amount vs fraud visualization

### 🧠 Machine Learning Engine
- Models: Random Forest & XGBoost
- Fraud prediction using:
  - Transaction amount
  - Transaction frequency
  - Transaction velocity
  - Geolocation (latitude/longitude)
- Model performance evaluation (precision, recall, F1-score)
- Feature importance visualization

### 🌍 Geo Intelligence
- Global fraud mapping using latitude & longitude
- Fraud hotspot detection by country
- Interactive Plotly map visualization

### 🧠 Behavioral Analysis
- Transaction frequency vs velocity patterns
- Detection of abnormal user behavior
- Fraud clustering insights

### 💳 Device Intelligence
- Card BIN analysis
- Device fingerprint tracking
- Identification of high-risk devices

### 📡 Real-Time Monitoring
- Simulated live transaction streaming
- Instant fraud alert triggers

### 🔍 Investigation Lab
- Transaction lookup by ID
- Full fraud investigation panel
- Risk indicator breakdown

---

## 🗂️ Dataset Description

The system uses an advanced fraud dataset (`advanced_fraud_dataset.xlsx`) with enriched features:

### Core Transaction Fields
- `transaction_id`: Unique identifier
- `customer_id`: Customer reference
- `amount`: Transaction value
- `is_fraud`: Fraud label (0 = Legit, 1 = Fraud)

### Behavioral Features
- `txn_frequency`: Number of transactions per period
- `txn_velocity`: Speed of transactions

### Geo Intelligence
- `latitude`: Transaction location latitude
- `longitude`: Transaction location longitude
- `country`: Country of transaction

### Device Intelligence
- `card_bin`: Card issuer identification
- `device_fingerprint`: Unique device identifier
- `channel`: Transaction channel (web, mobile, POS)

### Additional Context
- `merchant_category`: Type of merchant

---

## 🧠 Fraud Detection Logic

The system detects fraud using:
- Behavioral anomalies (high frequency & velocity)
- Geographic inconsistencies
- Device reuse patterns
- Transaction amount thresholds
- Machine learning predictions

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Pandas / NumPy
- Plotly
- Scikit-learn
- XGBoost

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🌐 Live Demo
https://checkfraud.streamlit.app

---

## 📌 Use Case

This project is ideal for:
- Banking compliance teams
- Fraud analysts
- AML/KYC professionals
- Data analysts building risk systems

---

## 🚀 Future Improvements
- Real-time API integration
- Deep learning fraud models
- Network graph fraud detection
- Automated case management system

---

## 👨‍💻 Author
Developed as a professional-grade fraud detection portfolio project.
