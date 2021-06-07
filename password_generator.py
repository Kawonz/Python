import random
import string

ALPHABET = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = string.punctuation

def main():
    print("Password Generator:")
    print(" -------------------")
    print("Please type the input in the follow order with SPACES separarting each number or letter.")
    print("[Password length] [Letters? Y/N] [Numbers? Y/N] [Symbols? Y/N]")
    print("[Ex: 5 Y Y Y]")
    print("*Please note that Y means 'Yes' and N means 'No'*")
    userInput = input()
    global newUserInput
    newUserInput = userInput.split(" ")

    if len(newUserInput) == 4:
        print("Your Generatored Password is....")
        global savedPassword
        savedPassword = generatePassword()
        print(savedPassword+ "\n")
        savePasswordToFile()

    else:
        print("Invalid Input.\n")
        main()
        
def generatePassword():
    global newUserInput
    passContent = ""

    #Generates password with Letters, Numbers, and Symbols
    if newUserInput[1] == "Y" and newUserInput[2] == "Y" and newUserInput[3] == "Y":
        for i in range(int(newUserInput[0])):
            passContent += random.choice(ALPHABET+NUMBERS+SYMBOLS)
            
    #Generates password with ONLY Letters
    elif newUserInput[1] == "Y" and newUserInput[2] == "N" and newUserInput[3] == "N":
        for i in range(int(newUserInput[0])):
            passContent += random.choice(ALPHABET)

    #Generates password with ONLY Numbers
    elif newUserInput[1] == "N" and newUserInput[2] == "Y" and newUserInput[3] == "N":
        for i in range(int(newUserInput[0])):
            passContent += random.choice(NUMBERS)

    #Generates password with ONLY Symbols
    elif newUserInput[1] == "N" and newUserInput[2] == "N" and newUserInput[3] == "Y":
        for i in range(int(newUserInput[0])):
            passContent += random.choice(SYMBOLS)

    #Generates password with ONLY Letters and Numbers
    elif newUserInput[1] == "Y" and newUserInput[2] == "Y" and newUserInput[3] == "N":
        for i in range(int(newUserInput[0])):
            passContent += random.choice(ALPHABET+NUMBERS)

    #Generates password with ONLY Letters and Symbols
    elif newUserInput[1] == "Y" and newUserInput[2] == "N" and newUserInput[3] == "Y":
         for i in range(int(newUserInput[0])):
            passContent += random.choice(ALPHABET+SYMBOLS)

    #Generates password with ONLY Numbers and Symbols
    elif newUserInput[1] == "N" and newUserInput[2] == "Y" and newUserInput[3] == "Y":
         for i in range(int(newUserInput[0])):
            passContent += random.choice(NUMBERS+SYMBOLS)

    #No password Criteria
    elif newUserInput[1] == "N" and newUserInput[2] == "N" and newUserInput[3] == "N":
        print("That password cannot be made.")

    else:
        print("Invalid input")
            
    return passContent


def savePasswordToFile(fileName="PasswordFile.txt"):
    savingUserInput = input("Would you like to save this password to a file? [Y/N]")
    if savingUserInput == "Y":
        nameOfFileUserInput = input("Please type the use of the file and the file name separated by a colon. For example: Facebook:mypass.txt\n")
        separatedUserInput = nameOfFileUserInput.split(":")
        if len(separatedUserInput) == 2:
            fileName = separatedUserInput[1]
        fin = open(fileName, "w")
        print("file created")
        fin.write(f"{separatedUserInput[0]}: {savedPassword}")
        fin.close()
        return separatedUserInput
        
    elif savingUserInput == "N":
        print("Your password was not saved.\n")
        main()
    else:
        print("Your password was not saved due to invalid input.\n")
        main()


if __name__ == "__main__":
    main()
    
