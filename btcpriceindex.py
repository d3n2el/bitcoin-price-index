#objective: learn how to use and get comfortable with requests
#ask with sys.argv the user for the price of n btc
#transform n to float
#make request at bitcoin price index which returns a json
#print number given by user multiplied by x
import json
import sys
import requests
def main():
        rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        price= rate.json()
        x = price["bpi"]["USD"]["rate"]
        x= x.replace(",", "")
        x= float(x)
        try:
            if len(sys.argv)== 2:
                n= sys.argv[1]
                n =float(n)
                amount= n * x
                print(f"${amount:,.4f}")
        except requests.RequestException:
            pass