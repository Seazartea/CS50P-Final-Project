# Simple terminal Blackjack

## Video demo link: https://youtu.be/tnRaN_-LhWA

## Project Description:
This code runs a game of blackjack which you play in the terminal window. The blackjack game follows general blackjack rules which will be explained further down.
The main function of the code runs the base game in a nested while loop, such that it doesn't end after 1 round of playing and continues.
It uses if and elif statements that trigger depending on inputs from the player, and later on hand values to determine who wins each round and making outputting the correct print statements and changes to the win, losses and draw counts.

The rules function simply prints out a large paragraph of text to explain the rules of the game to the player/user. It was more concise having it in a function rather than several times in the main code.

The scoreboard function prints out a scoreboard when called showing the relative wins, losses and draws of the played rounds. The losses are shown as dealer wins. Again it was more concise having it in a seperate function than several times in the main code.

The shuffle function contains the a list of all the cards in a card deck in a list. Which the order is then randomised to simulate shuffling a deck of cards and the shuffled list is returned back.

The deal_card function chooses the first element in the deck list, simulating taking a card off the top of a deck. Then adds that to a second list, which will be either the player's or dealer's hand. It then removes the element from the deck list such that the same card can't be 'drawn' twice as only one of each card exist in a deck.

The dealer function simulates the dealer's turn in the game. It follows the blackjack rule that a dealer has to draw if their hand value is less than or equal to 16, otherwise they don't draw a card.

The valuator function converts the str name of any card to a numerical value. Doing so by only using the first word in the name of the card to not have 52 seperate entries in the dict and meaning that it doesn't matter what the suit of the cards are.



When you run the code you play against the computer following the blackjack rules where you aim to get 21 or as close to 21 without going over and aiming to get a higher hand value than the dealer.
You start being dealt two cards, the game will tell you the total hand value, and the dealer is also dealt two cards though only one of which you can see. You then have to choose whether to 'hit', draw another card, or 'stand', stick with your current cards.
The dealer will then play. The dealer follows the blackjack rule where they have to draw a card if their hand value is less than 16.
If either the player or dealer goes over a hand value of 21 they go 'bust' and instantly lose no matter what hand value the other has.
If either player or dealer has a hand value of 21, they have 'blackjack' and win the round instantly.
There is no betting function implemented, however wins, losses and dwraws and counted on a scoreboard that is displayed at the exiting of the program.
The code will display the rules of the game, including what are valid inputs for each option.



##Design Choices:
I started with the initial idea of not showing what cards you had but only their values. I changed this to showing the cards you have, along with the symbol for the suit of the card, and the total numerical value of the cards in your hand. Showing the total numerical value helps the user not have to work out their hand value each time so helps with ease of using the code. While showing the card and symbol was more a design choice instead of it being plain text you see.


Went with using a dict to store the card values in that I could compare the name of each card against to get their value instead of having a long list of all 52 cards and their values. This was done by using the startswith() function as the first word in each card denotes its numerical value.


To simplify the code I decided to treat ace cards as having a value of '1' instead of both 1 and 11. I also decided against allowing the player or dealer to split their hand when they have two aces as I was looking to keep the game relatively simple.


I decided to go with a score tracking system for wins, losses and draws instead of implementing a betting system for playing the game. This was partially done for simplicity and allowing you to keep playing as many rounds as you liked instead of worrying about running out of coins or whatever currency but also due to being unsure if I wanted to include what is effectively a feature that imitates gambling.


I added simple number inputs for each option you can choose to do, like draw a card or stand, such that it is easier to use as you no longer have to write an entire word for each of your moves. I did end up leaving the original input words in the code incase the user writes those.


For some ease of use when trying to use the code I added various print lines of code that help make the output more easily readable. These include: print() lines to form breaks in output, lines of "------" to make it easier to determine different hands of the game, varied "_-_-_-_-_" on the invalid input print to make it stand out more from the rest of the text and breaking up the rules print output with print() to make each section stand out more easier instead of being on block paragraph.


### File details
*project.py contains the code for the project and when run simulates a simple game of blackjack in the terminal window.
*README.md is this file and contains an explanation of the project and other key information.
*requirements.txt contain a list of all pip-installable libraries that the project requires to run.
*test_project.py contains the test functions to test several of the functions in the main project code when run.
