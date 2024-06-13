# CS50P - Problem set 4 - 2022 course
# Tarn Montgomery 2024/06/10
# returns the exchange of USD to Bitcoin

import sys
import requests

#Calculates and prints the value for n number of bitcoins at the current USD rate
def main():
    n = valid_input()
    bitcoin = get_bitcoin()
    value = float(n*bitcoin)
    print('${:,.4f}'.format(value),end="")

# Validates the correct number of arguments
def valid_input():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            return n
        except ValueError:
            sys.exit("Command-line argument is not a number")
        except TypeError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument  ")
        
# loads and returns the Bitcoin rate as a float for USD
def get_bitcoin():
    try:
        r = requests.get(' https://api.coindesk.com/v1/bpi/currentprice.json')
        rjson = r.json()
        coin_price = rjson['bpi']['USD']['rate_float']
        return coin_price
    except requests.RequestException:
        sys.exit("Request unavailable")
    

if __name__ == "__main__":
    main()
    