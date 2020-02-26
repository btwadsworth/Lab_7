import requests

def main():
    usd = get_amount()
    print('Amount in USD: $%d' % usd)


def get_rate():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url).json()
    return response


def get_amount():
    # provide bitcoin
    bitcoin = 100
    response = get_rate()
    rate_float = response['bpi']['USD']['rate_float']
    amount_in_usd = bitcoin * rate_float
    return amount_in_usd


if __name__ == "__main__":
    main()