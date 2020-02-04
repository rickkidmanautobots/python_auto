import requests
from Common import shuffledeck
from Common import drawcard


cards_api_url = 'https://deckofcardsapi.com/api/deck'


def test_create_new_shuffled_deck():
    response = shuffledeck()
    deckID = response['deck_id']
    print("")
    print("DECK ID RETURNED: " + deckID)
    assert response['remaining'] == 52
    assert response['shuffled']
    assert response['deck_id'] != 'null'
    assert response['success']
    return deckID


def test_draw_two_cards():
    deckID = shuffledeck()
    response = drawcard(deckID)
    assert response['success']
    assert len(response['cards']) == 2
    assert response['remaining'] == 50
