from urllib.request import urlopen
import requests
import bs4 as BeautifulSoup


# url = "https://lichess.org/@/Bialx/all"


def main():
    liste_opening = []
    for i in range(1,50):
        j = 30 + i
        link = f"https://lichess.org/@/Bialx/all?page={i}&_=15457356313{j}"
        liste_opening, end  = add_opening(link, liste_opening)
        if end == 1:
            break
    return occurence(liste_opening)


def add_opening(url, l):
    page = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(page.text, "html.parser")
    print(f"###### {url} ######")
    tag = soup.findAll('div', attrs={"class":"opening"})
    if tag == []:
        print("no more game")
        return (l,1)
    else:
        for elt in tag:
            l.append(elt.text)
        return (l,0)

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
    print(opening, len(opening))
