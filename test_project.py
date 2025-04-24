from project import valuator, deal_card, scoreboard, shuffle, dealer


def main():
    test_function_valuator()
    test_function_deal_card()
    test_function_scoreboard()
    test_function_shuffle()
    test_function_dealer()


#tests the valuator function to make sure returns right values for cards
def test_function_valuator():
    assert valuator("Ace of spades") == 1
    assert valuator("Two of hearts") == 2
    assert valuator("Three of clubs") == 3
    assert valuator("Four of diamonds") == 4
    assert valuator("Five of clubs") == 5
    assert valuator("Six of hearts") == 6
    assert valuator("Seven of diamonds") == 7
    assert valuator("Eight of spades") == 8
    assert valuator("Nine of clubs") == 9
    assert valuator("Ten of hearts") == 10
    assert valuator("Jack of spades") == 10
    assert valuator("Queen of clubs") == 10
    assert valuator("King of spades") == 10


#tests the deal_card function to make sure it moves the first element from one list to the last element of another list, and removes it from the first list without leaving an empty space
def test_function_deal_card():
    assert deal_card([1], []) == ([], [1])
    assert deal_card([1,2,3,4], [0]) == ([2,3,4], [0, 1])
    assert deal_card(["Ace of Clubs", "Two of Spades"], ["Three of Diamonds"]) == (["Two of Spades"], ["Three of Diamonds", "Ace of Clubs"])


#tests the scoreboard function such that it prints the correct values when given score values
def test_function_scoreboard(capsys):
    scoreboard(1, 2, 3)
    captured_prints = capsys.readouterr()
    all_printouts = captured_prints.out.split('\n')
    print_one = all_printouts[0]
    print_two = all_printouts[1]
    print_three = all_printouts[2]
    print_four = all_printouts[3]
    print_five = all_printouts[4]

    assert print_one and print_five == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    assert print_two == "Player: 1."
    assert print_three == "Dealer: 2."
    assert print_four == "Draws: 3."


#tests the shuffle function to confirm that all 52 cards are returned in a list
def test_function_shuffle():
    assert len(shuffle()) == 52


#tests the dealer function to make sure it'll draw cards for the dealer until the dealer hand is over 16 in value and will stop/not draw cards if dealer value is 17 or more
def test_function_dealer():
    assert dealer(["King of Clubs", "Queen of Spades"], 20, ["Two of Diamonds", "Three of Hearts"]) == 20
    assert dealer(["Ace of Clubs", "Seven of Spades"], 8, ["Four of Diamonds", "Five of Hearts"]) == 17
    assert dealer(["King of Clubs", "Six of Spades"], 16, ["Two of Diamonds", "Three of Hearts"]) == 18
    assert dealer(["King of Clubs", "Six of Spades"], 16, ["Jack of Diamonds", "Three of Hearts"]) == 26
