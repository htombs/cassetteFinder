import pandas as pd
import csv
import os
import requests
import json


stockData=[]

resp = requests.get("http://127.0.0.1:5000/__skus")
if resp.ok:
    data = resp.content.decode()
    stockData = json.loads(data)

csv = pd.read_csv(os.path.join(os.getcwd(),"jobs","zyro","ZyroEPOS.csv"), encoding='unicode_escape')
df = pd.DataFrame(data=csv, columns=['SKU',
                                    'StockIndicator'])
filteredCsv = df.query(f"{stockData} == SKU ")


results = []

for i in stockData: 
    sku = filteredCsv[filteredCsv['SKU'].str.contains(i)]
    result = sku.query('StockIndicator == "IS"')
    if not result.empty:
        results.append((i, 1, 8))
    else:
        results.append((i, 0, 8))
        
        
requests.post("http://127.0.0.1:5000/stock",  json = json.dumps(results))
