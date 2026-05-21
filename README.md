# 📊 Sales Analytics Pipeline Dashboard

A **production-style Sales Analytics System** built using **Python, SQLite, Pandas, Streamlit, and Plotly** to automate data ingestion, transformation, analysis, and visualization.

This project simulates a real-world **data analytics workflow** — from raw sales data processing to an interactive business intelligence dashboard.

---

## 🚀 Project Highlights

✅ End-to-End **ETL Pipeline**  
✅ Automated **Data Cleaning & Transformation**  
✅ **SQLite Database Integration**  
✅ Business KPI & Revenue Analysis  
✅ Interactive **Streamlit Dashboard**  
✅ Dynamic Product Filters  
✅ Interactive **Plotly Visualizations**  
✅ Logging & Modular Project Architecture  
✅ Production-Ready Folder Structure

---

## 🏗️ System Architecture

```text
Raw TXT Data
      ↓
   Extraction
      ↓
Data Cleaning & Transformation
      ↓
   SQLite Database
      ↓
 Business Analytics
      ↓
 CSV / JSON Outputs
      ↓
 Streamlit Dashboard
```

---

## 📌 Key Features

### 🔹 ETL Pipeline
- Reads raw sales data from `.txt` file
- Handles missing values & duplicates
- Converts incorrect datatypes
- Generates derived metrics like `total_sales`

### 🔹 Business Analytics
Provides insights such as:

- 💰 Total Revenue
- 🏆 Top Selling Products
- 👤 Customer Spending Analysis
- 📈 Revenue Trends Over Time

### 🔹 Interactive Dashboard
- KPI Cards
- Revenue Trend Analysis
- Product-wise Sales Visualization
- Customer Sales Insights
- Sidebar Product Filters
- Interactive Plotly Charts

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Pandas | Data Processing |
| SQLite | Database |
| Streamlit | Dashboard UI |
| Plotly | Interactive Charts |
| JSON / CSV | Output Reports |

---

## 📂 Project Structure

```text
sales_project/
│
├── app/
│   └── app.py
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── analytics/
│   └── analysis.py
│
├── db/
│   └── database.py
│
├── config/
│   └── config.py
│
├── utils/
│   └── logger.py
│
├── data/
│   └── sales.txt
│
├── output/
├── logs/
├── database/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd sales_project
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run ETL Pipeline

```bash
python main.py
```

### 4️⃣ Launch Dashboard

```bash
streamlit run app/app.py
```

---

## 📊 Dashboard Preview

_Add screenshots here after deployment_

### Example:
- KPI Overview
- Revenue Trends
- Product Sales Analysis
- Customer Insights

---

## 📈 Sample Business Insights

✔ Identify top-performing products  
✔ Monitor revenue trends over time  
✔ Analyze customer purchase behavior  
✔ Generate analytics-ready datasets

---

## 🌟 Future Improvements

- [ ] Date Range Filters  
- [ ] Customer-Level Filtering  
- [ ] PostgreSQL Integration  
- [ ] Cloud Deployment  
- [ ] Real-Time Data Refresh  
- [ ] Authentication System

---

## 👨‍💻 Author

**Biswarup Majumdar**  
B.Tech in Information Technology | Data Science & Software Development Enthusiast

---

### ⭐ If you found this project useful, consider giving it a star!