import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

st.set_page_config(layout="wide")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    file = "advanced_fraud_dataset.xlsx"
    df = pd.read_excel(file, sheet_name="transactions")
    return df

df = load_data()

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🚨 Fraud Intelligence System")
menu = st.sidebar.radio("Navigation", [
    "Dashboard",
    "ML Engine",
    "Geo Intelligence",
    "Behavior Analysis",
    "Device Intelligence",
    "Real-Time Monitoring",
    "Investigation Lab"
])

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":
    st.title("📊 Fraud Intelligence Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Transactions", len(df))
    col2.metric("Fraud Cases", df["is_fraud"].sum())
    col3.metric("Fraud Rate %", round(df["is_fraud"].mean()*100, 2))
    col4.metric("Avg Amount", round(df["amount"].mean(), 2))

    st.markdown("---")

    # Fraud distribution
    fig1 = px.histogram(df, x="is_fraud", title="Fraud Distribution")
    st.plotly_chart(fig1, use_container_width=True)

    # Amount vs Fraud
    fig2 = px.box(df, x="is_fraud", y="amount", title="Amount vs Fraud")
    st.plotly_chart(fig2, use_container_width=True)

    # Country fraud
    fig3 = px.bar(df.groupby("country")["is_fraud"].sum().reset_index(),
                  x="country", y="is_fraud", title="Fraud by Country")
    st.plotly_chart(fig3, use_container_width=True)

# =========================
# ML ENGINE
# =========================
elif menu == "ML Engine":
    st.title("🧠 Machine Learning Fraud Detection")

    features = [
        "amount",
        "txn_frequency",
        "txn_velocity",
        "latitude",
        "longitude"
    ]

    X = df[features]
    y = df["is_fraud"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model_type = st.selectbox("Choose Model", ["RandomForest", "XGBoost"])

    if st.button("Train Model"):

        if model_type == "RandomForest":
            model = RandomForestClassifier()
        else:
            model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        st.success("Model Trained Successfully")

        st.text("Model Performance:")
        st.text(classification_report(y_test, preds))

        # Feature importance
        importance = pd.DataFrame({
            "feature": features,
            "importance": model.feature_importances_
        }).sort_values(by="importance", ascending=False)

        fig = px.bar(importance, x="feature", y="importance",
                     title="Feature Importance")
        st.plotly_chart(fig)

# =========================
# GEO INTELLIGENCE (FIXED & UPGRADED)
# =========================
elif menu == "Geo Intelligence":
    st.title("🌍 Geo Fraud Mapping")

    # -------------------------
    # CLEAN DATA (CRITICAL FIX)
    # -------------------------
    geo_df = df.copy()

    # Remove missing coordinates
    geo_df = geo_df.dropna(subset=["latitude", "longitude"])

    # Keep only valid geo ranges
    geo_df = geo_df[
        (geo_df["latitude"].between(-90, 90)) &
        (geo_df["longitude"].between(-180, 180))
    ]

    # Debug info (helps you understand what's happening)
    st.write(f"Total Valid Geo Records: {len(geo_df)}")

    if geo_df.empty:
        st.error("⚠️ No valid geo data available for mapping")
    else:
        # -------------------------
        # POWER BI–LEVEL MAP
        # -------------------------
        fig = px.scatter_mapbox(
            geo_df,
            lat="latitude",
            lon="longitude",
            color="is_fraud",
            size="amount",
            hover_name="merchant_category",
            hover_data={
                "customer_id": True,
                "country": True,
                "channel": True,
                "txn_frequency": True,
                "txn_velocity": True,
                "amount": True
            },
            zoom=2,
            height=600
        )

        fig.update_layout(
            mapbox_style="carto-positron",
            title="🌍 Global Fraud Risk Distribution",
            margin={"r":0,"t":40,"l":0,"b":0}
        )

        st.plotly_chart(fig, use_container_width=True)

        # -------------------------
        # BONUS: FRAUD HOTSPOTS
        # -------------------------
        st.subheader("🔥 Fraud Hotspot Analysis")

        hotspot = geo_df.groupby("country")["is_fraud"].sum().reset_index()

        fig2 = px.bar(
            hotspot.sort_values(by="is_fraud", ascending=False).head(10),
            x="country",
            y="is_fraud",
            title="Top Fraud Countries"
        )

        st.plotly_chart(fig2, use_container_width=True)

# =========================
# BEHAVIOR ANALYSIS
# =========================
elif menu == "Behavior Analysis":
    st.title("🧠 Behavioral Fraud Detection")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.scatter(df,
                         x="txn_frequency",
                         y="txn_velocity",
                         color="is_fraud",
                         title="Behavior Pattern")
        st.plotly_chart(fig)

    with col2:
        fig = px.box(df,
                     x="is_fraud",
                     y="txn_frequency",
                     title="Transaction Frequency Risk")
        st.plotly_chart(fig)

# =========================
# DEVICE INTELLIGENCE
# =========================
elif menu == "Device Intelligence":
    st.title("💳 Device & Card Intelligence")

    fig = px.histogram(df,
                       x="card_bin",
                       color="is_fraud",
                       title="Fraud by Card BIN")
    st.plotly_chart(fig)

    device_counts = df.groupby("device_fingerprint")["is_fraud"].sum().reset_index()

    fig2 = px.bar(device_counts.sort_values(by="is_fraud", ascending=False).head(20),
                  x="device_fingerprint",
                  y="is_fraud",
                  title="Top Fraud Devices")
    st.plotly_chart(fig2)

# =========================
# REAL-TIME MONITORING
# =========================
elif menu == "Real-Time Monitoring":
    st.title("📡 Live Transaction Stream")

    placeholder = st.empty()

    for i in range(50):
        sample = df.sample(5)

        placeholder.dataframe(sample)

        if sample["is_fraud"].sum() > 0:
            st.error("🚨 Fraud Detected in Stream!")

        time.sleep(1)

# =========================
# INVESTIGATION LAB
# =========================
elif menu == "Investigation Lab":
    st.title("🔍 Fraud Investigation Lab")

    txn_id = st.text_input("Enter Transaction ID")

    if st.button("Investigate"):

        result = df[df["transaction_id"] == txn_id]

        if result.empty:
            st.error("Transaction Not Found")
        else:
            row = result.iloc[0]

            st.success("Transaction Found")

            st.write("### Details")
            st.write(row)

            if row["is_fraud"] == 1:
                st.error("🚨 FRAUD ALERT")
            else:
                st.success("🟢 Legitimate")

            st.write("### Risk Indicators")
            st.write(f"Frequency: {row['txn_frequency']}")
            st.write(f"Velocity: {row['txn_velocity']}")
            st.write(f"Device: {row['device_fingerprint']}")