import random
from drawcard import *

def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"}
    deck = []
    # Write your nested for-loop creating 52 cards in deck.
    for s in suits:
        for r in ranks:
            deck.append((s, r))
    random.shuffle(deck)
   
    # shuffle deak using random.shuffle function
    return deck

def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])

def count_score(cards):
    score = 0
    number_of_aces = 0
    
    for card in cards:
        rank = card[1]
        if rank == 'A':
            score += 11
            number_of_aces += 1
        elif rank in {'J', 'Q', 'K'}:
            score += 10
        else:
            score += rank
            
    while score > 21 and number_of_aces > 0:
        score -= 10
        number_of_aces -= 1
        
    return score

def show_cards_motion(cards, message, sec):
    print(message)
    draw_cards_motion(cards,sec)
    for card in cards:
        if card[0] != '?':
            print((card[0]+' '+str(card[1])).center(13),end='')
        else:
            print("**** **".center(13),end='')
    print('')    

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'

def show_cards(cards, message):
    print(message)
    draw_cards(cards)
    for card in cards:
        if card[0] != '?':
            print((card[0]+' '+str(card[1])).center(13),end='')
        else:
            print("**** **".center(13),end='')
    print('')
    
