"""Demonstrates While loops by finding low value in str"""

cards: str = "5235"

Card_idx: int = 0
low_card: int = int(cards[0])

#look at each number in the string
while Card_idx < 4:
    #check if current card is less than low card
    current_card: int = int(cards[Card_idx])
    if (current_card < low_card):
        #update low card to be current card
        low_card = current_card
    Card_idx = Card_idx + 1
print(low_card)
