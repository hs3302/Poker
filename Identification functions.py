#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Straight Flush, including Royal Flush. There should be 40 combinations.
def IdSF(cards):
    # Determine flush or not
    if cards[0].suit==cards[1].suit==cards[2].suit==cards[3].suit==cards[4].suit:
        cards_sort = sorted(cards,key=lambda x:x.number) # Sort by number
        # Situation 1: not include Ace
        if cards_sort[4].number != 14:
            # Determine straight or not
            if cards_sort[4].number == cards_sort[0].number + 4:
                return True
            else:
                return False
        # Situation 2: include Ace
        else:
            # Determine straight or not
            if cards_sort[0].number == 10 or cards_sort[3].number == 5:
                return True
            else:
                return False
    else:
        return False


# Four of a kind. There should be 624 combinations.
def IdFK(cards):
    unique_number = len(set([c.number for c in cards])) # Get the unique numbers in 5 cards
    # Four of a kind only has two different numbers, and they are distributed as 4+1
    if unique_number == 2:
        cards_sort = sorted(cards,key=lambda x:x.number)
        if cards_sort[0].number != cards_sort[1].number:
            return True
        elif cards_sort[3].number != cards_sort[4].number:
            return True
        else:
            return False
    else:
        return False


# Full house. There should be 3744 combinations.
def IdFH(cards):
    unique_number = len(set([c.number for c in cards])) # Get the unique numbers in 5 cards
    # Full house only has two different numbers
    if unique_number == 2:
        return True
    else:
        return False


# Flush. There should be 5108 combinations.
def IdFl(cards):
    if cards[0].suit==cards[1].suit==cards[2].suit==cards[3].suit==cards[4].suit:
        return True
    else:
        return False


# Straight. There should be 10200 combinations.
def IdSt(cards):
    cards_sort = sorted(cards,key=lambda x:x.number) # Sort by number
    # Situation 1: not include Ace
    if cards_sort[4].number != 14:
        # Determine straight or not
        if cards_sort[1].number == cards_sort[0].number + 1 and cards_sort[2].number == cards_sort[1].number + 1 and cards_sort[3].number == cards_sort[2].number + 1 and cards_sort[4].number == cards_sort[3].number + 1:
            return True
        else:
            return False
    # Situation 2: include Ace
    else:
        # Determine straight or not
        if cards_sort[0].number == 2 and cards_sort[1].number == 3 and cards_sort[2].number == 4 and cards_sort[3].number == 5:
            return True
        elif cards_sort[0].number == 10 and cards_sort[1].number == 11 and cards_sort[2].number == 12 and cards_sort[3].number == 13:
            return True
        else:
            return False


# Three of a Kind. There should be 54912 combinations.
def IdTK(cards):
    unique_number = len(set([c.number for c in cards])) # Get the unique numbers in 5 cards
    # Three of a Kind has 3 different numbers, and they are distributed as 3+1+1
    if unique_number == 3:
        cards_sort = sorted(cards,key=lambda x:x.number) # Sort by number
        if cards_sort[0].number == cards_sort[1].number == cards_sort[2].number:
            return True
        elif cards_sort[1].number == cards_sort[2].number == cards_sort[3].number:
            return True
        elif cards_sort[2].number == cards_sort[3].number == cards_sort[4].number:
            return True
        else:
            return False
    else:
        return False


# Two Pairs. There should be 123552 combinations.
def IdTP(cards):
    unique_number = len(set([c.number for c in cards])) # Get the unique numbers in 5 cards
    # Two Pair has 3 different numbers
    if unique_number == 3:
        return True
    else:
        return False


# One Pair. There should be 1098240 combinations.
def IdOP(cards):
    unique_number = len(set([c.number for c in cards])) # Get the unique numbers in 5 cards
    # One Pair has 4 different numbers
    if unique_number == 4:
        return True
    else:
        return False


# High Card. There should be 1302540 combinations.
