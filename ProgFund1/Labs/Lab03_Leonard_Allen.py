# Leonard Allen
# Lab 03
# Lame Game
# An unfinished gaming room.
# Make Change is now accessible. Enter in the amount a custome owes and the amount they pay
# to get the amount of change they will get back.


# printing the menu
print("MENU:\n\t1. Make Change\n\t2. High Card\n\t3. Quit\n")

# User must make a decision
option = int(input("Please choose an option (1, 2, or 3) to contiue: "))

# Option 1
if option == 1:
    print("""\nPlaying the "Make Change" game\n""")

# Input the money owed and money given
    money_owed = float(input("How much money will the customer pay?  "))
    money_given = float(input("How much money did the customer give?  "))
    change_amount = money_given - money_owed
    print("$", format(change_amount,'.2f'), sep='')

# Dummy is a place holder for the integer amount of change_amount 
    dummy = int(change_amount)

# Algorithms presented to find the change amount
    dollars = dummy / 1


    change_amount = change_amount - dummy
    quarters = change_amount / .25
    change_amount = change_amount % .25
    dimes = change_amount / .10
    change_amount = change_amount % .10
    nickels = change_amount / .05
    change_amount = change_amount % .05
    pennies = change_amount / .01

# Printing the solutions
   
    if dollars >= 1:
        print("dollars: ", int(dollars))
    if quarters >= 1:
        print("quarters: ", int(quarters))
    if dimes >= 1:
        print("dimes: ", int(dimes))
    if nickels >= 0:
        print("nickels: ", int(nickels))
    if pennies >= 0:
# Had to add a penny for now because the divison would be off by .0000001 and it would round down
        print("pennies: ", int(pennies)+1)

# Other options are not availble quite yet
elif option == 2:
    print("High Card is coming soon!")
    
elif option == 3:
    print()
    
else:
    print("Invalid Option")

