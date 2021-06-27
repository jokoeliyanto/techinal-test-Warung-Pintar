import psycopg2

db_host = 'db'
db_name = 'warung_pintar_db'
db_user = 'username'
db_pass = 'secret'

# Connecto to the database
conn = psycopg2.connect("host={} dbname={} user={} password={}".format(db_host, db_name, db_user, db_pass))
 
#Extract
cur = conn.cursor()

#Transform

sql_query= """
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

"""
cur.execute(sql_query)
one = cur.fetchone()

print('Order Date: {}'. format(one[0]))

print('Total Customer: {}'. format(one[1]))

print('Product SKU: {} ...'. format(one[2][0:5]))

print('Total Quota: {} ...'. format(one[3][0:5]))

print('Total Price: {}'. format(one[-1]))

# Load
all = cur.fetchall()
print('Query Result1, all)
