def getRoundResult(winning_suit, suit1, number1, suit2, number2):

    if suit1 == winning_suit and suit2 == winning_suit:
        if number1 > number2:
            return "Player 1 wins"
        elif number1 < number2:
            return "Player 2 wins"
        else:
            return "Draw"
    elif suit1 == winning_suit:
        return "Player 1 wins"
    elif suit2 == winning_suit:
        return "Player 2 wins"
    else:
        if number1 > number2:
            return "Player 1 wins"
        elif number1 < number2:
            return "Player 2 wins"
        else:
            return "Draw"


w = "B"
n = 5

print(getRoundResult(w, "A", 2, "B", 1))
