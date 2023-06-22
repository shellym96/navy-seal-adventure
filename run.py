#print a welcome message
print("Welcome to your Navy Seal Adventure!")

print("Choose one of the two options:")
option = input("Press 'i' for instructions or 's' to start the game.")

if (option == "i"):
    print("Here is your instructions")

elif (option == "s"): 
    print("The game is beginning... \n")
    name = input("Enter your name here: \n")
    print("Hello", name "let's begin \n")

else: 
    print("Invaild option. \n")
