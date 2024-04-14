import random

def draw_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    drawn_card = random.choice(cards)
    return drawn_card

def take_turns(score, cards, player):
    if player == 'user':
        take_hit = input("Would you like another card? Press Y for 'hit' and N to end your turn.: ")
        while take_hit.lower() == 'y':
            new_card = draw_card()
            score += new_card
            cards.append(new_card)
            if score > 21 and 11 in cards:
                ace_location = cards.index(11)
                cards[ace_location] = 1
                score -= 10
            print(f"Players cards: {cards}/ Players score: {score}")
            if score > 21:
                take_hit == 'n'
                return score
            take_hit = input("Would you like another card? Press Y for 'hit' and N to end your turn.: ")
        return score
    if player == 'computer':
        while score < 17:
            new_card = draw_card()
            score += new_card
            cards.append(new_card)
            if score > 21 and 11 in cards:
                ace_location = cards.index(11)
                cards[ace_location] = 1
                score -= 10
            print(f"Computer hits and draws {new_card}/ computers score: {score}")
        return score


play = True


#Loop through until player or computer either win or bust
while play:
    computer_score = 0
    computer_cards = []
    user_score = 0
    user_cards = []
    new_card = draw_card()
    computer_score += new_card
    computer_cards.append(new_card)
    new_card = draw_card()
    user_score += new_card
    user_cards.append(new_card)
    
    print(f"Computer's card: {computer_cards[0]}")
    print(f"Your cards: {user_cards}/ Players score: {user_score}")
    user_score = take_turns(player='user', score=user_score, cards=user_cards)
    if user_score > 21:
        print("Player busted! Computer wins!")
        continue_game = input("Play another round? Y for yes, N for no: ")
        if continue_game.lower() == 'n':
            play = False
        print("\n\n\n")
        continue
    computer_score = take_turns(player='computer', score=computer_score, cards=computer_cards)
    if computer_score > 21:
        print("Computer busted! Player wins!")
        continue_game = input("Play another round? Y for yes, N for no: ")
        if continue_game.lower() == 'n':
            play = False
        print("\n\n\n")
        continue
    
    if user_score == computer_score:
        print("It's a tie!")
    elif user_score > computer_score:
        print("User wins!")
    else:
        print("Computer wins!")

    continue_game = input("Play another round? Y for yes, N for no: ")
    print("\n\n\n")
    if continue_game.lower() == 'n':
        play = False

    
