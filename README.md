# ♞ CHESS ANALYZER ♘

Tool to analyse game played on lichess. The idea is to gather as much data as we can on a player

## MENU

* **1.** Provide stats on the differents opening played by the player           
   * most played opening              
   * best/worst opening in term of win ratio            
   * details on a given opening (win ration according to every variation played)


* **2.** You can give a player as a command line argument to display his overall rating and games played
         in bullet/blitz/rapid/classical


## Parameters

We have to different ways to scrap data. Either automatic with selenium or using hard coded url (need to get it by analyzing the request made by lichess when scrolling the infinite scroll). The selenium option is slower and gather less data. 


**-v --verbose** : increase verbosity

**-p --player**: name of the player on lichess you wish to analyze (atm works to display overall information such as rating/numbers of games played)

**-o --old**: how old are the game you wish to analyze in terms of months

**-m**: enable manual hard-coded url, otherwise uses selenium (can provide player and clock timing with -p and -c)

**-c**: clock timing you'd like to analyze amoung bullet, blitz, rapid, classical, all

**Default parameters**: -o 6 months // -p = bialx // -c blitz


## Provide

opening/nbr_win/nbr_match in a text file -> /output/opening_{player}_{clock}.txt


## Requirements


You'll need to install the following modules via *[pip](https://pip.pypa.io/en/stable/):

    $ pip install beautifulsoup4
    
    $ pip install selenium

    $ pipenv install requests


## Examples

```
python main.py -p bialx -o 6
```


## WIP

- [x] Automize the process of the infinite scroll to avoid having to get by hand the link of the pages we wish to work on.
- [x] submit via command-line options clock-timer for menu 1.
- [x] Submit via command-line options player
- [x] Submit via command-line options how old are the games we wish to analyze
- [ ] Data analysis on the different game/openings in order to get the most efficient opening, which lines are good/bad. TO DEBUG
- [ ] History chart
- [ ] use class instead of functions to provide a better library
- [ ] create a settings.py file to initialize global variable/parser and parameters
- [ ] refine the selenium scrapping in term of date to collect more data 

## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - Language used


## Authors

* **Bialx** - *Initial work* -

## License

This project is not licensed
