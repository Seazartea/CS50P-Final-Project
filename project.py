import random


def main():
    #print rules first off to inform player of rules
    rules()
    #set up score tracking variables
    player_score = 0
    dealer_score = 0
    draws = 0
    #setting up lists for player input options
    rule = ["rule", "rules", "5"]
    score = ["score", "scores", "scoreboard", "scoreboards", "6"]
    exit = ["exit", "end", "leave", "finish", "0"]
    hit = ["hit", "h", "yes", "y", "draw", "card", "1"]
    stand = ["stand", "s", "no", "n", "2"]
    #set up the play variable to allow the main while loop to run
    play = "yes"
    #start while true loop
    while play == "yes":
        #lists to set up the players and dealers hand as empty
        players_hand = []
        dealers_hand = []
        #call shuffle function to shuffle and return the deck
        deck = shuffle()
        #sets the total value of the player and dealer hands
        dealer_value = 0
        player_value = 0
        #call deal_cards functions 4 times in row, alternating between player and dealer to deal first cards of the game
        #calls the valuator function to get the value of each card as its dealt to add to the total value of dealer or player, the [-1] denoting the last item in the list
        #the temp_ to get around errors
        temp_deck, temp_players_hand = deal_card(deck, players_hand)
        player_value = player_value + valuator(temp_players_hand[-1])
        deck, temp_dealers_hand = deal_card(temp_deck, dealers_hand)
        dealer_value = dealer_value + valuator(temp_dealers_hand[-1])
        temp_deck, players_hand = deal_card(deck, temp_players_hand)
        player_value = player_value + valuator(players_hand[-1])
        deck, dealers_hand = deal_card(temp_deck, temp_dealers_hand)
        dealer_value = dealer_value + valuator(dealers_hand[-1])
        #prints a line to make it easier to determine rounds of game
        print()
        print("------------------------------------------------------------")

        #while true loop for player inputs
        while True:
            #prints a blank to space out outputs
            print()
            #print player and dealers hands, keeping 1 of dealers hidden
            print(f"Your cards: {players_hand} with total value: {player_value}.")
            #If player's starting hand is a blackjack, instant win for the round
            if player_value == 21:
                print("Player has Blackjack, Player wins")
                player_score = player_score + 1
                break
            print(f"The dealer has a {dealers_hand[0]} face up and one face down card.")
            #let player input their moves
            choice = input("What's your move? ")
            #if statements that depend on different player input
            if choice.lower() in rule:
                #call rule function
                rules()
            elif choice.lower() in score:
                print()
                print("The current score is:")
                #call scoreboard to print current scores
                scoreboard(player_score, dealer_score, draws)
            elif choice.lower() in exit:
                #changes play variable to break main while loop
                play = "no"
                break
            elif choice.lower() in hit:
                #call deal_card function for player
                temp_deck, temp_players_hand = deal_card(deck, players_hand)
                deck = temp_deck
                players_hand = temp_players_hand
                #add the new card value to the total for the player
                player_value = player_value + valuator(players_hand[-1])
                #if player goes over 21, they lose and ends loop
                if player_value > 21:
                    #create spacing
                    print()
                    print("Player has bust, Dealer wins")
                    dealer_score = dealer_score + 1
                    break
                #if player has 21/blackjack, they win, ends loop
                elif player_value == 21:
                    #create spacing
                    print()
                    print("Player has Blackjack, Player wins")
                    player_score = player_score + 1
                    break
            #if player chooses to stand, turns to dealer turn
            elif choice.lower() in stand:
                #call dealer function to let dealer play
                dealers_value = dealer(dealers_hand, dealer_value, deck)
                #if returned dealer value over 21, print dealer bust, player wins, +1 to player score
                if dealers_value > 21:
                    print()
                    print("Dealer has bust, Player wins")
                    player_score = player_score + 1
                    break
                #elif player value > dealer value, print player wins, +1 to player score
                elif player_value > dealers_value:
                    print()
                    print ("Player has higher total card value, Player wins")
                    player_score = player_score + 1
                    break
                #elif dealer value > player value, print dealer wins, +1 to dealer score
                elif dealers_value > player_value:
                    print()
                    print("Dealer has higher total card value, Dealer wins")
                    dealer_score = dealer_score + 1
                    break
                #elif dealer value == player value, print draw, +1 to draws
                elif dealers_value == player_value:
                    print()
                    print("Player and Dealer have same total card value, it's a Draw")
                    draws = draws + 1
                    break
            #catch for any user inputs not valid
            else:
                print()
                print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
                print()
                print("Invalid input, input 'rules' if need help or usable inputs")
                print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

    print()
    #print final score
    print("The final score is:")
    scoreboard(player_score, dealer_score, draws)





#function to print rules to show what the code is about and accepted inputs for each action
def rules():
    print()
    print("===========================RULES============================")
    print("This is a simplified version of blackjack, mainly without the betting, splitting hands or aces acting as 2 different values, aces count as 1.")
    print("The goal is to get a higher score than the dealer and get as close to 21 as possible without going over 21 and busting.")
    print("The dealer will always draw a card if they have a hand value less than 17.")
    print()
    print("The game only accepts specific inputs for each action which are as follows.")
    print("To see the rules (this stuff) enter: '5', 'rule' or 'rules'.")
    print("To see the scoreboard enter: '6', 'score', 'scores', 'scoreboard' or 'scoreboards'.")
    print("To exit/end the program enter: '0', 'exit', 'end', 'leave' or 'finish'.")
    print("The program will also exit to a ctrl+d input.")
    print("To hit/draw a card enter: '1', 'hit', 'h', 'yes', 'y', 'draw' or 'card'.")
    print("To stand/stick with hand you've got enter: '2', 'stand', 's', 'no', or 'n'.")
    print()
    print("A line of '-------' represents a new hand occuring.")
    print("At the exiting of the program a final score will be displayed showing total wins, losses and draws.")
    print("Please enjoy the game.")
    print("============================================================")



#function to print scoreboard, wins, losses and draws
def scoreboard(player_score, dealer_score, draws):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Player: {player_score}.")
    print(f"Dealer: {dealer_score}.")
    print(f"Draws: {draws}.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



#function to reset the lists/cards and shuffle the deck
def shuffle():
    #all cards in a deck in a list format
    deck = ["Ace of Clubs♣", "Two of Clubs♣", "Three of Clubs♣", "Four of Clubs♣", "Five of Clubs♣", "Six of Clubs♣", "Seven of Clubs♣", "Eight of Clubs♣", "Nine of Clubs♣", "Ten of Clubs♣", "Jack of Clubs♣", "Queen of Clubs♣", "King of Clubs♣",
            "Ace of Diamonds♦", "Two of Diamonds♦", "Three of Diamonds♦", "Four of Diamonds♦", "Five of Diamonds♦", "Six of Diamonds♦", "Seven of Diamonds♦", "Eight of Diamonds♦", "Nine of Diamonds♦", "Ten of Diamonds♦", "Jack of Diamonds♦", "Queen of Diamonds♦", "King of Diamonds♦",
            "Ace of Hearts♥", "Two of Hearts♥", "Three of Hearts♥", "Four of Hearts♥", "Five of Hearts♥", "Six of Hearts♥", "Seven of Hearts♥", "Eight of Hearts♥", "Nine of Hearts♥", "Ten of Hearts♥", "Jack of Hearts♥", "Queen of Hearts♥", "King of Hearts♥",
            "Ace of Spades♠", "Two of Spades♠", "Three of Spades♠", "Four of Spades♠", "Five of Spades♠", "Six of Spades♠", "Seven of Spades♠", "Eight of Spades♠", "Nine of Spades♠", "Ten of Spades♠", "Jack of Spades♠", "Queen of Spades♠", "King of Spades♠"]
    #shuffles the deck
    random.shuffle(deck)
    #returns the shuffled deck
    return deck



#function to deal cards to inputted list
def deal_card(deck, hand):
    #selects the first card in the list
    card = deck[0]
    #adds card to hand inputted into function
    hand.append(card)
    #removes the card from the deck list
    deck.pop(0)
    return deck, hand



#function for how dealer plays
#dealer draws on 16 or less and stands on 17 or more
#return value of dealers cards
def dealer(dealers_hand, dealer_value, deck):
    while dealer_value <=16:
        #calls deal_card function for the dealer to draw a card, temp_ to ignore errors
        temp_deck, temp_dealers_hand = deal_card(deck, dealers_hand)
        deck = temp_deck
        dealers_hand = temp_dealers_hand
        #adds the new cards value to the total
        dealer_value = dealer_value + valuator(temp_dealers_hand[-1])
    return dealer_value



#function to return value of a card
def valuator(card):
    #create a dict holding all the cards and their relative values
    card_values = {
        "Ace": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10
    }
    #turns string into usable format to grab individual words
    string = card.split()
    #grabs only the first word to use
    prefix = string[0]
    #compares prefix of card against dict to get value
    value = card_values[prefix]
    return value




if __name__ == "__main__":
    main()
