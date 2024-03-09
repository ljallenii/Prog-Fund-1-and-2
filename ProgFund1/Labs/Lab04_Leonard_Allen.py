# Leonard Allen
# Lab 03
# Lame Game
# This program will output a menu for the user to choose from. 1 - Make Change | 2 - High Card | 3 - Quit 
# *Make Change* is accessible. Enter in the amount a custome owes and the amount they pay to get the amount of change they will get back.
# *High Card has* been added. The users inputs there names and draws a card. The highest value card wins.
# *Quit* is now assigned a boolean value True until option is chosen.


import random

# Prints welcome message
print("""Welcome user, \nto the LAME GAME gaming room. The room is currently under """)
print("""construction, so currently only have a few options for you to select from.""")
print("""Please stay tuned, we plan on sendiing updates every week. Thank you!\n""")

# printing the menu
print("MENU:\n\t1. Make Change\n\t2. High Card\n\t3. Quit\n")

# User must make a decision
option = int(input("Please choose an option (1, 2, or 3) to contiue: "))

# Checks for valid option
while option != 1 and option != 2 and option != 3:
    print("Invalid Option")
    option = int(input("Please choose an option (1, 2, or 3) to contiue: "))
    
# GameState decides if we continue playing
Game_State = True

while Game_State:
    # Option 1
    if option == 1:
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


    # Other options are not availble quite yet
    elif option == 2:

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
            
    # Loops again unless user inputs '3' to quit. Also checks to make sure a valid option is chosen
    print("MENU:\n\t1. Make Change\n\t2. High Card\n\t3. Quit\n")
    option = int(input("Please choose an option (1, 2, or 3) to contiue: "))       
    while option != 1 and option != 2 and option != 3:
        print("Invalid Option")
        option = int(input("Please choose an option (1, 2, or 3) to contiue: "))           
    
    if option == 3:
        Game_State = False


