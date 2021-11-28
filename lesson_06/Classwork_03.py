"""Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
где на первом месте номинал карты номинал (6 - 10, J, D, K, A),
а на втором название масти (Hearts, Diamonds, Clubs, Spades)."""

import random

"""faces = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
a = random.choice(faces)
b = random.choice(suits)
print(a)
print(b)
"""



def carddraw():
    faces = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    cards = []
    for suit in suits:
        for face in faces:
            cards.append([face, suit])
    card = random.choice(cards)
    return card
print(carddraw())