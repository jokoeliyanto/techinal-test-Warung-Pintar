/* Create Table warpin_db */

CREATE TABLE warpin_db (
id VARCHAR(255),
order_date DATE,
order_status VARCHAR(255),
customer_id VARCHAR(255),
product_sku VARCHAR(255),
product_category VARCHAR(255),
quantity INT NOT NULL,
total_price FLOAT);

/* Import Data from CSV File */
COPY PUBLIC.warpin_db FROM 'C:\Users\Joko Eliyanto\Documents\Python for Data Sains\PostgreSQL\[Technical Test - Data Engineer] Sale Report - wp.csv' DELIMITER ',' CSV HEADER;

/* [D] Specify Time Zone = Jakarta timezone, origin still on UTC */
SELECT * FROM pg_timezone_names;
SET TIMEZONE='Asia/Jakarta';

/* SQL Query */
SELECT
  date
, SUM(total_customer) as total_consumer

/* 
[B] Details of order_type :
E.g. same combinations Product Category like Minuman Sachet, Minuman Kemasan or …. 
and combination of Product Category are unacceptable, it needs to be unique
*/

, array_agg(product_sku ORDER BY product_sku) as product_sku
, array_agg(total_qty   ORDER BY product_sku) as total_qty
, SUM(total_price) as total_price
FROM ( SELECT 
	   /* [C] Count total customer, total quantity for each product SKU and aggregate total price per day */
        date(order_date)
        , count(customer_id) as total_customer
        , product_sku
        , sum(quantity) as total_qty
        , sum(total_price) as total_price
        FROM public."warpin_db"
	  /* [A] Take only order_status = “sale” */
        WHERE order_status = 'sale'
        GROUP BY date(order_date), product_sku
) T

GROUP BY date
ORDER BY date
