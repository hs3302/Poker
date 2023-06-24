#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Organize Straight Flush
def OrgSF(cards):
    cards_sort = sorted(cards,key=lambda x:x.number,reverse=True)
    if cards_sort[0].number != 14:
        return cards_sort
    else:
        if cards_sort[1].number == 13:
            return cards_sort
        else:
            return cards_sort[1:]+cards_sort[:1]
        
# Organize Four of a Kind
def OrgFK(cards):
    cards_sort = sorted(cards,key=lambda x:x.number,reverse=True)
    if cards_sort[0].number == cards_sort[1].number:
        return cards_sort
    else:
        return cards_sort[1:]+cards_sort[:1]

# Organize Full House
def OrgFH(cards):
    cards_sort = sorted(cards,key=lambda x:x.number,reverse=True)
    if cards_sort[1].number == cards_sort[2].number:
        return cards_sort
    else:
        return cards_sort[2:]+cards_sort[:2]
    
# Organize Flush
def OrgFl(cards):
    cards_sort = sorted(cards,key=lambda x:x.number,reverse=True)
    return cards_sort

# Organize Straight
def OrgSt(cards):
    cards_sort = sorted(cards,key=lambda x:x.number,reverse=True)
    if cards_sort[0].number != 14:
        return cards_sort
    else:
        if cards_sort[1].number == 13:
            return cards_sort
        else:
            return cards_sort[1:]+cards_sort[:1]
        
# Organize Three of a Kind
def OrgTK(cards):
    cards_sort = sorted(cards,key=lambda x:x.number,reverse=True)
    if cards_sort[0].number == cards_sort[1].number:
        return cards_sort
    elif cards_sort[1].number == cards_sort[2].number:
        return cards_sort[1:4]+cards_sort[:1]+cards_sort[4:]
    else:
        return cards_sort[2:]+cards_sort[:2]
    
# Organize Two Pairs
def OrgTP(cards):
    cards_sort = sorted(cards,key=lambda x:x.number,reverse=True)
    if cards_sort[0].number == cards_sort[1].number and cards_sort[2].number == cards_sort[3].number:
        return cards_sort
    elif cards_sort[0].number == cards_sort[1].number:
        return cards_sort[:2]+cards_sort[3:]+cards_sort[2:3]
    else:
        return cards_sort[1:]+cards_sort[:1]
    
# Organize One Pair
def OrgOP(cards):
    cards_sort = sorted(cards,key=lambda x:x.number,reverse=True)
    if cards_sort[0].number == cards_sort[1].number:
        return cards_sort
    elif cards_sort[1].number == cards_sort[2].number:
        return cards_sort[1:3]+cards_sort[:1]+cards_sort[3:]
    elif cards_sort[2].number == cards_sort[3].number:
        return cards_sort[2:4]+cards_sort[:2]+cards_sort[4:]
    else:
        return cards_sort[3:]+cards_sort[:3]
    
# Organize High Card
def OrgHC(cards):
    cards_sort = sorted(cards,key=lambda x:x.number,reverse=True)
    return cards_sort

