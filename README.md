# chess

Tool to analyse game played on lichess. Maleability isnt great tho, i have to change the url used in my code if i want a different player, haven't automized the process yet for openings

Parameters
------------

user : bialx (hard-coded url to get openings)

clock timer : blitz (hard code clock timer for openings)

how many months to consider : 6 by default (command line option -o month or --old month)

-v --verbose : increase verbosity

-p --player: name of the player on lichess you wish to analyze (atm works to display overall information such as rating/numbers of games played)

-o --old: how old are the game you wish to analyze in terms of months

Provide
------------
opening/nbr_win/nbr_match in a text file -> /output/opening.txt


Requirements
------------

You'll need to install the following modules :


    $ pip install MechanicalSoup

    $ pip install beautifulsoup4

    $ pipenv install requests

WIP
------------

Automize the process of the infinite scroll to avoid having to get by hand the link of the pages we wish to work on. We currently have to analyse the requests made when we are scrolling. In fact lichess does a POST request to create different html pages as long as we are scrolling.

Submit via command-line options clock-timer

Data analysis on the different game/openings in order to get the most efficient opening, which lines are good/bad.  
