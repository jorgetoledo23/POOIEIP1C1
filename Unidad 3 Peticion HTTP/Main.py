#pip install requests
#pip3 install requests

import requests
import time
import os

while True:

    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(request.status_code)
    if(request.status_code == 200):
        datos = request.json()
        bpi = datos['bpi']
        usd = bpi['USD']
        valorUSD = usd['rate']
        eur = bpi['EUR']
        valorEUR = eur['rate']
        
        os.system("cls")
        print(f"El valor del Bitcoin en USD es : $${valorUSD}")
        print(f"El valor del Bitcoin en EUR es : $${valorEUR}")
        time.sleep(5)