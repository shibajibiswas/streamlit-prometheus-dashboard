import streamlit as st
import requests
import time

# Prometheus server URL
PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

# Page setup
st.set_page_config(page_title="Prometheus Metrics Dashboard", layout="wide")
st.title("📊 Real-Time Prometheus Metrics Dashboard")

# Define queries to Prometheus
queries = {
    "Request Rate (rps)": "rate(app_requests_total[1m])",
    "Error Rate (rps)": "rate(app_errors_total[1m])",
    "Avg Processing Time (s)": "rate(app_processing_seconds_sum[1m]) / rate(app_processing_seconds_count[1m])"
}

# Display each metric in columns
cols = st.columns(len(queries))

for i, (label, query) in enumerate(queries.items()):
    try:
        res = requests.get(PROMETHEUS_URL, params={"query": query})
        res.raise_for_status()
        result = res.json()

        if result["data"]["result"]:
            value = float(result["data"]["result"][0]["value"][1])
            cols[i].metric(label, f"{value:.4f}")
        else:
            cols[i].warning("No data")
    except Exception as e:
        cols[i].error(f"Error fetching {label}: {str(e)}")

st.caption("🔄 Data pulled from Prometheus in real time")
st.caption("⏱ Last updated: " + time.strftime("%Y-%m-%d %H:%M:%S"))