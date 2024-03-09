# Leonard Allen
# Lab 07
# Lame Game
# This program will output a menu for the user to choose from. 1 - Make Change | 2 - High Card | 3 - Quit 
# *Make Change* is accessible. Enter in the amount a custome owes and the amount they pay to get the amount of change they will get back.
# *High Card has* been added. The users inputs there names and draws a card. The highest value card wins.
# *Deal hand* has been added. The user draws five random cards and is displayed on the screen.
# *Save Dream Hand* has been added. User creates a Dream Hand and saves it for later use in the program.
# *Display Dream Hand* has been added. Displays the saved hand the user added earlier in saved Dream Hand.
# *Quit* is now assigned a boolean value True until option is chosen.
# Added some basic ASCII art
# Cleaned up the program a little bit for easier changes.
# Added Exceptions to handle errors
# Data structures were added


Make_Change = 1
High_Card = 2
Deal_Hand = 3
Save_Dream_Hand = 4
Display_Dream_Hand = 5
Word_Guess = 6
Quit_ = 7


# Function: Welcome
# Inputs: None
# Outputs: None
# Purpose: The function prints out a welcome message for the user at the start of the program
def welcome():
    # Prints welcome message
    print("""Welcome user, \nto the LAME GAME gaming room. The room is currently under """)
    print("""construction, so currently only have a few options for you to select from.""")
    print("""Please stay tuned, we plan on sendiing updates every week. Thank you!\n""")
    print("""New games have been added recently! Give our newest game 'Deal Hand' a go!\n\n""")

# Funtion: Main
# Inputs: None
# Outputs: None
# Purpose: The main function calls the function the function we select in the Menu function.
def main():
    # Prints welcome message
    welcome()

    option = menu()
    
    while option != Quit_:
        
        
        if option == Make_Change:
            make_change()

        elif option == High_Card:
            high_card()

        elif option == Deal_Hand:
            deal_hand()
        
        elif option == Save_Dream_Hand:
            save_dream_hand()

        elif option == Display_Dream_Hand:
            display_dream_hand()

        elif option == Word_Guess:
            word_guess()

        option = menu()
        
            
# Function: Menu
# Inputs: None
# Output: Returns the option to the main function
# Purpose: Displays the menu. Also checks if user inputs a valid option.
def menu():
    # printing the menu
    print("MENU:\n\t1. Make Change\n\t2. High Card\n\t3. Deal Hand\n\t4. Save Dream Hand\n\t5. Display Dream Hand\n\t6. Quit\n")

    # User must make a  "VALID" decision
    try:
        option = int(input("Please choose an option (1, 2, 3, 4, 5, 6, or 7) to contiue: "))
        
        while option < Make_Change or option > Quit_:
            print("Invalid option! Please select an option from the menu.\n")
            print("MENU:\n\t1. Make Change\n\t2. High Card\n\t3. Deal Hand\n\t4. Save Dream Hand\n\t5. Display Dream Hand\n\t6. Quit\n")
            option = int(input("Please choose an option (1, 2, 3, 4, 5, 6, or 7) to contiue: "))

            
    # If there is an error with the input, this message will be displayed.
    except ValueError:
        print("\nERROR! The value used is not valid.\n")
        return -1

    return option
        
# Function: Make Change
# Input: None
# Output: None
# Purpose: User gives the amount they owe and how they will pay. The function then gives them the change amount.
def make_change():
    print("""\nPlaying the "Make Change" game\n""")

    # Read the amount of the purchase
    price = float(input('\nEnter the amount of the purchase '))

    # Read the amount of the payment
    paid = float(input('Enter the amount of payment '))
    
    # Check to see if the payment is enough to cover the purchase
    if paid < price:
        print('You did not pay enough')
        
    else:

        # Calculate the change due
        change = paid - price

        # Display the change due
        print('\nChange due: ',format(change,'.2f'))
        #print('   unformatted: ',change)
        print('This breaks down into:')

        # Calculate the number of dollars due
        dollars = int(change)
        print('\tDollars:\t',dollars)

        # Isolate the change amount and convert it to an integer.
        # To account for precesion lost converting to an integer,
        # force rounding of the 100ths digit by adding .005
        # to the change portion
        change = int(((change - dollars) + .005)* 100)
        #print('change is now ',change)

        # Calculate the number of quaters due
        quarters = change // 25
        print('\tQuarters:\t',quarters)
        change = change - (quarters * 25)

        # Calculate the number of dimes due
        dimes = change // 10
        print('\tDimes:\t\t',dimes)
        change = change - (dimes * 10)

        # Calculate the number of nickels due
        nickels = change // 5
        print('\tNickels:\t',nickels)
        change = change - (nickels * 5)

        # The number of pennies due will be all that is left
        pennies = change
        print('\tPennies:\t',pennies)

    print('___________________________________________________')
    print('\n\n')


# Function: High Card
# Input: None
# Output: None
# Purpose: After inputting each user name, this function gives each player a random card. Function then chooses the
#       higher card as the winner.
def high_card():
    #Player names
    player1 = input("Enter a name for player 1:\t")
    player2 = input("Enter a name for player 2:\t")
    print()

    # Imported Random function to get random number Generator
    card1 = random.randint(1,13)
    card2 = random.randint(1,13)

        
    # Assigns cards to displayable values for the user
    Display_Card1 = display_face_value(card1)
    Display_Card2 = display_face_value(card2)

    # Shows who drew what and declares the winner
    print(player1, "drew a", Display_Card1, sep=' ')
    print(player2, "drew a", Display_Card2, sep=' ')
    print()
    if card1 < card2:
        print(Display_Card1, " is lower than ", Display_Card2,"!", sep='')
        print(player2, " wins!\n", sep='')
    elif card1 > card2:
        print(Display_Card1, "is higher than ", Display_Card2,"!", sep='')
        print(player1, " wins!\n", sep='')
    else:
        print("The cards are the same!\nIts a tie!\n")
    print('___________________________________________________')
    print('\n\n')
    

# Function: Display Face Value
# Inputs: card_val reprsents the value of the card. 
# Output: Returns a string that represent the card value, and the number value of the card.
# Purpose: Displays the card value that the user has or randomly chooses.
def display_face_value(card_val):
    if card_val == 1:
        return "Ace"
    elif card_val == 2:
        return "Two"
    elif card_val == 3:
        return "Three"
    elif card_val == 4:
        return "Four"
    elif card_val == 5:
        return "Five"
    elif card_val == 6:
        return "Six"
    elif card_val == 7:
        return "Seven"
    elif card_val == 8:
        return "Eight"
    elif card_val == 9:
        return "Nine"
    elif card_val == 10:
        return "Ten"
    elif card_val == 11:
        return "Jack"
    elif card_val == 12:
        return "Queen"
    else:
        return "King"



# Function: Deal Hand
# Input: None
# Output: None
# Purpose: Generates 5 random cards form display face value. Also added a point system for the value of the hand.
def DealHand():

    card1 = random.randint(1, 13)
    card2 = random.randint(1, 13)
    card3 = random.randint(1, 13)
    card4 = random.randint(1, 13)
    card5 = random.randint(1, 13)
    
    Hand = [card1, card2, card3, card4, card5]
    print(Hand)
    Hand_Display = display_hand(Hand)

    print(Hand_Display)

    total_points, average = hand_stats(Hand)

    print("The value of these cards are ", total_points, ". \nThat averages each card to be ", average, '.', sep='')
    print('___________________________________________________')
    print('\n\n')


# Function: Display Hand
# Inputs: hand reprsents the list generated from the Deal Hand function where we are tryong to get random values
# Output: returns the hand valueas a list
# Purpose: Individually gets a random integer from the display
def display_hand(hand):
    disp_hand = []
    for card in hand:
        disp_hand.append(display_face_value(card))
    

    return disp_hand


# Function: Hand Stats
# Input: hand represents the 5 cards from the deal hand function
# Output returns both total and average of the value of cards.
# Purpose: Purpose is to take the value of cards, average the the values or return the total.
def hand_stats(stat_hand: list):
    total = 0
    
    for stat in stat_hand:
        total += stat
    average = total/5
    return total, average
    

    print("You are currently holding " + card1, card2, card3, card4, "and " + card5, sep=', ')


# Funtion: Quit
# Input: None
# Output: returns False if called
# Purpose: Stops programing by changing the while True statement to False.
def Quit():
    return False


# Function: Save Dream Hand
# Input: None
# Output: None
# Purpose: User inputs a value for each 5 cards in this function. Those 5 cards will be saved to a file
def save_dream_hand():
    hand = []

    # User creates file neam
    file_name = input('Save file name as: ')

    # File is open for writing
    cards_file = open(file_name + '.txt', 'w')
    


    # Added an exception to handle Value Errors
    try:
        # Loops 5 times
        for x in range(5):
            card = int(input("Give the number value for the card. input(1 - 13: "))

            # Loops if integer is not withing 1 through 13
            while card < 1 or card > 13:
                print("Invalid card! Card must be between 1 and 13.")
                card = int(input("Give the number value for the card. input(1 - 13: "))

            # Holds variable for card input in a list
            hand.append(card)

        #file inserts card variables
        for line in hand:
            cards_file.write(str(line) + '\n')

        # File is then closed
        cards_file.close()
            
    # Exception, if value is not an integer        
    except ValueError:
        print("ERROR! String characters aren't allowed. Please input a number as followed.")
        

 

    

    print('___________________________________________________')
    print('\n\n')
    
    # Return file name for later use when reading contents
    return file_name


# Function: Display Dream Hand
# Input: None
# Output: None
# Purpose: This function gathers data from file created and post it's contents for the user to understand.
def display_dream_hand():
    file = input("Enter file name:\t")
    
    Card_Names = []
    
    #Opens file
    cards_file = open(file + '.txt', 'r')

    print("Here are your dream cards:   ")

    
    cards = cards_file.readlines()

    index = 0

    # Reads file by line and inserts each value int a List
    while index < len(cards):
        cards[index] = int(cards[index].rstrip('\n'))
        index += 1

    # Loops through and adds the face value to a list to display
    for name in cards:
        Card_Names.append(display_face_value(name))

    # Displays the cards    
    print(Card_Names)

    # Close file
    cards_file.close()
       
    
    print('___________________________________________________')
    print('\n\n')


# Function: Word Guess
# Inputs: None
# Outputs: Nione
# Purpose: create a word. Make the word invisible for user. Have the user guess
#           the word by inputting letters. Function ends when user guesses the word.
def word_guess():
    word = input("Please enter a word for the WORD GUESS game:\t")
    guesses_used = ''
    
    word_disp = '*' * len(word)
    print('\n'*100)

    while word_disp != word:
        print('So far you have:\n\t', word_disp)
        char = input("Enter a character to guess:\t")
        
        if char in guesses_used:
            print('Letter already used!')

        elif char in word:
            if word.find(char) != len(word) -1:
                word_disp = word_disp[:word.find(char)] + char + word_disp[word.find(char) + 1:]
                guesses_used += char
            else:
                word_disp = word_disp[:word.find(char)] + char
                guesses_used += char
        else:
            guesses_used += char            

    print('Correct! You have guessed all letter correctly!')

    print('___________________________________________________')
    print('\n\n')

    
import random

# Calls the program to start.


main()
    

        


    
               

