
# Global Variables

menu = ["Show all contacts","Add new contact","Find contact","Delete contact","Quit"] # Contains the menu options that the user gets to see
contactInfo = ["name","surname","DOB","mobileNum","locality"] # Contains the contact informaton to be used as keys for the dictionaries inside the contacts list
contacts = [] # Empty list

filename = "myContacts.csv" # Stores file names

# Functions

def displayMenu():
    '''Displays the menu for the user item by item by using the enumerate
       built in function to display a number near each item for the user to choose from.'''
    print("---------------")
    print("-  MAIN MENU  -")
    print("---------------")
    for num,item in enumerate(menu, start = 1): # Adds a number near each item displayed to the user.
        print(num,"-",item) # Prints the option number near the item.
    print() # Prints an empty line for space
    choice = input("Enter your choice: ") # Stores user's choice
    return choice # Returns user's choice to the main code

def loadContacts(filename):
    '''This function attempts to open the csv file to get the data saved onto it and stores
        the saved contacts inside the contacts list. If the function is unable to find the file,
        it would create an empty list as it can't load in data from the csv since it can't be found.'''
     
    try: # Checks if this line of code can be run or not depending the error
        fo = open(filename) # Opens the csv file

    except(FileNotFoundError): # Checks for any file not found errors if it's not able to open the file
       contacts = [] # Empty list as file can't be found so the data inside the file can't be loaded in
        
    else: # Runs if an error doesn't pop up
        global contacts # Refers to the global variable outside of the function so it can be used
        for item in fo: 
            tempList = item.strip().split(",") # The list stores the values from a single row
            loadCon = dict(zip(contactInfo,tempList)) # Saves the values from a single row into a dictionary
            contacts.append(loadCon) # Adds the dicionary to the contacts list
##        print(contacts) # For testing purposes
        fo.close() # Closes the csv file

def saveContacts(filename):
    '''This function saves all of the data inside the dictionaries in the contacts list into
        the csv file by storing all of the data inside each key of a dictionary inside a string, 
        which are seperated by commas except for the last key from the dictionary. This function then
        returns a True boolean value to tell the program to stop. '''

    print("Saving and exiting program...")
    try: # Checks if this line of code can be run or not depending the error
        fo = open(filename, 'w') # Opens the file
    except(PermissionError): # Checks for any permission errors when trying to open the file
        print("The file "+filename+" is read only.")
        userOpt = input("Are you sure you want to quit without saving any changes (Y/N)? ") # Stores the user's choice
        if(userOpt == "y" or userOpt == "Y"): # Checks if user still wanted to quit after telling them their changes won't save through the previous message
            return True # Returns True for the program to stop
    else: # Runs if an error doesn't pop up
        for x in range(len(contacts)): # Loops by the amount of contacts there are in the list
             saveList = [contacts[x]["name"],contacts[x]["surname"],contacts[x]["DOB"],contacts[x]["mobileNum"],contacts[x]["locality"]] # Stores a single contact in a list

             saveCon = "" # String variable initialisation

             for num,i in enumerate(saveList, start = 1): # i stores data one by one from the list after the it runs the code below. num keeps note of how many times the loop has been repeated.
                 if(num != 5): # Checks if the number of times the loop was repeated isn't 5
                     saveCon += i+"," # Stores whatever is inside the variable with what is inside of i as a string and adds a comma at the end so it can be stored for the csv file
                 else: # If the number of times repeated doesn't match the criteria of the if statement 
                    saveCon += i # Stores what is inside of i into the string but doesn't add the coma since it's supposed to be the last contact data saved
                    
             saveCon += "\n" # The \n is used so it can create a new row inside the csv file
             fo.write(saveCon) # Writes the variable into the csv file

        fo.close() # Closes the csv file
        return True # Returns True for the program to stop
    
def showAllContacts():
    '''This function displays all of the contacts inside the contacts list to the user by
        looping by the amount of contacts there are and for each contact specifically selectiing
        the data of related contact and printing it to the user appropriately.'''
    for x in range(len(contacts)): # It loops by the number of contacts there are in the list
        print(contactInfo[0],":",contacts[x]["name"])
        print(contactInfo[1],":",contacts[x]["surname"])
        print(contactInfo[2],":",contacts[x]["DOB"])
        print(contactInfo[3],":",contacts[x]["mobileNum"])
        print(contactInfo[4],":",contacts[x]["locality"],"\n")

def addNewContact():
    '''  '''
    userName = input("Enter name: ")
    userSurNa = input("Enter surname: ")
    userDOB = input("Enter Date Of Birth: ")
    userMobNo = input("Enter Monile Number: ")
    userLoc = input("Enter Locality: ")

    userList = [userName,userSurNa,userDOB,userMobNo,userLoc] # Stores the users' input for a new contact
    
    addCon = dict(zip(contactInfo, userList)) # Turns the data into a dictionary

    contacts.append(addCon) # Adds the dictionary of the new contact into the contacts list

def findContactsByName(name):
    '''This function looks for the contact by the name that user has entered. It does this
        through a loop which appends all of the contact names that match the names entered
        into a list then returning that list so it can be used for another fucntion. If the
        name doesn't match with any name in contacts list, it displays the appropriate message.'''
    findList = [] # Empty list

    for x in range(len(contacts)): # It loops by the number of contacts there are in the list
        if(name.title() == contacts[x]["name"].title()): #Checks if the name entered by the user matches any name from the list
            findList.append(contacts[x]) # Adds the contacts to the list
            
    if(len(findList) == 0): # Checks if the list is empty so it can display the appropriate message
        print("No contacts were found with the name",name)
    return findList # Returns the list that contains all of the contacts found

def displayContactByName(name):
    '''This function displays all of the contacts that match with the name the user has
        entered to the function. It does this by looping by the amount of users that match
        the name entered and displaying the relevant data connected to the user appropriately.
        If there's no users in the list, this function would only return the same list for the next function.'''
    disList = findContactsByName(name)# Stores the list from the findContacts function into a list in this fuction
    if(len(disList) > 0): # Checks if the list if empty or not
        print() # Prints out an extra space
        for x in range(len(disList)): # It loops by the number of contacts there are in the list
            print(contactInfo[0],":",disList[x]["name"])
            print(contactInfo[1],":",disList[x]["surname"])
            print(contactInfo[2],":",disList[x]["DOB"])
            print(contactInfo[3],":",disList[x]["mobileNum"])
            print(contactInfo[4],":",disList[x]["locality"],"\n")

        print(len(disList),"contacts found.") # Prints the amount of contacts found

    return disList # Returns the list that contains all of the contacts displayed

def deleteContactByName(name):
    '''This function deletes the contacts that match with the name the user has
        entered to the function.'''
    delList = len(displayContactByName(name)) # Stores the length of the list of the contacts displayed
    storeCon = [] # Empty List
    global contacts # Refers to the global variable outside of the function so it can be used
    
    if(delList > 0): # Checks if the list if empty or not
        print("Are you sure you want to remove the above",delList,"contacts (Y/N)? ",end="")
        userAns = input() # Stores user's choice
        if(userAns == "y" or userAns == "Y"): # If the user chose yes
            for x in range(len(contacts)): 
                if(name.title() != contacts[x]["name"].title()): # Checks if the name doesn't match
                    storeCon.append(contacts[x]) # Stores the contacts that doe't match with the name into the list
            contacts = storeCon # Stores the list that doesn't have the contact which the user didn't want into the contacts list
            print("Contacts removed.")
        elif(userAns == "n" or userAns == "N"): # If the user chose no
            print("No contacts were removed.")
        
# Main Code
        
loadContacts(filename)
while True: # Loops until a break function is used
    choice = displayMenu() # Displays menu and stores the user's choice
    if(choice == "1"):
##        print("Item 1 was selected: Show all contacts\n") # Testing purposes
        showAllContacts()
    elif(choice == "2"):
##        print("Item 2 was selected: Add new contact\n") # Testing purposes
        addNewContact()
    elif(choice == "3"):
##        print("Item 3 was selected: Find contact\n") # Testing purposes
        findName = input("Enter the name of a contact to find: ") # Stores the name of the contact the user wants to find
        displayContactByName(findName)
    elif(choice == "4"):
##        print("Item 4 was selected: Delete contacts\n") #T esting purposes
        delName = input("Enter the name of a contact to delete: ") # Stores the name of the contact the user wants to delete
        deleteContactByName(delName)
    elif(choice == "5"):
        userOpt = saveContacts(filename) # Runs the saveContacts function and also stores if the user wanted to end the program
        if(userOpt == True): # Checks if the user wanted to quit the program.
            break # Breaks the loop if true
    else:
        print("Please enter a number between 1 and 5") # Tells the user to enter a number between 1-5
