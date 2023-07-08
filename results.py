from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style


user_results = {
    "end_of_game":
    (
        "You have been discharged for not"
        " following orders.\n Go back to play again. \n"
    ),

    "relatiation":
    (
        "You lie to cover your back and say it was "
        "relatiation that made you termiate "
        "the enemy.\n There is an investigation launched "
        "and for this reason you have been \n "
        "discharged.\n"
        "GAME OVER! YOU LOSE."
    ),

    "plead_the_fifth":
    (
        "Pleading the fifth is definitely saying "
        "your guilty without saying your guilty.\n "
        "Straight away you are sent home and fired."
        "You now work in starbucks.\n"
        "GAME OVER! YOU LOSE."
    ),

    "denied_terminate":
    (
        "You disobeyed you're orders to terminate "
        "the enemy.\n In doing so the enemy gain on you and "
        "your men.\n 100 armed soliders come from every angle "
        "and attack.\n Your entire team are killed but you live.\n "
        "You arrive home injured but alive and the guilt eats "
        "you.\n You decide to never return to the Navy. \n"
        "GAME OVER! YOU LOSE."
    ),

    "stay_at_compound":
    (
        "After deciding to stay, you soon realised "
        "it was the right decision\n. After working another 6 months "
        "over seas,\n you were offered a position to be a Commanding "
        "Officer yet again.\n You return home to your family as "
        "a Commanding Officer.\n"
        "CONGRATULATIONS YOU HAVE WON THE GAME!!!"
    ),

    "bring_me_home":
    (
        "Choosing to go home in spite of being striped "
        "of your title,\n leads you to then "
        "be discharged from the Navy.\n "
        "You now work in Starbucks.\n"
        "GAME OVER! YOU LOSE."
    ),

    "tell_a_lie":
    (
        "One of your team mates have gone to the head of "
        "operations.\n They said that you attacked first. \n You have been "
        "given a Military Discharge and sent home.\n"
        "GAME OVER! YOU LOSE."
    ),

    "evacuate_position":
    (
        "You evacuate position, 100 men are gaining on you quickly,\n "
        "you aren't quick enough and you end up having to fight in their "
        "forests. \n They have the advantage here. "
        "You being Commander of this op, have failed!\n "
        "You and your team don't make it.\n"
        "GAME OVER! YOU LOSE."
    ),

    "stay_and_fight":
    (
        "You chose to stay and fight.\n Taking the right steps to "
        "call air-support gives yous an advantage.\n You take out most "
        "of the enemy and the air-support does the rest.\n You and you "
        "team arrive home injured but safe.\n Although your injuries lead "
        "to you having to have both legs amputated\n which leads to "
        "you never return to the Navy.\n You will never "
        "again be called Commander again.\n"
        "GAME OVER! YOU LOSE."
    ),

    "print_instructions":
    (
        "In order to play this game you simply \n"
        "need to use your UP and DOWN arrows,\n"
        "typically located on the bottom right of your keyboard.\n"
        "Follow along with the questions asked.\n"
        "Answer the questions that come up then "
        "click yes or no using the arrows.\n"
        "Do this to see if you have what it takes to be a\n"
        "Officer or Commanding Officer in the Navy Seals!\n"
    ),

    "question_one":
    (
        "You're being sent for deployment to Afghanistan.\n"
        " Do you leave your family and risk your life? \n"
    ),

    "congratulations_commander":
    (
        "Congratulations,\n You've been offered to"
        " be the Commanding Officer of this"
        " mission.\n Do you accept this position? \n"
    ),

    "denied_position":
    (
        "The enemy has came upon your location"
        " and the op is compromised.\n"
        " Your commanding officer orders you to terminate"
        " the enemy. \n Do you obey your orders? \n"
    ),

    "accepted_position":
    (
        "Commander, the enemy just stumbled upon your"
        " location and the op is compromised.\n"
        " Do you 'yes' let the enemy go safely or 'no' terminate? \n"
    ),

    "terminate":
    (
        "You terminated the enemy!\n Which is in"
        " violation with rules of engagement.\n"
        " Do you lie and say they attacked you and your team first? \n"
    ),

    "go_safely":
    (
        "You chose to let the enemy go safely.\n"
        "They have told their army where you are hiding.\n"
        "100 armed soldiers are on their way "
        "to you right now.\n Do you 'yes' evacuate position "
        "asap or .. \n 'no' stay and fight, call air-support for backup! \n"
    ),

    "tell_the_truth":
    (
        "You didn't lie and your honesty for the protection "
        "of your men\n had resulted in you not being fired,\n but you are "
        "striped of your title. Do you stay at the compound? \n"
    ),

    "denied_go_safely":
    (
        "You obyed your orders from your Commander and "
        "terminated the enemy.\n This is in complete violation "
        "with the rules of engagement.\n Do you lie and tell "
        "the head officer that your termination of the enemy \n "
        "was purely retaliation?\n "
    )
}
