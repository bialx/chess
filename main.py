import src.opening as opening
import src.get_url as get_url
import sys, os

# Main definition - constants
menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')

    print ("Welcome,\n")
    print ("Type to get the info you want:")
    print ("1. Analyse openings")
    print ("2. Display ranks, general information")
    print ("\n0. Quit")
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
def menu1():
    print ("Clock timer ?\n")
    print("1. bullet\n")
    print("2. blitz\n")
    print("3. rapide\n")
    print("4. longue\n")
    print ("9. Back")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print ("Hello Menu 2 !\n")
    print ("9. Back")
    print ("0. Quit")
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
    '1': menu1,
    '2': menu2,
    '9': back,
    '0': exit,
}


# =======================
#      MAIN PROGRAM
# =======================

if __name__ == '__main__':
    # main_menu()
    opening_partial, opening_full = opening.build_dict()
    print(f"partial = \n{opening_partial}\n###\nfull = \n{opening_full}\n")
    opening.display_info_openings(opening_partial)
    opening.special_opening("Italian Game", opening_partial, opening_full)
    with open("output/opening.txt", "w") as f:
         for key, item in opening_partial.items():
             nbr_win, nbr_match = item
             f.write(key + "-- nombre win: " + str(nbr_win) + "--nombre match: " + str(nbr_match))
             f.write("\n")
