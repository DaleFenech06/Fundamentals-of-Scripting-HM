
menu = ["Show all contacts","Add new contact","Find contact","Delete contact","Quit"]
contacts = []
choice = ""

filename = "myContacts.csv"


def displayMenu():
    print("---------------")
    print("-  MAIN MENU  -")
    print("---------------")
    for num,item in enumerate(menu, start = 1):
        print(num,"-",item)
    choice = input("Enter your choice: ")
    return choice


def loadContacts():
    fo = open(filename)
    
    for item in fo:
        tempList = item.strip().split(",")
        contact = {
          "name": tempList[0],
          "surname": tempList[1],
          "DOB": tempList[2],
          "mobileNum": tempList[3],
          "locality": tempList[4]
        }
        contacts.append(contact)
        print(contacts)

    fo.close()

def saveContacts():
    fo = open(filename, 'w')
    saveCon = ""
    for x in range(len(contacts)):
         saveList = [contacts[x]["name"],contacts[x]["surname"],contacts[x]["DOB"],contacts[x]["mobileNum"],contacts[x]["locality"]]

         saveCon = ""

         for num,i in enumerate(saveList, start = 1):
             if(num != 5):
                 saveCon += i+","
             else:
                 saveCon += i
                 
         saveCon += "\n"
         fo.write(saveCon)

    fo.close()

# Main Code
        
loadContacts()
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
        saveContacts()
        print("Saving and exiting program...")
    else:
        print("Please enter a number between 1 and 5")
