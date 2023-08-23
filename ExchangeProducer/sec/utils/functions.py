from dotenv import load_dotenv
import os
import requests
import json
from confluent_kafka import Producer


def exchange_rate_api(token):
    load_dotenv('.env')
    api_endpoint = "http://apilayer.net/api/live?access_key=" + token + "&currencies=JPY,EUR,RMB,CAD&source=USD&format=1"
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        print ("Success connect with API! Here's the data")
        data = response.json()
        print (data)
    elif response.status_code == 404:
        print ("Unable to reach URL")
    else:
        print ("unable to connect API or retrieve data")
    

def load_producer(kafka_server):
    return Producer(bootstrap_servers=kafka_server)

