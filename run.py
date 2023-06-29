from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style


def end_of_game():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print('\033[32m' + "You have been discharged for not " +
    "following orders. Return to the home page " +
    "with the option to play again. \n")


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
    print('\033[32m' + "You lie to cover your back and say it was" +
    " relatiation that made you termiate" +
    " the enemy. There is an investigation launched" +
    " and for this reason you have been" +
    " discharged. GAME OVER. \n")


def plead_the_fifth():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print('\033[32m' + "Pleading the fifth is definitely saying" +
    " your guilty without saying your guilty." +
    " Straight away you are sent home and fired." +
    " You now work in starbucks. GAME OVER!\n")


def denied_terminate():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print('\033[32m' + "You disobeyed you're orders to terminate" +
    " the enemy. In doing so the enemy gain on you and" +
    " your men, 100 armed soliders come from every angle" +
    " and attack. Your entire team are killed but you live." +
    " You arrive home injured but alive and the guilt eats" +
    " you. You decide to never return to the Navy." +
    " There for GAME OVER. \n")
    

def denied_go_safely_():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print('\033[32m' + "You obyed your orders from your Commander and" + 
    " terminated the enemy. This is in complete violation" +
    " with the rules of engagement. Do you lie and tell" +
    " the head officer that your termination of the enemy" +
    " was purely retaliation?\n ")
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
    print('\033[32m' + "After deciding to stay, you soon realised" +
    " it was the right decision. After working another 6 months" +
    " over seas, you were offered a position to be a Commanding" +
    " Officer yet again. You return home to your family as" +
    " a Commanding Officer.")
    print("CONGRATULATIONS!! You have won the game!")


def bring_me_home():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print('\033[32m' + "Choosing to go home by spite of being striped" +
    " of your title, leads you to then" +
    " be discharged from the Navy. You now work" +
    " in Starbucks. GAME OVER! \n")


def tell_a_lie():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print('\033[32m' + "One of your team mates told the head of" +
    " operations that you attacked first. You have been" +
    " given a Military Discharge and sent home. GAME OVER! \n")


def tell_the_truth():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print('\033[32m' + "You didn't lie and your honesty for the protection" +
    " of your men stopped you from being fired, but you are" +
    " striped of your title. Do you stay at the compound? \n")
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
    print('\033[32m' + "You evacuate position, 100 men are gaining on you quickly," +
    " you aren't quick enough you end up having to fight in their" +
    " forests where they have the advantage. You being" +
    " Commander of this op, have failed! You and your team" +
    " don't make it. GAME OVER! \n")


def stay_and_fight():
    """ 
    This function presents the user with their outcome of the game. 
    This lets them know their fate, and that the game is over.
    """
    print('\033[32m' + "You chose to stay and fight. Taking the right steps to" +
    " call air-support gives yous an advantage. You take out most" +
    " of the enemy and the air-support does the rest. You and you" +
    " team arrive home injured but safe. Although your injuries lead" +
    " to you having to have both legs amputated which leads to" +
    " you never return to the Navy. You will never" +
    " again be called Commander again. GAME OVER! \n")


def go_safely():
    """ 
    This function presents the user with a question, with yes or no answers 
    then leading them to yet another question.
    """
    print('\033[32m' + "You chose to let the enemy go safely." +
    "They have told their army where you are" +
    " hiding and 100 armed soldiers are on their way" +
    " to you right now. Do you yes evacuate position" +
    " asap or no stay and fight, call air-support for backup! \n")
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
    print('\033[32m' + "You terminated the enemy which is in" +
    " violation with rules of engagement." +
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
    print('\033[32m' + "The enemy just stumbled upon your" +
    " location and the op is compromised." +
    " Do you yes let the enemy go safely or no terminate? \n")
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
    print('\033[32m' + "The enemy has came upon your location" +
    " and the op is compromised." +
    " Your commanding officer orders you to terminate" +
    " the enemy. Do you obey your orders? \n")
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
    print('\033[32m' + "Congratulations, you've been offered to" +
    " be the Commanding Officer of this" +
    " mission. Do you accept this position? \n")
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
    print('\033[32m' + "You're being sent for deployment to Afghanistan." +
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
    print('\033[32m' + "\n In order to play this game you simply" +
    " need to use your UP and DOWN arrows," +
    " typically located on the bottom right of your" +
    " keyboard. follow along with the questions" +
    " asked. Answer the questions that come up then answer" +
    " with the yes and no using the arrows," +
    " then see if you have what it takes to be a Commanding" +
    " Officer in the Navy Seals! \n")
    options = ['1. Go back']
    main_menu = TerminalMenu(options)
    options_index = main_menu.show()
    options_choice = options[options_index]
    if options_choice == '1. Go back':

        main()


def start_game():
    """ This function will ask the user for their name and then the game will begin to start"""
    print('\033[32m' + "The game is beginning... \n")
    name = input('\033[32m' + "Enter your name here: \n")
    print('\033[32m' + "Hello, " + name + " let's begin \n")
    question_one()


def main():
    """
    This function will greet the user to the game with a title,
    It will give the user the option of 2 choices with instructions or to start the game,
    If they choose the instructions option they will be given another option to go back and begin the game.
    """
    print('\033[32m' + "Welcome to your Navy Seal Adventure!")
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
