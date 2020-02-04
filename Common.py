import requests


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


cards_api_url = 'https://deckofcardsapi.com/api/deck'


def shuffledeck():
    request = requests.get(cards_api_url + '/new/shuffle/', verify=False).json()
    return request


def drawcard(deck):
    cards = requests.get(cards_api_url + '/' + deck['deck_id'] + '/draw/?count=2', verify=False).json()
    return cards