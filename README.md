![](https://github.com/jokoeliyanto/techinal-test-Warung-Pintar/blob/main/header%20warpin.png)



This is my answer for Techinal Test Data Engineer Position at Warung Pintar.
By: Joko Eliyanto, Yogyakarta, 27 June 2021

# TECHINAL TEST

## Instructions

A. There are 4 tasks in this technical test

B. We expect the below outputs:

1. SQL Files
2. Source Code
3. Python Script
4. Any notes application


# Question 1

For analysis, build a summary table to show how many customers use Warung Pintar services on a daily basis, along with the combination of products used:

![](https://github.com/jokoeliyanto/techinal-test-Warung-Pintar/blob/main/SSWP.png)

Several rules for this task:
1. Take only order_status = “sale”
2. Details of order_type 

      a. E.g. same combinations Product Category like Minuman Sachet, Minuman Kemasan or …. and combination of Product Category are unacceptable, it needs to be unique

3. Count total customer, total quantity for each product SKU and aggregate total price per day
4. Used date in Jakarta timezone, origin still on UTC

You will use PostgreSQL for this task, please follow these steps to access this link the data source, you can download as .csv: [Technical Test - Data Engineer](https://github.com/jokoeliyanto/techinal-test-Warung-Pintar/blob/main/%5BTechnical%20Test%20-%20Data%20Engineer%5D%20Sale%20Report%20-%20wp.csv) Sale Report


# Question 2
Based on your SQL Query from task Question 1, please create a job to run the SQL on daily basis with any programming language and fulfill these conditions:

1. By default, it will run a query with D-1 date as the start date and today as the end date
2. It can receive variables sent when executing the script which contains the start date and end date for backfill purposes
3. Create an Airflow DAG to run the job daily at 5 am WIB.

# Question 3
Given a CSV file (same file as Question 1) as the data source, please create a python script to reformat the data to JSON files

# Question 4
* Create an ETL Script using Python with case:
  1. Create an ETL from the CSV file (same file as Question 1) to a database (table name: “up to you”)
  2. Include all requirements or dependencies to run the script
* Please provide documentation on how to run the application


