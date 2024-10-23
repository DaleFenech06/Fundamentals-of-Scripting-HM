
menu = ["Show all contacts","Add new contact","Find contact","Delete contact","Quit"]
contactInfo = ["name","surname","DOB","mobileNum","locality"]
contacts = []
choice = ""

filename = "myContacts.csv"

def displayMenu():
    '''Displays the menu item by item '''
    print("---------------")
    print("-  MAIN MENU  -")
    print("---------------")
    for num,item in enumerate(menu, start = 1):
        print(num,"-",item)
    print()
    choice = input("Enter your choice: ")
    return choice

def loadContacts(): 
    fo = open(filename)

    for item in fo:
        tempList = item.strip().split(",")
        loadCon = dict(zip(contactInfo,tempList))
        contacts.append(loadCon)
        print(contacts) #Testing purposes

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
    
def showAllContacts():
    for x in range(len(contacts)):
        print("name :",contacts[x]["name"])
        print("surname :",contacts[x]["surname"])
        print("DOB :",contacts[x]["DOB"])
        print("mobileNum :",contacts[x]["mobileNum"])
        print("locality :",contacts[x]["locality"],"\n")

def addNewContact():
    userName = input("Enter name: ")
    userSurNa = input("Enter surname: ")
    userDOB = input("Enter Date Of Birth: ")
    userMobNo = input("Enter Monile Number: ")
    userLoc = input("Enter Locality: ")

    userList = [userName,userSurNa,userDOB,userMobNo,userLoc]
    
    addCon = dict(zip(contactInfo, userList))

    contacts.append(addCon) 

def findContactsByName(name): 

    findList = [] 

    for x in range(len(contacts)): 
        if(name == contacts[x]["name"]): 
            findList.append(contacts[x]) 
            
    if(len(findList) == 0):
        print("No contacts were found with the name",name)
    return findList

def displayContactByName(name):

    disList = findContactsByName(name)
    if(len(disList) > 0):
        print()
        for x in range(len(disList)):
            print("name :",disList[x]["name"])
            print("surname :",disList[x]["surname"])
            print("DOB :",disList[x]["DOB"])
            print("mobileNum :",disList[x]["mobileNum"])
            print("locality :",disList[x]["locality"],"\n")

        print(len(disList),"contacts found.")

    return disList

def deleteContactByName(name):

    delList = len(displayContactByName(name))
    storeCon = []
    global contacts
    
    if(delList > 0):
        print("Are you sure you want to remove the above",delList,"contacts (Y/N)? ",end="")
        userAns = input()
        if(userAns == "y"):
            for x in range(len(contacts)):
                if(name != contacts[x]["name"]):
                    storeCon.append(contacts[x])
            contacts = storeCon
            print("Contacts removed.")
        elif(userAns == "n"):
            print("No contacts were removed.")
        
#Main Code
        
loadContacts()
while choice != 5:
    choice = displayMenu()
    if(choice == "1"):
        print("Item 1 was selected: Show all contacts\n")
        showAllContacts()
    elif(choice == "2"):
        print("Item 2 was selected: Add new contact\n")
        addNewContact()
    elif(choice == "3"):
        print("Item 3 was selected: Find contact\n")
        findName = input("Enter the name of a contact to find: ")
        displayContactByName(findName)
    elif(choice == "4"):
        print("Item 4 was selected: Delete contacts\n")
        delName = input("Enter the name of a contact to delete: ")
        deleteContactByName(delName)
    elif(choice == "5"):
        saveContacts()
        print("Saving and exiting program...")
    else:
        print("Please enter a number between 1 and 5")
