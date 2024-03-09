# Leonard Allen
# Lab 03
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

def welcome():
    # Prints welcome message

    print("#############################################################################")
    print("###^^##############^########^^#######^^#^^^^^^^^^############################")
    print("###^^#############^^^#######^^^#####^^^#^^###################################")
    print("###^^############^^#^^######^^^^###^^^^#^^###################################")
    print("###^^###########^^###^^#####^^#^^#^^#^^#^^^^^^###############################")
    print("###^^##########^^#####^^####^^##^^^##^^#^^###################################")
    print("###^^#########^^^^^^^^^^^###^^#######^^#^^###################################")
    print("###^^########^^#########^^##^^#######^^#^^###################################")
    print("###^^^^^^^^#^^###########^^#^^#######^^#^^^^^^^^^############################")
    print("#############################################################################")
    print("###############################^^^^^##########^########^^#######^^#^^^^^^^^^#")
    print("##############################^^###^^########^^^#######^^^#####^^^#^^########")
    print("#############################^^#####^^######^^#^^######^^^^###^^^^#^^########")
    print("#############################^^############^^###^^#####^^#^^#^^#^^#^^^^^^####")
    print("#############################^^###^^^^####^^#####^^####^^##^^^##^^#^^########")
    print("#############################^^#####^^###^^^^^^^^^^^###^^#######^^#^^########")
    print("##############################^^###^^###^^#########^^##^^#######^^#^^########")
    print("###############################^^^^^###^^###########^^#^^#######^^#^^^^^^^^^#")
    print("#############################################################################")
    
    
    print("""Welcome user, \nto the LAME GAME gaming room. The room is currently under """)
    print("""construction, so currently only have a few options for you to select from.""")
    print("""Please stay tuned, we plan on sendiing updates every week. Thank you!\n""")
    print("""New games have been added recently! Give our newest game 'Deal Hand' a go!\n\n""")

# All functions are called here. Add new game options here.
def main():

    # GameState decides if we continue playing.
    Game_State = True
    
    while Game_State:
        option = menu()
        
        if option == 1:
            MakeChange()

        elif option == 2:
            HighCard()

        elif option == 3:
            DealHand()
        
        elif option == 4:
            file = SaveDreamHand()

        elif option == 5:
            DisplayDreamHand(file)

        elif option == 6:
            Game_State = Quit()

        
            

# Displays the menu. Also checks if user inputs a valid option.
def menu():
    # printing the menu
    print("MENU:\n\t1. Make Change\n\t2. High Card\n\t3. Deal Hand\n\t4. Save Dream Hand\n\t5. Display Dream Hand\n\t6. Quit\n")

    # User must make a  "VALID" decision
    try:
        option = int(input("Please choose an option (1, 2, 3, 4, 5, or 6) to contiue: "))

    # If there is an error with the input, this message will be displayed.
    except:
        print("ERROR! The value used is not valid.")

    # Checks for valid option
    while option < 1 and option > 6:
        print("Invalid Option")
        option = int(input("Please choose an option (1, 2, 3, 4, 5, or 6) to contiue: "))

    print()
    return option
        
        
# Make Change Function
def MakeChange():
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
        print()


#High Card function
def HighCard():
    # Other options are not availble quite yet
    

        #Player names
        player1 = input("Enter a name for player 1:\t")
        player2 = input("Enter a name for player 2:\t")
        print()

        # Imported Random function to get random number Generator
        card1 = random.randint(1,13)
        card2 = random.randint(1,13)

        
        # Assigns cards to displayable values for the user
        if card1 == 1:
            D_card1 = "Ace"
        elif card1 == 2:
            D_Card1 = "Two"
        elif card1 == 3:
            D_card1 = "Three"
        elif card1 == 4:
            D_card1 = "Four"
        elif card1 == 5:
            D_card1 = "Five"
        elif card1 == 6:
            D_card1 = "Six"
        elif card1 == 7:
            D_card1 = "Seven"
        elif card1 == 8:
            D_card1 = "Eight"
        elif card1 == 9:
            D_card1 = "Nine"
        elif card1 == 10:
            D_card1 = "Ten"
        elif card1 == 11:
            D_card1 = "Jack"
        elif card1 == 12:
            D_card1 = "Queen"
        else:
            D_card1 = "King"

        if card2 == 1:
            D_card2 = "Ace"
        elif card2 == 2:
            D_Card2 = "Two"
        elif card2 == 3:
            D_card2 = "Three"
        elif card2 == 4:
            D_card2 = "Four"
        elif card2 == 5:
            D_card2 = "Five"
        elif card2 == 6:
            D_card2 = "Six"
        elif card2 == 7:
            D_card2 = "Seven"
        elif card2 == 8:
            D_card2 = "Eight"
        elif card2 == 9:
            D_card2 = "Nine"
        elif card2 == 10:
            D_card2 = "Ten"
        elif card2 == 11:
            D_card2 = "Jack"
        elif card2 == 12:
            D_card2 = "Queen"
        else:
            D_card2  = "King"

        # Shows who drew what and declares the winner
        print(player1, "drew a", D_card1, sep=' ')
        print(player2, "drew a", D_card2, sep=' ')
        print()
        if card1 < card2:
            print(D_card1, " is lower than ", D_card2,"!", sep='')
            print(player2, " wins!\n", sep='')
        elif card1 > card2:
            print(D_card1, "is higher than", D_card2,"!", sep='')
            print(player1, " wins!\n", sep='')
        else:
            print("The cards are the same!\nIts a tie!\n")

# Displays the card value that the user has.
def display_face_value(card_val = 0, randomize = True):
    
    # Added randomizer algorithm if Deal Hand function is ran
    if randomize == True:
        card1 = random.randint(1,13)
    # Randomizer is set to false for Display Hand function
    else:
        card1 = card_val

    if card1 == 1:
        return "Ace"
    elif card1 == 2:
        return "Two"
    elif card1 == 3:
        return "Three"
    elif card1 == 4:
        return "Four"
    elif card1 == 5:
        return "Five"
    elif card1 == 6:
        return "Six"
    elif card1 == 7:
        return "Seven"
    elif card1 == 8:
        return "Eight"
    elif card1 == 9:
        return "Nine"
    elif card1 == 10:
        return "Ten"
    elif card1 == 11:
        return "Jack"
    elif card1 == 12:
        return "Queen"
    else:
        return "King"


# Deal Hand Function
def DealHand():


    Hand = [card1, card2, card3, card4, card5]
    Hand = display_hand(Hand)

    # Ask about this before submitting -->
    total_points, average = hand_stats(Hand)

    print("The value of these cards are ", total_points, ". \nThat averages each card to be ", average)

def display_hand(hand):
    display_face_value(hand[0])
    display_face_value(hand[1])
    display_face_value(hand[2])
    display_face_value(hand[3])
    display_face_value(hand[4])

    return hand


def hand_stats(hand):
    for x in range(hand):
        total += x
    average = total/5
    return total, average
    

    # print("You are currently holding " + card1, card2, card3, card4, "and " + card5, sep=', ')


# Stops programing by changing the while True statement to False.
def Quit():
    return False


# User inputs a value for each 5 cards in this function
def SaveDreamHand():
    hand = ''

    # User inputs 5 cards
    for x in range(5):

        # Added an exception to handle Value Errors
        try:
            card = str(input("Give the number value for the card OR enter 'stop' to complete input(1 - 13: "))

        except ValueError:
            print("ERROR! String characters aren't allowed. Please input a number as followed.")
        # Holds variable for card input
        hand = hand + card + '\n'

        
    # User creates file neam
    file_name = input('Save file name as: ')

    # File is open for writing
    cards_file = open(file_name + '.txt', 'w')

    #file inserts card variables
    cards_file.write(hand)

    # File is then closed
    cards_file.close()
    
    # Return file name for later use when reading contents
    return file_name


# This function gathers data from file created and post it's contents for the user to understand.
def DisplayDreamHand(file):   

    #Opens file
    cards_file = open(file + '.txt', 'r')

    print("Here are your dream cards:   ")

    # Loops the data of each line and displays data.
    for cards in cards_file:
        card_val = int(cards)

        # Disables the random number generator for this function.
        randomize = False
        print("\t" + display_face_value(card_val, randomize))

    # Closes file
    cards_file.close()
       
    print()
    print("**************************************************")

    
import random

# Calls the program to start.
welcome()

main()
    

        


    
               

