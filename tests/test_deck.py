from .. import main
import pytest

# Arrange   
@pytest.fixture
def deck():
    return main.generateDeck()

def test_deck(deck):
    assert type(deck) == list

def test_draw(deck):
    card = main.drawCard(deck)
    assert (type(card) == tuple) and (type(card[0]) == str) and (type(card[1]) == str)

def test_overdraw(deck):
    with pytest.raises(IndexError):
        main.drawCard([])
