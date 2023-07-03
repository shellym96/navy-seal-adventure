from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style
from results import user_results


def end_of_game():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print(Fore.GREEN  + "You have been discharged for not "
    "following orders.\n Return to the home page "
    "with the option to play again. \n")
    def go_back():
        options =['Go back',]
        main_menu = TerminalMenu(options)
        options_index = main_menu.show()
        options_choice = options[options_index]
        if options_choice == 'Go back':
            main()


def go_back():
    options =['Go back',]
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == 'Go back':
        main()


def retaliation():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print(Fore.GREEN  + "You lie to cover your back and say it was "
    "relatiation that made you termiate "
    "the enemy.\n There is an investigation launched "
    "and for this reason you have been \n "
    "discharged.\n")
    print("GAME OVER!")


def plead_the_fifth():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print(Fore.GREEN  + "Pleading the fifth is definitely saying "
    "your guilty without saying your guilty.\n "
    "Straight away you are sent home and fired."
    "You now work in starbucks.\n")
    print("GAME OVER!")


def denied_terminate():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print(Fore.GREEN  + "You disobeyed you're orders to terminate "
    "the enemy.\n In doing so the enemy gain on you and "
    "your men.\n 100 armed soliders come from every angle "
    "and attack.\n Your entire team are killed but you live.\n "
    "You arrive home injured but alive and the guilt eats "
    "you.\n You decide to never return to the Navy. \n")
    print("GAME OVER!")
    

def denied_go_safely_():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print(Fore.GREEN  + "You obyed your orders from your Commander and "
    "terminated the enemy.\n This is in complete violation "
    "with the rules of engagement.\n Do you lie and tell "
    "the head officer that your termination of the enemy \n "
    "was purely retaliation?\n ")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        retaliation()
    else:
        plead_the_fifth()


def stay_at_compound():
    """ 
    This function congratulates the user for their win on successfully
    completing the game, resulting in the win.
    """
    print(Fore.GREEN  + "After deciding to stay, you soon realised "
    "it was the right decision\n. After working another 6 months "
    "over seas,\n you were offered a position to be a Commanding "
    "Officer yet again.\n You return home to your family as "
    "a Commanding Officer.")
    print("CONGRATULATIONS!! You have won the game!")


def bring_me_home():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print(Fore.GREEN  + "Choosing to go home in spite of being striped "
    "of your title,\n leads you to then "
    "be discharged from the Navy.\n "
    "You now work in Starbucks.\n")
    print("GAME OVER!")


def tell_a_lie():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
   # print(Fore.GREEN  + "One of your team mates have gone to the head of "
    #"operations\n. They said that you attacked first. \n You have been "
   # "given a Military Discharge and sent home.\n")
   # print("GAME OVER!")


def tell_the_truth():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print(Fore.GREEN  + "You didn't lie and your honesty for the protection "
    "of your men\n had resulted in you not being fired,\n but you are "
    "striped of your title. Do you stay at the compound? \n")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        stay_at_compound()
    else:
        bring_me_home()


def evacuate_position():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print(Fore.GREEN  + "You evacuate position, 100 men are gaining on you quickly,\n "
    "you aren't quick enough and you end up having to fight in their "
    "forests. \n They have the advantage here. "
    "You being Commander of this op, have failed!\n "
    "You and your team don't make it.\n")
    print("GAME OVER!")


def stay_and_fight():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print(Fore.GREEN  + "You chose to stay and fight.\n Taking the right steps to "
    "call air-support gives yous an advantage.\n You take out most "
    "of the enemy and the air-support does the rest.\n You and you "
    "team arrive home injured but safe.\n Although your injuries lead "
    "to you having to have both legs amputated\n which leads to "
    "you never return to the Navy.\n You will never "
    "again be called Commander again.\n")
    print("GAME OVER!")


def go_safely():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print(Fore.GREEN  + "You chose to let the enemy go safely.\n"
    "They have told their army where you are hiding.\n"
    "100 armed soldiers are on their way "
    "to you right now.\n Do you 'yes' evacuate position "
    "asap or .. \n 'no' stay and fight, call air-support for backup! \n")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        evacuate_position()
    else:
        stay_and_fight()


def terminate():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print(Fore.GREEN  + "You terminated the enemy!\n Which is in"
    " violation with rules of engagement.\n"
    " Do you lie and say they attacked you and your team first? \n")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        tell_a_lie()
    else:
        tell_the_truth()


def accepted_position():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print(Fore.GREEN  + "The enemy just stumbled upon your"
    " location and the op is compromised.\n"
    " Do you 'yes' let the enemy go safely or 'no' terminate? \n")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        go_safely()
    else:
        terminate()


def denied_poistion():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print(Fore.GREEN  + "Commander , the enemy has came upon your location"
    " and the op is compromised.\n"
    " Your commanding officer orders you to terminate"
    " the enemy. \n Do you obey your orders? \n")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        denied_go_safely_()
    else:
        denied_terminate()


def congratulations_commander():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print(Fore.GREEN  + "Congratulations,\n You've been offered to"
    " be the Commanding Officer of this"
    " mission.\n Do you accept this position? \n")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        accepted_position()
    else:
        denied_poistion()


def question_one():
    """ 
    This function brings the user to the first question with yes or no answers,
    leading to the next question.
    """
    print(Fore.GREEN + "You're being sent for deployment to Afghanistan.\n"
    " Do you leave your family and risk your life? \n")
    options = ['1. yes', '2. no']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. yes':

        congratulations_commander()
    else:
        end_of_game()


def print_instructions():
    """ This function will explain the instructions on how to play the game to the user """
    print(Fore.GREEN + "In order to play this game you simply \n"
    "need to use your UP and DOWN arrows,\n"
    "typically located on the bottom right of your keyboard.\n"
    "follow along with the questions asked.\n"
    "Answer the questions that come up then click yes or no using the arrows.\n"
    "Do this to see if you have what it takes to be a\n"
    "Officer in the Navy Seals! \n")
    options = ['1. Go back']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. Go back':

        main()


def start_game():
    print(Fore.GREEN + "The game is beginning...\n")
    while True:
        name = input("Enter your name here:")
        if not name.isalpha() or len(name) < 2 or len(name) > 8:
            print (f"{name} is invalid. Please enter 2-8 letters")
        else:
            print(f"Welcome {name.capitalize()}!")
            break
    question_one()


def main():
    """
    This function will greet the user to the game with a title,
    It will give the user the option of 2 choices with instructions or to start the game,
    If they choose the instructions option they will be given another option to go back and begin the game.
    """
    print(Fore.GREEN + "Welcome to your Navy Seal Adventure!")
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
