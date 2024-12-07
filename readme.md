# Data Seeding and Analysis Project

This project demonstrates database seeding, data manipulation, and analysis using Python. The seeding script generates dummy data for users and products in a database, while the analysis script performs data preprocessing and feature engineering.

---

## Features

- Seed the database with **500,000 users** and **500,000 products**.
- Handle random null values in the generated data.
- Perform basic data preprocessing and feature creation.
- Analyze datasets and generate enriched reports.

---

## Setup Guide

Follow these steps to set up and run the project:

### 1. clone repository

```bash
git clone https://github.com/FADHILI-Josue/Data-manipulation-demo.git
```

### 2. Create and Activate a Virtual Environment

For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

For Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Install Dependencies

Install the required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

### 3. Update Database Connection

Edit the `app/database.py` file to update the **database connection string** with your database credentials. Example:
```python
DATABASE_URL = "postgresql://username:password@localhost:5432/db_name"
```

---

### 4. Run the FastAPI Server

Start the FastAPI application:
```bash
uvicorn main:app --reload
```

This will start the API server at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### 5. Seed the Database

Run the `seed.py` script to populate the database with dummy data:
```bash
python seed.py
```

---

### 6. Run the Data Manipulation Script

Execute the `data_analysis_task.py` file to manipulate the seeded data:
```bash
python data_analysis_task.py
```

This script:
- Fetches datasets from the API.
- Handles null values and performs preprocessing.
- Adds new features to the datasets.
- Saves the processed datasets as CSV files:
  - `processed_users.csv`
  - `processed_products.csv`
  - `enriched_users.csv`

---

## Project Structure

```
project/
│
├── app/
│   ├── __init__.py
│   ├── database.py     # Database configuration
│   ├── models.py       # SQLAlchemy models for User and Product
│   └── main.py         # FastAPI application entry point
│
├── requirements.txt    # Python dependencies
├── seed.py             # Database seeding script
├── data_analysis_task.py  # Data manipulation and analysis script
├── README.md           # Project documentation
```

---

## Dependencies

- Python 3.8+
- SQLAlchemy
- FastAPI
- Faker
- Pandas
- Requests
- Uvicorn

---

## Notes

- Ensure the database is properly set up before running the seeding script.
- Replace placeholder database credentials in `app/database.py` with actual values.
- After running the scripts, inspect the generated CSV files for results.