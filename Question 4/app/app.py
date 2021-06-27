import psycopg2

db_host = 'db'
db_name = 'warung_pintar_db'
db_user = 'username'
db_pass = 'secret'

# Connecto to the database
conn = psycopg2.connect("host={} dbname={} user={} password={}".format(db_host, db_name, db_user, db_pass))
                        
cur = conn.cursor()
cur.execute(sql_query)
one = cur.fetchone()
#all = cur.fetchall()

print('Order Date: {}'. format(one[0]))

print('Total Customer: {}'. format(one[1]))

print('Product SKU: {} ...'. format(one[2][0:5]))

print('Total Quota: {} ...'. format(one[3][0:5]))

print('Total Price: {}'. format(one[-1]))
