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


        terminateOrSafe = input("  ")

        

        evacuateOrFight = input("  ")

        if(evacuateOrFight == "y"):
            print("")

        elif(evacuateOrFight == "n"):
            print(" You chose to stay and fight. Taking the right steps to call air-support gives yous an advantage. \n You take out most of the enemy and the air-support does the rest.\n You and you team arrive home injured but safe.\n Although your injuries lead to you having to have both legs amputated which leads to you never return to the Navy.\n You will never again be called Commanding " + name + " again. \n End of game.")
        elif(terminateOrSafe == "n"):
            print("Your first act as Commander " + name + ", you have terminated the enemy which is in violation with rules of engagement. \n Do you lie and say they attacked you and your team? Y/N \n")

        
        elif(acceptPosition == "n"):
            print("The enemy has came upon your location and the op is compromised. Your commanding officer orders you to terminate the enemy. Do you obey your orders? Y/N \n")
        else:
            print("Invaild option. Please answer questions with y or n only.\n")


        print("Invaild option. Please answer questions with y or n only.\n")



def main():

    acceptPosition = input("")
    terminateOrSafe = input("")
    """

from simple_term_menu import TerminalMenu 

def end_of_game():
    print("You have been discharged for not following orders. Return to the home page with the option to play again.")



def stay_at_compound():
    print("After deciding to stay, you soon realised it was the right decision. After working another 6 months over seas, you were offered a position to be a Commanding  Officer yet again. You return home to your family as a Commanding Officer. CONGRATULATIONS You have won the game!")

def bring_me_home():
    print("Choosing to go home by spite of being striped of your title, leads you to then be discharged from the Navy. You now work in Starbucks. GAME OVER!")

def tell_a_lie():
    print("One of your team mates told the head of operations that you attacked first. You have been given a Military Discharge and sent home. GAME OVER!")

def tell_the_truth():
    print("You didn't lie and your honesty for the protection of your men stopped you from being fired, but you are striped of your title. Do you stay at the compound?")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

       stay_at_compound()
        
    else:
        bring_me_home()


def evacuate_position():
    print("You evacuate position, 100 men are gaining on you quickly, you aren't quick enough. You end up having to fight in their forests where they have the advantage. You being Commander of this op, have failed! You and your team don't make it. GAME OVER!")

def stay_and_fight():
    print("You chose to stay and fight. Taking the right steps to call air-support gives yous an advantage. You take out most of the enemy and the air-support does the rest. You and you team arrive home injured but safe. Although your injuries lead to you having to have both legs amputated which leads to you never return to the Navy. You will never again be called Commanding again. GAME OVER!")


def go_safely():
    print("You chose to let the enemy go safely. They have told their army where you are hiding and 100 armed soldiers are on their way to you right now. Do you yes evacuate position asap or no stay and fight, call air-support for backup!")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

       evacuate_position()
        
    else:
        stay_and_fight()


def terminate():
    print("You terminated the enemy which is in violation with rules of engagement. Do you lie and say they attacked you and your team first?")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

       tell_a_lie()
        
    else:
        tell_the_truth()



def accepted_position():
    print("The enemy just stumbled upon your location and the op is compromised. Do you yes let the enemy go safely or no terminate?")


def denied_poistion():
    print("The enemy has came upon your location and the op is compromised. Your commanding officer orders you to terminate the enemy. Do you obey your orders?")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

       go_safely()
        
    else:
        terminate()

def congratulations_commander():
    print("Congratulations, you've been offered to be the Commanding Officer of this mission. Do you accept this position?")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        accepted_position()
        
    else:
        denied_poistion()



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