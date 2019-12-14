from urllib.request import urlopen
import requests
import bs4 as BeautifulSoup
import datetime
from collections import defaultdict
import src.parse as parse

args = parse.make_parser()

def get_player():
    number_of_games, rating = defaultdict(int), defaultdict(int)
    list_of_cadence = ["BULLET", "BLITZ", "RAPID", "CLASSICAL"]
    global args
    player = args.player
    url = f"https://lichess.org/@/{player}"
    page = requests.get(url)

    #Handle wrong username on lichess
    if page.status_code == 404:
        print("This player doesnt play on lichess !")
        return

    #create the Beautiful object to parse containing all informations
    #related to a player's stats
    soup = BeautifulSoup.BeautifulSoup(page.text, "html.parser")
    all_cadence = soup.findAll('a', attrs={"class":"game"})

    #for each cadence we update a dict with the number of games played and the rating in this cadence
    for class_game in all_cadence:
        cadence = class_game.h3.text
        if cadence in list_of_cadence:
            info = class_game.rating.text.split()
            number_of_games[cadence] = info[2]
            rating[cadence] = info[0]
        else: continue
    return number_of_games, rating


def display_info_player(dict_game, dict_rating):
    global args
    player = args.player
    print(f"Information on {player}:\n")
    for cadence in dict_game:
         print(f"Rating in {cadence} is {dict_rating[cadence]} with {dict_game[cadence]} games\n")
