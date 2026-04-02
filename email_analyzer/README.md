# Email Analyzer

This project analyzes a raw email log file to extract simple but meaningful insights about email activity.
The goal is to show how unstructured text data can be processed using basic Python, without relying on external libraries.

---

## Dataset

The dataset is a text file ('mbox.txt') containing email log data.
Each relevant line follows this format:

From user@example.com Sat Jan 5 09:14:16 2008

From these lines, the program extracts:
- the sender's email address  
- the time the email was sent  

The file is stored inside the 'data/' folder.

---

## What This Project Does

The script reads the file line by line and focuses only on lines starting with "From ".
From there, it builds two analyses:

### 1. Emails by Sender
Counts how many emails each user has sent and identifies the most active sender.

### 2. Emails by Hour
Extracts the hour from each email and counts how many emails were sent at each time of day.

---

## Example Output

| Email             | Emails Sent |
|-------------------|-------------|
| cwen@iupui.edu    | 5           |
| ...               | ...         |
The user who sent the most emails is: cwen@iupui.edu

| Hour    | Emails Sent |
|---------|-------------|
| 09      | 5           |
| ...     | ...         |

The hour with the highest number of emails is: 09

---

## How It Works

The script:
- reads the file using 'open()' 
- filters relevant lines with 'startswith("From ")'  
- uses 'split()' to extract data  
- stores results in dictionaries  
- sorts results to identify top values  

The implementation is intentionally simple and focuses on clarity and core Python concepts.

---

## Technologies Used

- Python (base)
- File handling
- Dictionaries
- String processing

---

## Purpose

This project is part of a beginner data analysis portfolio.

It demonstrates how to:
- work with unstructured data  
- extract useful information from text  
- perform basic aggregation and analysis  

---

## How to Run

Make sure the dataset is inside the 'data/' folder, then run:

'''bash
python main.py
