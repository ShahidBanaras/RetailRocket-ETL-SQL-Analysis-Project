
# 🛒 RetailRocket ETL & SQL Analysis Project

A complete end-to-end data engineering project demonstrating how to build an ETL pipeline using Python and SQL to analyze real-world e-commerce data from the [RetailRocket dataset](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset). The processed data is stored in a PostgreSQL database and queried using SQL for business insights.

---

## 📂 Project Structure

```
retailrocket-etl-project/
├── etl.py               # ETL pipeline script (Extract, Transform, Load)
├── analysis.sql         # SQL queries for data exploration and reporting
├── datasets/            # (Optional) Directory for local CSV data
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧰 Tech Stack

- **Python** – `pandas`, `SQLAlchemy`, `psycopg2`
- **PostgreSQL** – Relational database for storing processed data
- **SQL** – For data analysis and business intelligence
- **RetailRocket Dataset** – Real user interaction data from an e-commerce platform

---

## 📦 Dataset Overview

The dataset includes:
- `events.csv` – User interactions such as views, add-to-cart actions, and transactions
- `item_properties.csv` – Metadata about products
- `category_tree.csv` – Hierarchical product categories

This allows exploration of user behavior, conversion funnels, and product performance.

---

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/retailrocket-etl-project.git
cd retailrocket-etl-project
```

### 2. Set Up PostgreSQL
- Install PostgreSQL locally or use a cloud provider.
- Create a new database (e.g., `retailrocket`).
- Update your database credentials in `etl.py`.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the ETL Script
```bash
python etl.py
```
This will:
- Load and clean raw CSVs
- Transform data into structured tables
- Load it into your PostgreSQL database

---

## 📊 SQL Analysis

All queries are stored in `analysis.sql`. Sample insights include:

- **Top 10 Most Viewed Products**
- **Conversion Rates (View → Purchase)**
- **Hourly Event Distribution**
- **Most Recent or Most Active Users**

Example query:
```sql
SELECT item_id, COUNT(*) AS view_count
FROM events
WHERE event = 'view'
GROUP BY item_id
ORDER BY view_count DESC
LIMIT 10;
```

---

## ✅ Use Cases

This project can be extended to:
- Build a product recommendation system
- Create dashboards using **Tableau**, **Power BI**, or **Streamlit**
- Automate the pipeline using **Apache Airflow**

---

## 🧾 Requirements

```text
pandas
sqlalchemy
psycopg2
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🧠 Future Enhancements

- Streamlit-based interactive dashboard
- Dockerize the pipeline for portability
- Add unit testing for ETL components

---

## 🙏 Acknowledgments

- [RetailRocket Dataset on Kaggle](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)

---

## 👨‍💻 Author

**Shahid**  
🎓 Computer Engineering Student | 📊 Aspiring Data Engineer  
🔗 [GitHub](https://github.com/ShahidBanaras)

Feel free to fork, contribute, or reach out!

