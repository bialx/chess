import argparse


def make_parser():
    parser = argparse.ArgumentParser(description = "Chess tool to analyzed lichess's players")
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    return args
