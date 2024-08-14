#objective: learn how to use and get comfortable with requests
#ask with sys.argv the user for the price of n btc
#transform n to float
#make request at bitcoin price index which returns a json
import json
import sys
import requests
def main():
        try:
            rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            price= rate.json()
            for usd in price["bpi"]["USD"]["rate"]:
                print(usd["rate_float"])
        except requests.RequestException:
            pass


main()