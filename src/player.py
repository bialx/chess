from urllib.request import urlopen
import requests
import bs4 as BeautifulSoup
import datetime

import src.parse as parse
args = parse.make_parser()

def get_player():
    global args
    player = args.player
    url = f"https://lichess.org/@/{player}"
    page = requests.get(url)
    if page.status_code == 404:
        print("This player doesnt play on lichess !")
        return

    soup = BeautifulSoup.BeautifulSoup(page.text, "html.parser")
    all_cadence = soup.findAll('a', attrs={"class":"game"})

    for class_game in all_cadence:
        href = class_game.get("href")
        next_link = f"https://lichess.org{href}"
        print(next_link)
        page_cadence = requests.get(next_link)
        soup2 = BeautifulSoup.BeautifulSoup(page_cadence.text, "html.parser")
        a = soup2.findAll('div', attrs={"class":"streak"})
        for i in a:
            print(i)
