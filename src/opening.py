from urllib.request import urlopen
import requests
import bs4 as BeautifulSoup
import datetime
############### Analyse games played on Lichess ###############

# url = "https://lichess.org/@/Bialx/all"
# url 15m : https://lichess.org/@/Bialx/search?page=1&clock.initMin=900&sort.field=d&sort.order=desc&_=1550832506578

limit_date = 12
current_date = datetime.datetime.now()

#This for loop rely on the url and the "cadence" you wanna analyse, need to modify the value of j and the url if you're looking
#for someone else
def build_dict():
    dict_opening_partial = {}
    dict_opening_full = {}
    print("Processing url /*")
    for i in range(1,50):
        j = i+26
        link = f"https://lichess.org/@/Bialx/search?page={i}&clock.initMin=900&sort.field=d&sort.order=desc&_=15508329043{j}"
        dict_opening_partial, dict_opening_full, end  = add_opening(link, dict_opening_partial,  dict_opening_full)
        if end == 1:
            break
    print("## DONE ##")
    return dict_opening_partial, dict_opening_full


def add_opening(url, d_filtered, d_full):
    """ Create a dictionary with key = opening, value = (nbr_win, nbr_match) """
    global limit_date, current_date
    page = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(page.text, "html.parser")
    # print(f"###### {url} ######")
    tag_opening = soup.findAll('div', attrs={"class":"opening"})
    tag_win = soup.findAll('div', attrs={"class":"result"})
    tag_header = soup.findAll('div', attrs={"class":"header"})

    #Working with infinite scroll, end condition to check if there is nothing more to scroll
    if tag_opening == []:
        # print("no more game")
        return (d_filtered,d_full,1)
    else:
        for opening, win, date in zip(tag_opening, tag_win, tag_header):
            tag = win.span
            tag_date = date.time
            date_game = tag_date['datetime']
            month = ((date_game.split("-")[1]).split("-")[0]).replace("0","")

            #if game are too old
            if abs(int(month) - current_date.month) > limit_date:
                break
            if ('class' in tag.attrs and tag['class'][0] == 'up'):
                win_status = 1
            elif ('class' in tag.attrs and tag['class'][0] == 'down'):
                win_status = 0
            elif ('class' not in tag.attrs and opening.text != ''):
                win_status = 0.5

            #We just want the name of the core opening, neither the variation nor its classification C45 for example
            filtered_text = ((opening.text).split(":")[0])[3:]
            # print(filtered_text, tag.attrs)
            d_filtered[filtered_text] = add(d_filtered.get(filtered_text, (win_status, 1)), (win_status, 1))

            #full opening
            d_full[opening.text] = add(d_full.get(opening.text, (win_status, 1)), (win_status, 1))
        return (d_filtered, d_full, 0)


#Function to add 2tuples
def add(xs,ys):
     return tuple(x + y for x, y in zip(xs, ys))


#Function to create from a list a dictionary with the number of times the key appear in the list as a value
#Here we rather return a list instead of a dictionnary
def occurence(l):
    liste_occurence = []
    compte = {}.fromkeys(set(l),0)
    for valeur in l:
        compte[valeur] += 1
    for cle, valeur in compte.items():
        liste_occurence.append((cle, valeur))
    return liste_occurence

def display_info_openings(dict):
    #most played opening
    k = list(dict.keys())
    v = list(dict.values())
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


def special_opening(key_opening, dict_partial, dict_full):
    detailled_list = [(key, value) for key,value in dict_full.items() if key_opening in key]
    max_opening, max_value = max(detailled_list, key = lambda x: x[1][1])
    min_opening, min_value = min(detailled_list, key = lambda x: x[1][0])
    winrate_win = (max_value[0]/max_value[1]) * 100
    winrate_loose = (min_value[0]/min_value[1]) * 100
    print(f"His main line in the opening {key_opening} is {max_opening} with a winrate of {winrate_win} over {dict_full[max_opening][1]} games")
    print(f"His worst line is {min_opening} with a winrate of {winrate_loose} over {dict_full[min_opening][1]} games")
    print(f"Do you want to display all the lines of {key_opening} ? Press Y to display")
    ch = input(">>")
    if ch == 'Y' or ch == 'y':
        print(detailled_list)
    else:
        return
