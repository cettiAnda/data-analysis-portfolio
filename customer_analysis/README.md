# Customer Analysis

This project performs a basic data analysis on customer orders using Python.

The goal is to extract meaningful insights from a CSV dataset by aggregating and analyzing purchase data.

---

## Dataset

The dataset ('orders.csv') contains the following fields:

- 'order_id' = unique identifier of the order  
- 'customer' = customer name  
- 'city' = city where the purchase was made  
- 'category' = product category  
- 'amount' = purchase value (€)  
- 'date' = date of the order  

---

## Analysis Performed

The script reads the dataset and computes:

### 1. Total Revenue
- Sum of all purchase amounts

### 2. Revenue by Customer
- Total spending for each customer

### 3. Revenue by Category
- Total revenue for each product category

### 4. Revenue by City
- Total revenue generated in each city

### 5. Revenue by Date
- Daily revenue aggregation

---

## Key Insights

The program identifies:

- **Best customer** = highest total spending  
- **Top category** = most profitable category  
- **Top city** = city with highest revenue  

---

## How It Works

The script:

1. Reads the CSV file using 'csv.DictReader'
2. Iterates through each row
3. Aggregates data using Python dictionaries
4. Uses '.get()' to handle missing keys safely
5. Computes maximum values using 'max()'
6. Prints results in a formatted way

---

## Technologies Used

- Python (base)
- CSV module
- Dictionaries for data aggregation

---



## Example Output
Total revenue: €4020.00
Best customer: Alice
Best category: Electronics
Top city: Rome

Revenue by city:
- Rome: €1680.00
- Milan: €570.00
- Naples: €820.00
- Turin: €950.00

Revenue by day:
- 2024-01-10: €1200.00
- 2024-01-11: €80.00
- 2024-01-12: €150.00
- 2024-01-13: €700.00
- 2024-01-14: €400.00
- 2024-01-15: €200.00
- 2024-01-16: €120.00
- 2024-01-17: €90.00
- 2024-01-18: €950.00
- 2024-01-19: €130.00

---



## Purpose

This project demonstrates:

- Data processing from CSV files  
- Basic data aggregation techniques  
- Extraction of business insights from raw data  

It is part of a beginner data analysis portfolio developed using Python.
