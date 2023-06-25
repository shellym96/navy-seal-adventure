from simple_term_menu import TerminalMenu 

def end_of_game():
    print("You have been discharged for not following orders. Return to the home page with the option to play again.")



def retaliation():
    print("You lie to cover your back and say it was relatiation that made you termiate the enemy. There is an investigation launched and for this reason you have been discharged. GAME OVER.")

def plead_the_fifth():
    print("Pleading the fifth is definitely saying your guilty without saying your guilty. Straight away you are sent home and fired. You now work in starbucks. GAME OVER!")

    
def denied_terminate():
    print("You obyed your orders from your Commander and terminated the enemy. This is in complete violation with the rules of engagement. Do you lie and tell the head officer that your termination of the enemy was purely retaliation?")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        retaliation()
        
    else:
        plead_the_fifth()


def denied_go_safely_():
    print("You disobeyed you're orders to terminate the enemy. In doing so the enemy gain on you and your men, 100 armed soliders come from every angle and attack. Your entire team are killed but you live. You arrive home injured but alive and the guilt eats you. You decide to never return to the Navy. There for GAME OVER.")

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
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

       go_safely()
        
    else:
        terminate()

def denied_poistion():
    print("The enemy has came upon your location and the op is compromised. Your commanding officer orders you to terminate the enemy. Do you obey your orders?")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

       denied_go_safely_()
        
    else:
        denied_terminate()

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