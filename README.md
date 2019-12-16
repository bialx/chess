# CHESS ANALYZE

Tool to analyse game played on lichess. The idea is to gather as much data as we can on a player

## MENU

Menu -> 1. Use hard-coded url of a player on lichess to provide stats on the differents opening played by the player
               
               -> most played opening
               
               -> best/worst opening in term of win ratio
               
               -> details on a given opening (win ration according to every variation played)
         
         
     -> 2. You can give a player as a command line argument to display his overall rating and games played
           
           in bullet/blitz/rapid/classical


## Parameters

-v --verbose : increase verbosity

-p --player: name of the player on lichess you wish to analyze (atm works to display overall information such as rating/numbers of games played)

-o --old: how old are the game you wish to analyze in terms of months

Hard coded parameters : for menu 1. uses "Bialx" as base player

Default parameters: -o = 6 months // -p = bialx


## Provide

opening/nbr_win/nbr_match in a text file -> /output/opening.txt


## Requirements


You'll need to install the following modules :


    $ pip install MechanicalSoup

    $ pip install beautifulsoup4

    $ pipenv install requests
    
    
## Examples 

```
python main.py -p bialx -o 6
```


## WIP


Automize the process of the infinite scroll to avoid having to get by hand the link of the pages we wish to work on. We currently have to analyse the requests made when we are scrolling. In fact lichess does a POST request to create different html pages as long as we are scrolling.

Submit via command-line options clock-timer

Data analysis on the different game/openings in order to get the most efficient opening, which lines are good/bad.  



## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - Language used


## Authors

* **Bialx** - *Initial work* - 

## License

This project is not licensed 



