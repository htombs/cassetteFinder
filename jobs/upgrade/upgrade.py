import pandas as pd
import csv
import os
import requests
import json

sku = "Stock Code"
stockIndicator = "Due In Date"
indicator = "In Stock"
distributorId = 7

stockData=[]

resp = requests.get("http://127.0.0.1:5000/__skus")
if resp.ok:
    data = resp.content.decode()
    stockData = json.loads(data)

csv = pd.read_csv(os.path.join(os.getcwd(),"jobs","upgrade","upgrade.csv"), encoding='unicode_escape')
df = pd.DataFrame(data=csv, columns=[sku,  stockIndicator])
filteredCsv = df.query(f'{stockData} == ' + f'`{sku}`')

results = []

for i in stockData: 
    key = filteredCsv[f"{sku}"]
    
    partnumber = filteredCsv[key.str.contains(i)]
    result = partnumber.query(f'`{stockIndicator}` == "{indicator}"')
    if not result.empty:
        results.append((i, 1, distributorId))
    else:
        results.append((i, 0, distributorId))
            
        
requests.post("http://127.0.0.1:5000/stock",  json = json.dumps(results))
