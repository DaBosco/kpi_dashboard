# KPI Dashboard

## 📌 Project Overview

This project automates the extraction of key performance indicators (KPIs) from a MariaDB database and saves them to a CSV file. The system is built using Python and MariaDB, with automation handled through cron jobs.  The KPIs can then be visualized using other tools if desired.

## 🛠️ Technologies Used

- **Python** (for data extraction and processing)
- **MariaDB** (database for storing sales data)
- **Linux Cron Jobs** (for scheduled automation)

## 🚀 Features

- Connects to a MariaDB database.
- Calculates KPIs (total sales, total orders, best-selling product).
- Saves KPIs to a CSV file (`kpi_report.csv`).
- Runs automatically at scheduled intervals using cron jobs.

## 📂 Project Structure
kpi_dashboard/
├── scripts/
│   └── extract_kpi.py     # Python script to extract KPIs
├── data/
│   └── kpi_report.csv    # Generated KPI report
├── logs/
│   └── cron.log          # Log file for cron job execution
└── myenv/                # Python virtual environment

## 🛠️ Setup Instructions

1️⃣ Install Dependencies
- Ensure you have Python and MariaDB installed. Then, install the required Python packages:

pip install -r requirements.txt

2️⃣ Configure Database Connection
- Edit scripts/extract_kpi.py with your MariaDB credentials:

conn = pymysql.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="kpi_db"
)

3️⃣ Set Up Cron Job (Automation)
- Open the cron job editor:

crontab -e

- Add the following line to schedule the KPI extraction every hour:

0 * * * * /path/to/your/project/scripts/extract_kpi.py >> /path/to/your/project/logs/cron.log 2>&1

4️⃣ Run Manually (For Testing)
- You can manually generate the KPI report:

python3 scripts/extract_kpi.py

💡 Visualizing the Data
- The generated kpi_report.csv file can be used with various tools for visualization, such as:

Python Libraries: Matplotlib, Seaborn, Plotly
Spreadsheet Software: Microsoft Excel, Google Sheets, LibreOffice Calc
Data Visualization Tools: Google Data Studio (Looker Studio), Tableau Public, etc.

## 📜 License
- This project is licensed under the MIT License.
