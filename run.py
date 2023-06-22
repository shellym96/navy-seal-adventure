#print a welcome message
print("Welcome to your Navy Seal Adventure!")

print("Choose one of the two options:")
option = input("Press 'i' for instructions or 's' to start the game.")

if (option == "i"):
    print("Here is your instructions")

elif (option == "s"): 
    print("The game is beginning... \n")
    name = input("Enter your name here: \n")
    print("Hello, " + name + " let's begin \n")
    print("You're being sent for deployment to Afghanistan. Do you leave you're family and risk your life? Y/N \n")

    choice = input("")

    if(choice == "y"):
        print("Congratulations, you've been offered to be a Commanding Officer of this mission. Do you accept this position? Y/N \n")

    elif(choice == "n"):
        print("You have been discharged for not following orders. Return to the home page with the option to play again. \n ")

    else: 
        print("Invaild option. Please answer questions with y or n only.\n")
