# 📊 Streamlit Prometheus Dashboard

A lightweight, Python-based dashboard to visualize **real-time Prometheus metrics** using **Streamlit** — ideal for monitoring 24×7 public-facing systems and API backends.

---

## 🚀 Features

- 🔌 Connects directly to your local Prometheus instance
- 📈 Displays live metrics such as:
  - **Request Rate (rps)**
  - **Error Rate (rps)**
  - **Average Processing Time**
- ⚙️ Fully built using Python and Streamlit
- 🧪 Easy to extend with more metrics or visualizations (charts, alerts)

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Prometheus](https://prometheus.io/)
- [Prometheus Python Client](https://github.com/prometheus/client_python)
- Python `requests` for fetching metrics

---

## 📁 Project Structure

```
streamlit_prometheus_dashboard/
├── dashboard.py           # Main Streamlit app
└── requirements.txt       # Python dependencies
```

---

## 🧰 Prerequisites

- Python 3.7+
- Prometheus server running on `localhost:9090`
- Your FastAPI (or backend) app must expose Prometheus metrics at `/metrics`

---

## ⚙️ Installation & Usage

1. **Clone this repository**

```bash
git clone https://github.com/yourusername/streamlit-prometheus-dashboard.git
cd streamlit-prometheus-dashboard
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Start the Streamlit app**:

```bash
streamlit run dashboard.py
```

4. Open in browser:

```
http://localhost:8501
```

---

## 📡 Prometheus Queries Used

| Metric                        | Description                        |
|------------------------------|------------------------------------|
| `rate(app_requests_total[1m])` | Request rate (RPS)                |
| `rate(app_errors_total[1m])`   | Error rate (RPS)                  |
| `rate(app_processing_seconds_sum[1m]) / rate(app_processing_seconds_count[1m])` | Average processing time (s) |

---

## 📌 Customizing

- Add more metrics to `queries` in `dashboard.py`
- Integrate line charts using `st.line_chart` or `Plotly`
- Use Prometheus `query_range` for historical visualizations

---



## 🙌 Author

**Shibaji Biswas**  
[LinkedIn](https://linkedin.com/in/shibajibiswas) | [Medium](https://medium.com/@shibajibiswas)
