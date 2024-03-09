# Leonard Allen
# Lab 03
# Lame Game
# An unfinished gaming room. The only thing that can be done with this program is
# that you can input information to be held for a later time.
#
#




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
    print(change_amount)
    quarters = change_amount / .25
    change_amount = change_amount % .25
    print(change_amount)
    dimes = change_amount / .10
    change_amount = change_amount % .10
    print(change_amount)
    nickels = change_amount / .05
    change_amount = change_amount % .05
    print(change_amount)
    pennies = change_amount / .01

# Printing the solutions
   
    if dollars > 0:
        print("dollars: ", format(dollars, '5.0f'))
    if quarters > 0:
        print("quarters: ", format(quarters, '1.0f')) 
    if dimes > 0:
        print("dimes: ", format(dimes, '1.0f'))
    if nickels > 0:
        print("nickels: ", format(nickels,'1.0f'))
    if pennies > 0:
        print("pennies: ", format(pennies, '1.0f'))

# Other options are not availble quite yet
elif option == 2:
    print("High Card is coming soon!")
    
elif option == 3:
    print()
    
else:
    print("Invalid Option")

