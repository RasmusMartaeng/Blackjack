import random
import time

def table():
    print("Welcome to Blackjack!")
    balance = float(input("How much do you want to buy-in for? "))

    cont = True

    while cont == True:
        balance = blackjackRound(balance)
        yesNo = input("Another round? y/n ")
        if yesNo == "n":
            cont = False
            print("Thank you for playing! You cash out $" + str(balance))

        if balance == float(0):
            balance = float(input("How much more would you like to buy-in for? "))



def blackjackRound(balance):
    print("Let's start!")
    time.sleep(1)
    print("Your balance is $" + str(balance))
    bet = float(input("How much do you bet? "))

    while bet > balance:
        bet = float(input("Too high! Please bet a lower amount: "))

    deck = generateDeck()

    time.sleep(1)
    playerHand = ["", ""]
    playerHand[0], deck = drawCard(deck)
    print("Hand: " + playerHand[0])
    time.sleep(1)

    dealerHand = ["", ""]
    dealerHand[0], deck = drawCard(deck)
    print("Dealer: " + "Hole")
    time.sleep(1)

    playerHand[1], deck = drawCard(deck)
    print("Hand: " + playerHand[0] + " & " + playerHand[1] + ", = " + str(sumHand(playerHand)))
    time.sleep(1)

    dealerHand[1], deck = drawCard(deck)
    print("Dealer: " + "Hole" + " & " + dealerHand[1])
    time.sleep(1)

    checkBlackjack(playerHand, dealerHand)

    playerHand, deck, playerBust = hitOrStand(playerHand, deck)

    if playerBust == True:
        balance = playerLoss(balance, bet)
    else:
        time.sleep(1)
        print("Dealer: " + dealerHand[0] + " & " + dealerHand[1] + ", = " + str(sumHand(dealerHand)))
        dealerHand, deck, dealerBust = dealerHit(dealerHand, deck)

        balance = evaluate(playerHand, playerBust, dealerHand, dealerBust, balance, bet)

    return balance

def generateDeck():

    deck = ["2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "Jack♠", "Queen♠", "King♠", "Ace♠",
            "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "Jack♥", "Queen♥", "King♥", "Ace♥",
            "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "Jack♦", "Queen♦", "King♦", "Ace♦",
            "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "Jack♣", "Queen♣", "King♣", "Ace♣"]
    return deck

def drawCard(deck):

    card = random.choice(deck)
    deck.remove(str(card))

    return card, deck

def checkBlackjack(playerHand, dealerHand):
    playerHandSum = sumHand(playerHand)
    dealerHandSum = sumHand(dealerHand)
    if playerHandSum == 21 and dealerHandSum != 21:
        print("player Win")
        #playerWin()
    elif playerHandSum != 21 and dealerHandSum == 21:
        print("house Win")
        print(dealerHand[0] + dealerHand[1])
        #houseWin()
    elif playerHandSum == 21 and dealerHandSum == 21:
        print("Push")
        print(dealerHand[0] + dealerHand[1])
        #push()
        return

def checkBust(hand):
    handSum = sumHand(hand)
    if handSum > 21:
        print("BUST!")
        time.sleep(1)
        bust = True
    else:
        bust = False

    return bust


def sumHand(hand):
    intHand = []
    for card in hand:
        card = card[:-1]
        try:
            card = int(card)
        except:
            if card == "Jack":
                card = 10
            elif card == "Queen":
                card = 10
            elif card == "King":
                card = 10
            elif card == "Ace":
                card = 11
        intHand.append(card)

    handSum = sum(intHand)

    while handSum > 21 and 11 in intHand:
        for i in range(len(intHand)):
            if intHand[i] == 11:
                intHand[i] = 1
                break
        handSum = sum(intHand)
    return handSum

def hitOrStand(hand, deck):
    move = "h"
    bust = False

    while move == "h" and bust == False:
        move = input("Hit (h) or Stand (s)?")

        if move == "h":
            newCard, deck = drawCard(deck)
            hand.append(newCard)
            print(", ".join(hand) + "  = " + str(sumHand(hand)))
            bust = checkBust(hand)
        elif move == "s":
            print("You stand at: " + ", ".join(hand) + " = " + str(sumHand(hand)))

    return hand, deck, bust

def dealerHit(hand, deck):
    while sumHand(hand) <17:
        newCard, deck = drawCard(deck)
        hand.append(newCard)
        print(", ".join(hand) + " = " + str(sumHand(hand)))
        time.sleep(1)
    bust = checkBust(hand)

    return hand, deck, bust

def evaluate(playerHand, playerBust, dealerHand, dealerBust, balance, bet):

    if dealerBust == True:
        balance = playerWin(playerHand, balance, bet)
    elif sumHand(playerHand) > sumHand(dealerHand):
        balance = playerWin(playerHand, balance, bet)
    elif sumHand(playerHand) < sumHand(dealerHand):
        balance = playerLoss(balance, bet)
    elif sumHand(playerHand) == sumHand(dealerHand):
        balance = playerPush(balance)

    return balance



def playerWin(hand, balance, bet):
    handSum = sumHand(hand)
    if handSum == 21:
        print("Blackjack! You win!")
        balance = balance + bet*1.5
        print("New balance = $" + str(balance))
    else:
        print("You win!")
        time.sleep(1)
        balance = balance + bet
        print("Your balance is $" + str(balance))

    return balance


def playerLoss(balance, bet):

    print("You loose...")
    time.sleep(1)
    balance = balance - bet
    print("Your balance is $" + str(balance))

    return balance


def playerPush(balance):
    print("You push...")
    time.sleep(1)
    print("Your balance is $" + str(balance))

    return balance

table()
