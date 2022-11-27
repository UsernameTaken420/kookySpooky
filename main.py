import csv, random

def generateDeck():
    deck = []
    with open('Tarot.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            deck.append(row)
    random.shuffle(deck)
    for c in deck[38:]:
        c[2] = "REV"
    random.shuffle(deck)
    return deck

if __name__ == "__main__":
    deck = generateDeck()
    correctInput = False
    while correctInput == False:
        print(f"Enter amount of cards to draw: ")
        try:
            drawAmount = int(input())
            correctInput = True
        except ValueError:
            print(f"You're supposed to input a number, try again")
    print(f"Drawing {drawAmount} cards")
    for number in range(drawAmount):
        drawn = deck.pop()
        if drawn[2] == "REV":
            print(f"{drawn[1]} reversed, \"{drawn[5]}\"")
        else:
            print(f"{drawn[1]}, \"{drawn[4]}\"")
    