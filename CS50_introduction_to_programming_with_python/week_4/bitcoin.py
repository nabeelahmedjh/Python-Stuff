import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage Error: program accept only 1 command line aurgument")
        sys.exit()

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        print("Command-line aurgument is not a number")
        sys.exit()

    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json")

    except requests.RequestException:
        sys.exit()

    bitcoin_info = response.json()

    btc_rate = float(bitcoin_info["bpi"]["USD"]["rate"].replace(",", ""))
    print(f"${btc_rate * float(sys.argv[1]):,.4f}")


main()
