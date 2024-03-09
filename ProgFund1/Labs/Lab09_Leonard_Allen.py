# Leonard Allen
# Lab 07
# Lame Game
# This program will output a menu for the user to choose from. 1 - Make Change | 2 - High Card | 3 - Deal Hand | 4 - Save Dream Hand
# 5 - Display Dream Hand | 6 - Guess | 7 - Quit
# ************** Final Release *******************
# This program is the final version of the Lame Game. Inside you will find code such as:
#   -Make Change         User inputs money owed and how much the will be paid. The program then returns how much achange the user get's
#                        or the amount left the user must pay.
#   -High Card           After the user input's their names, a random card will be given to each user. The highest value card wins.
#   -Deal Hand           The user draws five random cards and is displayed on the screen.
#   -Save Dream Hand     User creates a Dream Hand and saves it for later use in the program.
#   -Display Dream Hand  has been added. Displays the saved hand the user added earlier in saved Dream Hand.
#   -Word Guess          User will input a word. The word then becomse hidden. User then must guess the word by inputting characters



import card_Allen

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
    print("""New games have been added recently! Give our newest game 'Word Guess' a go!\n\n""")

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
    print("MENU:\n\t1. Make Change\n\t2. High Card\n\t3. Deal Hand\n\t4. Save Dream Hand\n\t5. Display Dream Hand\n\t6. Word Guess\n\t7. Quit\n")

    # User must make a  "VALID" decision
    try:
        option = int(input("Please choose an option (1, 2, 3, 4, 5, 6, or 7) to contiue: "))
        
        while option < Make_Change or option > Quit_:
            print("Invalid option! Please select an option from the menu.\n")
            print("MENU:\n\t1. Make Change\n\t2. High Card\n\t3. Deal Hand\n\t4. Save Dream Hand\n\t5. Display Dream Hand\n\t6. Word Guess\n\tQuit\n")
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
#       higher card as the winner. *Uses the module card_Allen*
def high_card():
    print('\n')
    # Inputs player's names
    player1 = input("Enter a name for player 1:\t")
    player2 = input("Enter a name for player 2:\t")
    print('\n')

    # Creates objects from the card class
    player1_card = card_Allen.Card()
    player2_card = card_Allen.Card()

    # Creates a random card in the Card class
    player1_card.deal()
    player2_card.deal()
     
    # Assigns cards to displayable values for the user. Grabs attributes from card class
    Display_Card1 = player1_card.get_face_value()
    Display_Card2 = player2_card.get_face_value()

    # Shows who drew what and declares the winner
    print(player1, "drew a", Display_Card1, sep=' ')
    print(player2, "drew a", Display_Card2, sep=' ')
    print('\n')
    if player1_card.get_value() < player2_card.get_value():
        print(Display_Card1, " is lower than ", Display_Card2,"!", sep='')
        print(player2, " wins!\n", sep='')
    elif player1_card.get_value() > player2_card.get_value():
        print(Display_Card1, "is higher than ", Display_Card2,"!", sep='')
        print(player1, " wins!\n", sep='')
    else:
        print("The cards are the same!\nIts a tie!\n")
        
    print('___________________________________________________')
    print('\n\n')
    


# Function: Deal Hand
# Input: None
# Output: None
# Purpose: Generates 5 random cards form display face value. Also added a point system for the value of the hand.
#           *Uses the module card_Allen*
def deal_hand():
    print('\n')
    # Creates an empty list
    hand = []

    # Creates a loop to deal 5 cards
    for deal_card in range(5):
        # Creates an object for card class
        card = card_Allen.Card()
        # Generates a random value for card
        card.deal()
        # Attaches obj values to spot in list
        hand.append(card)

    # Displays cards face values
    print(display_hand(hand))

    # Creates values from hand stats function
    total_points, average = hand_stats(hand)

    print("The value of these cards are ", total_points, ". \nThat averages each card to be ", average, '.', sep='')
    print('___________________________________________________')
    print('\n\n')


# Function: Display Hand
# Inputs: hand reprsents the list generated from the Deal Hand function where we are tryong to get random values
# Output: returns the hand valueas as a list of strings 
# Purpose: Individually gets a random integer from the display. *Uses the module card_Allen*
def display_hand(hand):
    # Creates an empty string
    disp_hand = []

    # Loops through hand and adds the face value to a list
    for test in hand:
        disp_hand.append(test.get_face_value())
    
    return disp_hand
        


# Function: Hand Stats
# Input: hand represents the 5 cards from the deal hand function
# Output returns both total and average of the value of cards.
# Purpose: Purpose is to take the value of cards, average the the values or return the total. *Uses the module card_Allen*
def hand_stats(stat_hand):
    # Assigns empty variable to 0
    total = 0

    # Loops through and adds the value to total
    for stat in stat_hand:
        total += stat.get_value()

    # Gets the average of values
    average = total/5
    return total, average



# Function: Save Dream Hand
# Input: None
# Output: None
# Purpose: User inputs a value for each 5 cards in this function. Those 5 cards will be saved to a file. *Uses the module card_Allen*
def save_dream_hand():
    print('\n')

    # Creates an empty list
    hand = []

    # User creates file neam
    file_name = input('Save file name as: ')

    # File is open for writing
    cards_file = open(file_name + '.txt', 'w')
    


    # Added an exception to handle Value Errors
    try:
        # Loops 5 times
        for x in range(5):
            card = card_Allen.Card()

            in_card = int(input("Give the number value for the card. input(1 - 13: "))

            # Loops if integer is not withing 1 through 13
            while in_card < 1 or in_card > 13:
                print("Invalid card! Card must be between 1 and 13.")
                in_card = int(input("Give the number value for the card. input(1 - 13: "))

            # Assign the value in object
            card.set_value(in_card)

            # Holds variable for card input in a list
            hand.append(card)

        # Loops through list and inserts card variables into file
        for line in hand:
            cards_file.write(str(line.get_value()) + '\n')

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
# Purpose: This function gathers data from file created and post it's contents for the user to understand. *Uses the module card_Allen*
def display_dream_hand():
    print('\n')

    # Creates an object for card
    card = card_Allen.Card()

    # Input File name
    file = input("Enter file name:\t")

    # Creates empty list for face values
    Card_Names = []
    
    #Opens file
    cards_file = open(file + '.txt', 'r')

    print("Here are your dream cards:   ")
    
    # Saves readlines to cards
    cards = cards_file.readlines()

    index = 0

    # Reads file by line and inserts each value int a List
    while index < len(cards):
        cards[index] = int(cards[index].rstrip('\n'))
        index += 1

    # Loops through and adds the face value to a list to display
    for name in cards:
        card.set_value(name)
        Card_Names.append(card.get_face_value())

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

    # Input for a word
    word = input("Please enter a word for the WORD GUESS game:\t")

    #Places all characters guessed here to search later
    guesses_used = ''

    # Displays word using '*'
    word_disp = '*' * len(word)

    print('\n'*100)

    # Loops until word is guessed
    while word_disp != word:
        
        print('So far you have:\n\t', word_disp)
        char = input("Enter a character to guess:\t")

        # Checks if letter was used
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
    

        


    
               

