import pandas as pd
import csv
import os
import requests
import json

def madison():
    sku = "Product Code"
    stockStatus = "In Stock"
    indicator = "Y"
    distributorId = 6
    
    stockData=[]
    
    resp = requests.get("http://127.0.0.1:5000/__skus")
    if resp.ok:
        data = resp.content.decode()
        stockData = json.loads(data)
    
    csv = pd.read_csv(os.path.join(os.getcwd(),"jobs","madison","madison.csv"), encoding='unicode_escape')
    df = pd.DataFrame(data=csv, columns=[sku,  stockStatus])
    filteredCsv = df.query(f'{stockData} == ' + f'`{sku}`')
    
    results = []
    
    for i in stockData: 
        key = filteredCsv[f"{sku}"]
        
        partnumber = filteredCsv[key.str.contains(i)]
        result = partnumber.query(f'`{stockStatus}` == "{indicator}"')
        if not result.empty:
            results.append((i, 1, distributorId))
        else:
            results.append((i, 0, distributorId))
                
            
    requests.post("http://127.0.0.1:5000/stock",  json = json.dumps(results))
