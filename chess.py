import src.opening as opening
import src.player as player
import sys, os, subprocess

# Main definition - constants
menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    print ("Welcome,\n", flush = False)
    print ("Type to get the info you want:", flush = False)
    print ("1. Analyse openings", flush = False)
    print ("2. Display ranks, general information", flush = False)
    print ("\n0. Quit", flush = False)
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

# Menu 1
def menu_opening():

    #Get the different opening as dict -> partial: main line // full: main line+variation
    opening_partial, opening_full = opening.build_dict()

    #Write in a text file the differents opening in opening_partial
    opening.opening_to_txt(opening_partial)

    #Display overall information on openings
    opening.display_info_openings(opening_partial)

    print("Display : \n1. A particular opening and its variations\n2. All the openings\n3. Go back", flush = False)
    choice = input(" >> ")
    if choice == "1":
        op = input(" Opening >> ")
        opening.special_opening(op, opening_partial, opening_full)
    elif choice == "2":
        opening.display_all()
    else:
        print("Wrong input", flush = False)
        exec_menu("9")

    print ("9. Back", flush = False)
    print ("0. Quit", flush = False)
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Menu 2
def menu_player():
    print ("Overall information !\n", flush = False)
    dict_game, dict_rating = player.get_player()
    player.display_info_player(dict_game, dict_rating)
    print ("9. Back", flush = False)
    print ("0. Quit", flush = False)
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()



# =======================
#    MENUS DEFINITIONS
# =======================
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu_opening,
    '2': menu_player,
    '9': back,
    '0': exit,
}



def decorate():
    print('''
  (\=, \t\t\t\t\t\t   ,=/)
 //  .\\ \t\t\t\t\t  /.  \\
(( \_  \\ \t\t\t\t\t /  _/ ))
 ))  `\_) \t\t\t\t\t(_/'  ((
(/     \\ \t\t\t\t\t/    /(
 | _.-'| \t\t CHESS ANALYZE \t\t \'-._ |
  )___( \t\t\t\t\t  )___(
 (=====) \t\t\t\t\t (=====)
 }====={ \t\t\t\t\t }====={
(_______) \t\t\t\t\t(_______)
''', flush = False)
# =======================
#      MAIN PROGRAM
# =======================

if __name__ == '__main__':
    decorate()
    main_menu()
