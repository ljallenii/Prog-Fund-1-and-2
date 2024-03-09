# Leonard Allen
# Lab 02
# Lame Game
# An unfinished gaming room. The only thing that can be done with this program is
# that you can input information to be held for a later time.


# Prints welcome message
print("""Welcome user, \nto the LAME GAME gaming room. The room is currently under """)
print("""construction, so currently only have a few options for you to select from.""")
print("""Please stay tuned, we plan on sendiing updates every week. Thank you!\n""")

# Takes the user's name and sores it for later use
name = input("Please give us your name ")
print("Welcome,", name + '!\n')

# printing the menu
print("MENU:\n\t1. Make Change\n\t2. High Card\n\t3. Quit\n")

# User must make a decision
option = input(name + ", please choose an option (1, 2, or 3) to contiue: ")

# Prints the user's name and the selected option
print(name + ", you have chose option " + option)
