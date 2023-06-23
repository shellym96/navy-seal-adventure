"""
#print a welcome message
print("Welcome to your Navy Seal Adventure!")

print("Choose one of the two options:")
option = input("Press 'i' for instructions or 's' to start the game.")

"""
#explaining the rules of the game by instructions when user presses i on keyboard
"""
if (option == "i"):
    print("Here is your instructions")

elif (option == "s"): 
    print("The game is beginning... \n")

    name = input("Enter your name here: \n")
    print("Hello, " + name + " let's begin \n")
    print("You're being sent for deployment to Afghanistan. Do you leave you're family and risk your life? Y/N \n")

    choice = input("  ")

    if(choice == "y"):
        print("Congratulations " + name + ", you've been offered to be the Commanding Officer of this mission.\n Do you accept this position? Y/N \n")

        acceptPosition = input("  ")

        if(acceptPosition == "y"):
            print("Commander " + name + "! You need to act fast as the enemy have just stumbled upon your location and the op is compromised.\n Do you let the enemy go safely or terminate. Y- go safely, N-terminate them. \n")

        terminateOrSafe = input("  ")

        if(terminateOrSafe == "y"):
            print("Your first act as Comander " + name + " you chose to let the enemy go safely. They have told their army where you are hiding. \n 100 armed soldiers are on their way to you right now. \n Y-Do you evacuate position asap.\n N-Stay and fight, call air-support. \n")

        evacuateOrFight = input("  ")

        if(evacuateOrFight == "y"):
            print("You evacuate position, 100 men are gaining on you quickly, you aren't quick enough.\n You end up having to fight in their forests where they have the advantage. You being Commander " + name + " of this op, have failed!\n You and your team don't make it. \n End of game")

        elif(evacuateOrFight == "n"):
            print(" You chose to stay and fight. Taking the right steps to call air-support gives yous an advantage. \n You take out most of the enemy and the air-support does the rest.\n You and you team arrive home injured but safe.\n Although your injuries lead to you having to have both legs amputated which leads to you never return to the Navy.\n You will never again be called Commanding " + name + " again. \n End of game.")
        elif(terminateOrSafe == "n"):
            print("Your first act as Commander " + name + ", you have terminated the enemy which is in violation with rules of engagement. \n Do you lie and say they attacked you and your team? Y/N \n")

        
        elif(acceptPosition == "n"):
            print("The enemy has came upon your location and the op is compromised. Your commanding officer orders you to terminate the enemy. Do you obey your orders? Y/N \n")
        else:
            print("Invaild option. Please answer questions with y or n only.\n")

    elif(choice == "n"):
        print("You have been discharged for not following orders. Return to the home page with the option to play again. \n ")

    else: 
        print("Invaild option. Please answer questions with y or n only.\n")



def main():

    acceptPosition = input("")
    terminateOrSafe = input("")
    """

from simple_term_menu import TerminalMenu 

def end_of_game():
    print("You have been discharged for not following orders. Return to the home page with the option to play again.")

    
def congratulations_commander():
    print("Congratulations, you've been offered to be the Commanding Officer of this mission.\n Do you accept this position?")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        attacked()
        
    else:
        third_ques()



def question_one():
    print("You're being sent for deployment to Afghanistan. Do you leave you're family and risk your life?") 
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        congratulations_commander()
        
    else:
        end_of_game()

def print_instructions():
    print("Here is your instructions")


def start_game():
    print("The game is beginning... \n")
    name = input("Enter your name here: \n")
    print("Hello, " + name + " let's begin \n")
    question_one()


def main():
    print("Welcome to your Navy Seal Adventure!")
    print("Choose one of the two options:")
    options = ['1. instructions', '2. start the game']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. instructions':

        print_instructions()
    else:
        start_game()

main()