import json
import boto3
import requests


def lambda_handler(event, context):
    # TODO implement
    # api-endpoint
    URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
 
    # extracting data in json format
    data = r.json()
    print(data)
    price=data['bpi']['USD']['rate_float']
    time_data=data['time']['updated']
    
 
    output="Price of bitcoin is "+str(price)+"USD at datetime "+time_data

    print(output)
    return output
    