menu = ["Show all contacts","Add new contact","Find contact","Delete contact","Quit"]
choice = ""

def displayMenu():
    print("---------------")
    print("-  MAIN MENU  -")
    print("---------------")
    for num,item in enumerate(menu, start = 1):
        print(num,"-",item)
    print()
    choice = input("Enter your choice: ")
    return choice

# Main Code

while choice != '5':
    choice = displayMenu()
    if(choice == "1"):
        print("Item 1 was selected: Show all contacts")
    elif(choice == "2"):
        print("Item 2 was selected: Add new contact")
    elif(choice == "3"):
        print("Item 3 was selected: Find contact")
    elif(choice == "4"):
        print("Item 4 was selected: Delete contacts")
    elif(choice == "5"):
        print("Exiting Program...")
    else:
        print("Please enter a number between 1 and 5")
