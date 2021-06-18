import requests

quotations = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
USD_BRL = float(quotations['USDBRL']['bid'])
EUR_BRL = float(quotations['EURBRL']['bid'])
BTC_BRL = float(quotations['BTCBRL']['bid'])

print(f"""
Current Quotations:
> USD 1 = BRL {round(USD_BRL, 2)}
> EUR 1 = BRL {round(EUR_BRL, 2)}
> BTC 1 = BRL {round(BTC_BRL, 2)}
""")