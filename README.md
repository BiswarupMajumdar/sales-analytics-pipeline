
# 📊 Sales Analytics Pipeline & Dashboard

A production-style **ETL pipeline + interactive dashboard** built using Python, Streamlit, SQLite, and Plotly.
This project demonstrates end-to-end data engineering workflow: from raw data ingestion to business insights visualization.

---

## 🚀 Live Demo
https://sales-analytics-pipeline-complete.streamlit.app/

---

## 📌 Project Overview

This project simulates a real-world **sales analytics system**:

* Extracts raw sales data from a `.txt` file
* Cleans and transforms data using Python (Pandas)
* Loads data into SQLite database
* Generates business reports (CSV + JSON)
* Displays insights using an interactive Streamlit dashboard

---

## ⚙️ Tech Stack

* 🐍 Python
* 📊 Pandas
* 🗄 SQLite3
* 📈 Plotly
* 🌐 Streamlit
* 📂 OS / Pathlib

---

## 📁 Project Structure

```
sales-analytics-pipeline/
│
├── app/                  # Streamlit dashboard
├── etl/                  # Extract, Transform, Load scripts
├── analytics/           # Business logic & reporting
├── db/                   # Database connection
├── config/              # Configuration settings
├── utils/               # Logging utilities
├── data/                # Raw input data (sales.txt)
├── output/              # Generated reports (CSV, JSON)
├── main.py              # ETL pipeline entry point
├── requirements.txt
└── README.md
```

---

## 🔄 ETL Pipeline Flow

1. **Extract**

   * Reads raw sales data from `sales.txt`

2. **Transform**

   * Cleans missing values
   * Removes duplicates
   * Creates calculated fields (e.g., total sales)

3. **Load**

   * Stores processed data into SQLite database

4. **Analytics**

   * Generates:

     * Revenue by date
     * Revenue by product
     * Customer analysis report

---

## 📊 Dashboard Features

* 📈 Revenue trend over time
* 🏆 Top performing products
* 👤 Customer purchase analysis
* 📌 KPI metrics (Revenue, Products, Customers)
* 🎯 Interactive filters (products, date range)
* 📥 Downloadable reports (CSV export)
* 🔄 Refresh pipeline button (run ETL from UI)

---

## 🧠 Key Learnings

This project demonstrates:

* ETL pipeline design (real-world data engineering flow)
* Modular Python project structure
* SQL database integration with Python
* Data visualization using Plotly
* Interactive dashboard development using Streamlit
* Handling deployment issues in cloud environments

---

## ▶️ How to Run Locally

```bash
# Clone repository
git clone https://github.com/your-username/sales-analytics-pipeline.git

# Move into directory
cd sales-analytics-pipeline

# Install dependencies
pip install -r requirements.txt

# Run ETL pipeline (optional)
python main.py

# Launch Streamlit app
streamlit run app/app.py
```

---

## ☁️ Deployment

This project is deployed on **Streamlit Cloud**.

To deploy:

1. Push code to GitHub
2. Connect repo to Streamlit Cloud
3. Set main file:

   ```
   app/app.py
   ```

---

## 📌 Future Improvements

* Move from CSV → fully database-driven dashboard
* Add authentication system
* Dockerize application
* Deploy backend using FastAPI
* Add real-time data ingestion

---

## 👨‍💻 Author

**Biswarup Majumdar**

* Data Science | Python | SQL | Power BI
* Passionate about building real-world data engineering systems

---