from urllib.request import urlopen
import requests
import bs4 as BeautifulSoup
import datetime
import argparse
import src.parse as parse



############### Tool to analyse games played on Lichess ###############

#Global variable used in the following .py
limit_date = 6  #how old in term of month we wish to analyze
current_date = datetime.datetime.now()
numbers_of_game = 0
args = parse.make_parser() #build parser for command line arguments



#This for loop rely on the url and the game timing you wanna analyse, need to modify the value of j and the url if you're looking for someone else
def build_dict():
    """ Return dictionnary with the differents opening -> partial: main line // full: main line+variation"""

    global args
    d_opening_partial = {}
    d_opening_full = {}

    print("Processing url /*")

    #Loop on the differents url (infinite loop on lichess) to build our dictionaries
    for i in range(1,50):

        #j and link must be build manually as the process isnt automized yet: WIP
        j = i+101
        link = f"https://lichess.org/@/Bialx/search?page={i}&perf=2&sort.field=d&sort.order=desc&_=1575394082{j}"

        if args.verbose:
            print(f"### {link} ###")

        d_opening_partial, d_opening_full, end  = add_opening(link, d_opening_partial,  d_opening_full)

        #If we reach the end of our infinite loop or games are too old
        if end == 1:
            break

    print(f"numbers of games analyzed : {numbers_of_game}\n## DONE ##")
    if args.verbose:
        print(f"partial dict = \n{d_opening_partial}\n\n\nfull dict = \n{d_opening_full}\n")
    return d_opening_partial, d_opening_full



def add_opening(url, d_opening_partial, d_opening_full):
    """ Create two dictionaries with key = opening, value = (nbr_win, nbr_match)
            partial: main line // full: main line+variation """

    global args, current_date, numbers_of_game
    if args.old:
        limit_date = args.old

    #Create the Beautiful object to parse
    page = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(page.text, "html.parser")
    tag_opening = soup.findAll('div', attrs={"class":"opening"})        #used to handle the opening
    tag_win = soup.findAll('div', attrs={"class":"result"})             #used to handle win, loose or draw
    tag_header = soup.findAll('div', attrs={"class":"header"})          #used to handle the date

    #Working with infinite scroll, end condition to check if there is nothing more to scroll
    if tag_opening == []:
        print("no more game */")
        return (d_opening_partial, d_opening_full, 1)
    else:
        for opening, win, date in zip(tag_opening, tag_win, tag_header):
            outcome = win.span
            tag_date = date.time
            date_game = tag_date['datetime']
            month = ((date_game.split("-")[1]).split("-")[0]).replace("0","")

            #if game are too old
            if abs(int(month) - current_date.month) > limit_date:
                break

            # we get 1 point if victory, 0.5 if draw, 0 if loss
            if ('class' in outcome.attrs and outcome['class'][0] == 'win'):
                win_status = 1
            elif ('class' in outcome.attrs and outcome['class'][0] == 'loss'):
                win_status = 0
            elif ('class' not in outcome.attrs and opening.text != ''):
                win_status = 0.5

            #We just want the name of the core opening for the parial dict, the full version for full dict, we need to parse the opening date first
            full_text, filtered_text = parser(opening.text)

            #We are working with tuples (nbr_win, nbr_match) so to update our dict when we encounter a knonw opening
            #we do the following get (nbr_win, nbr_match) of the opening and replace it with (nbr_win + win_status, nbr_match + 1)
            #If we dont have the opening in our dict we had for the key opening the following tuple (win_status, 1)
            d_opening_partial[filtered_text] = add(d_opening_partial.get(filtered_text, (win_status, 1)), (win_status, 1))
            d_opening_full[full_text] = add(d_opening_full.get(full_text, (win_status, 1)), (win_status, 1))

            #increase the number of games analyzed
            numbers_of_game += 1
        return (d_opening_partial, d_opening_full, 0)



def add(xs,ys):
    """ Function to add 2tuples """
    return tuple(x + y for x, y in zip(xs, ys))




def occurence(l):
    """ Function to create from a list a dictionary with the number of times the key appear in the list as a value
        Here we rather return a list instead of a dictionnary """

    liste_occurence = []
    compte = {}.fromkeys(set(l),0)
    for valeur in l:
        compte[valeur] += 1
    for cle, valeur in compte.items():
        liste_occurence.append((cle, valeur))
    return liste_occurence


def parser(opening):
    """ Return (opening_full, opening_partial) as tuple where our opening are parsed according the main line or main line + variation
        We get ride of the classification (ex: C44) """

    if ":" not in opening:
        opening_partial = ((opening).split("1.")[0]).strip()[3:]
    else:
        opening_partial = ((opening).split(":")[0]).strip()[3:]
    opening_full = ((opening).split("1.")[0]).strip()[3:]
    return opening_full, opening_partial



def display_info_openings(dict):
    """ Display overall information on differents opening:
                -> Most played
                -> Best opening
                -> Worst opening
        Input is partial_opening """

    k = list(dict.keys())
    v = list(dict.values())

    # WORK TO BE DONE HERE TO CHECK IF EVERYTHING IS OKAY
    max_value_games = max(v, key=lambda x: x[1]) #get the max value -> nbr_match of the among the tuples (nbr_win, nbr_match)
    max_value_ratio = max(v, key=lambda x: x[0]/x[1] if x[1]>5 else -1)
    min_value_ratio = min(v, key=lambda x: x[0]/x[1] if x[1]>5 else 1)
    opening_most_played = k[v.index(max_value_games)]
    opening_best_ratio = k[v.index(max_value_ratio)]
    opening_worst_ratio = k[v.index(min_value_ratio)]
    ratio_max = (max_value_ratio[0]/max_value_ratio[1])*100
    ratio_min = (min_value_ratio[0]/min_value_ratio[1])*100

    print(f"Most played opening is : {opening_most_played}\nIt was played {max_value_games[1]} times with {max_value_games[0]} games won")
    print(f"#########\nIt's best opening is : {opening_best_ratio}\nWith a win ratio of {ratio_max}% over {max_value_ratio[1]} games")
    print(f"#########\nIt's worst opening is : {opening_worst_ratio}\nWith a win ratio of {ratio_min}% over {min_value_ratio[1]} games\n#########")
    return

def special_opening(key_opening, dict_partial, dict_full):
    """ Display information on a particular opening choosed by key_opening """

    #build a list containing the different variations of the core opening: key_opening
    detailled_list = [(key, value) for key,value in dict_full.items() if key_opening in key]
    max_opening, max_value = max(detailled_list, key = lambda x: x[1][1])
    min_opening, min_value = min(detailled_list, key = lambda x: x[1][0])
    winrate_win = (max_value[0]/max_value[1]) * 100
    winrate_loose = (min_value[0]/min_value[1]) * 100

    print(f"His main line in the opening {key_opening} is {max_opening} with a winrate of {winrate_win} over {dict_full[max_opening][1]} games")
    print(f"His worst line is {min_opening} with a winrate of {winrate_loose} over {dict_full[min_opening][1]} games")
    print(f"Do you want to display all the lines of {key_opening} ? Press Y to display")
    ch = input(" >>")
    if (ch.lower() == 'y' or ch.lower() == 'yes'):
        print(detailled_list)
    else:
        print("bye bye")
        return
