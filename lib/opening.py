from urllib.request import urlopen
import requests
import bs4 as BeautifulSoup
import datetime
############### Analyse games played on Lichess ###############

# url = "https://lichess.org/@/Bialx/all"
# url 15m : https://lichess.org/@/Bialx/search?page=1&clock.initMin=900&sort.field=d&sort.order=desc&_=1550832506578

limit_date = 2
current_date = datetime.datetime.now()

#This for loop rely on the url and the "cadence" you wanna analyse, need to modify the value of j and the url if you're looking
#for someone else
def build_dict():
    dict_opening_partial = {}
    dict_opening_full = {}
    for i in range(1,50):
        j = i+26
        link = f"https://lichess.org/@/Bialx/search?page={i}&clock.initMin=900&sort.field=d&sort.order=desc&_=15508329043{j}"
        dict_opening_partial, dict_opening_full, end  = add_opening(link, dict_opening_partial,  dict_opening_full)
        if end == 1:
            break
    return dict_opening_partial, dict_opening_full


def add_opening(url, d_filtered, d_full):
    """ Create a dictionary with key = opening, value = (nbr_win, nbr_match) """
    global limit_date, current_date
    page = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(page.text, "html.parser")
    print(f"###### {url} ######")
    tag_opening = soup.findAll('div', attrs={"class":"opening"})
    tag_win = soup.findAll('div', attrs={"class":"result"})
    tag_header = soup.findAll('div', attrs={"class":"header"})

    #Working with infinite scroll, end condition to check if there is nothing more to scroll
    if tag_opening == []:
        print("no more game")
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
    for key, value in dict:
        return 0
