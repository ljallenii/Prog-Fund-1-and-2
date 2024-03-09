# Leonard Allen

def greeting():
    print("""*** IMPORTANT ***""")
    print("""I wasn;t sure if you wanted to just display the txt file, add to the text file, or create a whole new text file so I did all three just in case. \n\n""")
    print("Welcome to the gift shop! Here you can create, add to, or read off on our items. ")

def main():
    try:
        option = int(menu())
        if option == 1:
            display_inventory()

        elif option == 2:
            add_inventory()

        elif option == 3:
            decide = input("\n WARNING! This will erase previous data on the Exam2.txt file. \nWould you like to continue?(y/n)")
            if decide == 'y':
                New_inventory()
            elif decide == 'n':
                main()
        elif option == 4:
            print("End of program")

    except:
        print("ERROR! Something was wrong with your input!")


    

def menu():
    print("""Please select from our menu to continue:\n\t1.\tDisplay current inventory\n\t2.\tAdd to inventory\n\t3.\tCreate new inventory\n\t4.\tQuit\n""")
    option = input("\t Choice: ")
    return option

    

def display_inventory():
    Inventory = open('Exam2.txt', 'r')

    item = Inventory.readline()

    while item != '':
        quant = Inventory.readline()
        price = Inventory.readline()

        item = item.rstrip('\n')
        quant = quant.rstrip('\n')
        price = price.rstrip('\n')

        total = value(quant,price)

        print("Item Name: ", item)
        print("Quantity in inventory: ", quant)
        print("Item Price: ", price)
        print("Value: ", format(total, '.2f'))
        print()
        
        item = Inventory.readline()

    Inventory.close()

    main()

def value(quant, price):
    return float(price) * int(quant)    

def add_items():
    item = input("Item name: ")
    quant = input("Number of items: ")
    price = input("Item price: ")

    return item, quant, price


def add_inventory():
    Inventory = open('Exam2.txt', 'a')

    while item != '':
        item, quant, price = add_items()
        print("To stop, leave item blank.")
        
        Inventory.write(item + '\n')
        Inventory.write(quant + '\n')
        Inventory.write(price + '\n')   

    Inventory.close()

    main()

def New_inventory():
    Inventory = open('Exam2.txt', 'w')

    while item != '':
        item, quant, price = add_items()
        print("To stop, leave item blank.")
        
        Inventory.write(item + '\n')
        Inventory.write(quant + '\n')
        Inventory.write(price + '\n')   

    Inventory.close()

    main()

    

greeting()       
main()
            



