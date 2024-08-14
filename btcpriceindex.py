#objective: learn how to use and get comfortable with requests
#ask with sys.argv the user for the price of n btc
#transform n to float
#make request at bitcoin price index which returns a json
import sys
import requests
def main():
    try:
        price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        price = price.json
        n = sys.argv[1]

    except requests.RequestException:
        pass

def btc_usd(n):
    



main()