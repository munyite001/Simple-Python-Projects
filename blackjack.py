"""
Blackjack, by Emmanuel Munyite
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack

Tags: large, game, card game

|A  | |10 |
| ♣ | | ♦ |
|__A| |_10|

 """



from ast import While
import dis
from pickle import TRUE
import random,sys

#   Set up the constants:
HEARTS   = chr(9829)      # Character 9829 is '♥'
DIAMONDS = chr(9830)      # Character 9830 is '♦'.
SPADES   = chr(9824)      # Character 9824 is '♠'.
CLUBS    = chr(9827)      # Character 9827 is '♣'.  

BACKSIDE = 'backside'


def main ():
    print("""
    ♣ Blackjack Card Game by Emmanuel Munyite ♣
    ===================================================

    Rules:

        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.
        
    """)

    money = 5000

    while True: #   Main game loop
        #   check if the player has run out of money
        if money <= 0:
            print("You're broke!")
            print("Good thing you were'nt playing with real money")
            print("Thanks for playing!")
            sys.exit()

        #  Let the player enter their bet for this round
        print("Money: ", money)
        bet = getBet(money)

        #   Give the dealer and  player 2 cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(),deck.pop()]
        playerHand = [deck.pop(),deck.pop()]

        #   Handle player actions
        print('Bet: ', bet)
        while True: #   keep looping until player stands or busts
            displayHands(playerHand,dealerHand,False)
            print()

            #   check if the player has bust:
            if getHandValue(playerHand) > 21:
                break

            #   Get the player's moves either H, S, or D:
            move = getMove(playerHand, money - bet)

            #   Handle the player's actions
            if move == 'D':
                #   Player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet,(money - bet)))
                bet += additionalBet
                print(f'Bet increased to {bet}.')
                print('Bet:', bet)

            if move in ('H','D'):
                #   Hit/Doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}')
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted:
                    continue
            if move in ('S','D'):
                #   Stand/Doubing down stops the player's turn
                break
        # Handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break # The dealer has busted.

                input('Press Enter to continue...')
                
                print('\n\n')

        #   Show the final hands
        displayHands(playerHand,dealerHand,True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        #   Handle wether the player won, lost, or tied
        if dealerValue > 21:
            print(f'Dealer busts! You win {bet}')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You Lost!')
            money -= bet
        elif playerValue > dealerValue:
            print(f'You won {bet}')
            money += bet
        elif playerValue == dealerValue:
            print(f"It's a tie, the bet is returned to you")

        input("Press Enter to continue...")
        print('\n\n')

def getBet(maxBet):
    """ Ask the player how much they want to bet for this round """
    while True: #   Keep asking until they enter a valid amount
        print(f"How much do you want to bet ? 1 - {maxBet} or Quit")
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print("Thanks for playing")
            sys.exit()

        if not bet.isdecimal():
            continue #  If the player did not enter a number ask again

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  #   Player entered a valid bet.
        
def getDeck():
    """ Return a list of (rank, suite) tuples for all 52 cards """
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range (2,11):
            deck.append((str(rank),suit))   #   Add the numbered cards
        for rank in ('J','K','Q','A'):
            deck.append((rank,suit))    #   Add the face and ace cards

    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand,showDealerHand):
    """ Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False."""
    print()
    if showDealerHand:
        print('DEALER:',getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        #   Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    #   Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """ 
    Returns the value of the cards. Face cards are worth 10, aces are
    171.worth 11 or 1 (this function picks the most suitable ace value). 
    """
    value = 0 
    numberofAces = 0

    #   Add the value for the non ace cards
    for card in cards:
        rank = card[0]  #   Card is a tuple like (rank, suit)
        if rank == 'A':
            numberofAces += 1
        elif rank in ('J','Q','K'):
            value += 10
        else:
            value += int(rank) #    Numbered cards are worth their number.

    #   Add the value for the aces
    value += numberofAces   #   Add 1 per ace.
    for i in range(numberofAces):
        #   If another 10 can be added with busting do so:
        if value + 10 < 21:
            value += 10

    return value

def displayCards(cards):
    """ Display all the cards in the card list"""
    rows = ['','','','',''] #   The text to display on each row

    for  i, card in enumerate(cards):
        rows[0] += ' ___ '  #   Print the top line of the card
        if card == [BACKSIDE]:
            #   Print a card's back
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'

        else:
            #   print the card's front
            rank, suit = card # The card is a tuple structure
            rows[1] += f"|{rank.ljust(2)} | "
            rows[2] += f"| {suit} | "
            rows[3] += f"|_{rank.rjust(2, '_')}| "
    
    #   Print each row on screen
    for row in rows:
        print(row)


def getMove(playerHand,money):
    """
    Asks the player for their move, and returns
    'H' for hit, 'S' for stand, and 'D' for double down.
    """
    while True: #   Keep asking until they provide a valid move
        #   Determine what moves the player can make
        moves = ['(H)it','(S)tand']

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        #   Get the player's move:
        movePrompt = ','.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H','S'):
            return move             #   Player has entered a valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move     #   Player has entered a valid move.





















if __name__ == '__main__':
    main()