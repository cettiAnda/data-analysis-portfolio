# Customer Analysis

This project explores a simple customer orders dataset using Python. The objective is to understand how basic data analysis can turn raw transactional data into useful business insights, such as identifying top customers, most profitable categories, and revenue trends over time.

## Dataset

The dataset ('orders.csv') includes the following information:

- order_id - unique identifier of each order  
- customer - customer name  
- city - city where the purchase was made  
- category - product category  
- amount - purchase value (€)  
- date - order date  

## What the Analysis Covers

The script processes the dataset and extracts several key metrics:

- **Total revenue** - overall value of all purchases  
- **Revenue by customer** - how much each customer spent  
- **Revenue by category** - which product categories perform best  
- **Revenue by city** - where most revenue is generated  
- **Revenue over time** - daily trend of sales  

## Key Insights

From this analysis, it is possible to identify:

- **Top customer** - the one with the highest total spending  
- **Best category** - the most profitable category  
- **Top city** - the city generating the highest revenue  

These insights reflect common business questions and basic decision-making needs.

## How It Works

The script follows a straightforward approach:

1. Reads the CSV file using 'csv.DictReader'  
2. Iterates through each row  
3. Aggregates data using Python dictionaries  
4. Uses '.get()' to safely handle missing keys  
5. Uses 'max()' to identify top values  
6. Prints results in a clear format  

## Technologies Used

- Python  
- CSV module  
- Dictionaries for data aggregation  

## Example Output

Total revenue: €4020.00

Best customer: Alice
Best category: Electronics
Top city: Rome

Revenue by city:

Rome: €1680.00
Milan: €570.00
Naples: €820.00
Turin: €950.00

Revenue by day:

2024-01-10: €1200.00
2024-01-11: €80.00
2024-01-12: €150.00
2024-01-13: €700.00
2024-01-14: €400.00
2024-01-15: €200.00
2024-01-16: €120.00
2024-01-17: €90.00
2024-01-18: €950.00
2024-01-19: €130.00


## Purpose

This project demonstrates how to work with CSV files, perform basic data aggregation, and extract meaningful insights from raw data. It is part of a beginner data analysis portfolio built using Python.
