import argparse

def make_parser():
    """ Fonction to build command line arguments parser """

    parser = argparse.ArgumentParser(description = "Chess tool to analyzed lichess's players")
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-p", "--player", help="name of the player on lichess you wish to analyze")
    parser.add_argument("-o", "--old", help="how old are the game you wish to analyze in terms of months")
    args = parser.parse_args()
    return args
