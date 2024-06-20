import random

def initialize_deck():
    """Initialize a deck of cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    """Calculate the value of a hand."""
    value = 0
    num_aces = 0
    for card in hand:
        if card['rank'] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card['rank'] == 'Ace':
            num_aces += 1
            value += 11
        else:
            value += int(card['rank'])
    
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    
    return value

def display_hand(hand, player_name, hide_first_card=False):
    """Display the cards in a hand."""
    if hide_first_card:
        print(f"\n{player_name}'s hand:")
        print("Hidden Card")
        for card in hand[1:]:
            print(f"{card['rank']} of {card['suit']}")
    else:
        print(f"\n{player_name}'s hand:")
        for card in hand:
            print(f"{card['rank']} of {card['suit']}")

def blackjack():
    """Main function to play Blackjack."""
    print("Welcome to Python Blackjack!\n")
    
    while True:
        deck = initialize_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        
        display_hand(player_hand, "Player")
        display_hand(dealer_hand, "Dealer", hide_first_card=True)
        
        player_turn = True
        player_bust = False
        while player_turn:
            choice = input("\nDo you want to hit or stand? (h/s): ").strip().lower()
            if choice == 'h':
                new_card = deck.pop()
                player_hand.append(new_card)
                display_hand(player_hand, "Player")
                if calculate_hand_value(player_hand) > 21:
                    print("Player busts! Dealer wins.")
                    player_bust = True
                    break
            elif choice == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        
        if not player_bust:
            display_hand(dealer_hand, "Dealer")  # Reveal dealer's hidden card
            while calculate_hand_value(dealer_hand) < 17:
                new_card = deck.pop()
                dealer_hand.append(new_card)
                display_hand(dealer_hand, "Dealer")
                if calculate_hand_value(dealer_hand) > 21:
                    print("Dealer busts! Player wins.")
                    break
            
            player_value = calculate_hand_value(player_hand)
            dealer_value = calculate_hand_value(dealer_hand)
            
            print("\nFinal hands:")
            display_hand(player_hand, "Player")
            display_hand(dealer_hand, "Dealer")
            
            if player_value > dealer_value:
                print("Player wins!")
            elif dealer_value > player_value:
                print("Dealer wins!")
            else:
                print("It's a tie!")
        
        play_again = input("\nDo you want to play another game? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# Play the game
blackjack()
