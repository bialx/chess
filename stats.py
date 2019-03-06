from urllib.request import urlopen
import requests
import bs4 as BeautifulSoup
import datetime
import mechanicalsoup


############### Analyse games played on Lichess ###############

# url = "https://lichess.org/@/Bialx/all"
# url 15m : https://lichess.org/@/Bialx/search?page=1&clock.initMin=900&sort.field=d&sort.order=desc&_=1550832506578

limit_date = 2
current_date = datetime.datetime.now()

#This for loop rely on the url and the "cadence" you wanna analyse, need to modify the value of j and the url if you're looking
#for someone else
def main():
    dict_opening = {}
    for i in range(1,1000):
        j = i+26
        link = f"https://lichess.org/@/Bialx/search?page={i}&clock.initMin=900&sort.field=d&sort.order=desc&_=15508329043{j}"
        dict_opening, end  = add_opening(link, dict_opening)
        if end == 1:
            break
    print(dict_opening)
    return dict_opening


def add_opening(url, d):
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
        return (d,1)
    else:
        for opening, win, date in zip(tag_opening, tag_win, tag_header):
            tag = win.span
            tag_date = date.time
            date_game = tag_date['datetime']
            month = ((date_game.split("-")[1]).split("-")[0]).replace("0","")
            #if game are too old
            print(abs(int(month) - current_date.month), limit_date)
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
            d[filtered_text] = add(d.get(filtered_text, (win_status, 1)), (win_status, 1))
        return (d,0)

#2018-12-08T21:26:44.384Z

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


if __name__ == '__main__':
    opening = main()
    with open("opening.txt", "w") as f:
        for key, item in opening.items():
            nbr_win, nbr_match = item
            f.write(key + "-- nombre win: " + str(nbr_win) + "--nombre match: " + str(nbr_match))
            f.write("\n")
