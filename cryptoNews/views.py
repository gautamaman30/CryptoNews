from django.shortcuts import render
import requests
import json


def home(request):

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,USDT,LTC,EOS,BNB,BSV,XLM&tsyms=USD")
    price = json.loads(price_request.content)
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'cryptoNews/home.html', {"api": api, "price": price})


def prices(request):
    if request.method == 'POST':
        cryptoname = request.POST['crypto']
        if cryptoname:
            cryptoname = cryptoname.upper()
            price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+cryptoname+"&tsyms=USD")
            crypto = json.loads(price_request.content)
            return render(request, 'cryptoNews/prices.html', {"cryptoname": cryptoname, "crypto": crypto})
    notfound = "Please enter any Cryptocurrency."
    return render(request, 'cryptoNews/prices.html', {"nf": notfound})
