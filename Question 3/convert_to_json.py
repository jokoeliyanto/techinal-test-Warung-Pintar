import pandas as pd
import json

df = pd.read_csv('https://raw.githubusercontent.com/jokoeliyanto/techinal-test-Warung-Pintar/main/%5BTechnical%20Test%20-%20Data%20Engineer%5D%20Sale%20Report%20-%20wp.csv')

result = df.to_json(orient="columns")

with open('warpin_db.json', 'w') as json_file:
    json.dump(result, json_file)
