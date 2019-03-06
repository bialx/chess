# chess

Tool to analyse game played on lichess. Maleability isnt great, i have to change the url used in my code if i want a different player, haven't automized the process yet.

Parameters
------------

user : bialx

clock timer : 15+2

how many months to consider : 2


Provide
------------
opening/nbr_win/nbr_match in a text file -> opening.txt


Requirements
------------

You'll need to install the following modules :


    $ pip install MechanicalSoup
    
    $ pip install beautifulsoup4
    
    $ pipenv install requests

WIP
------------

Automize the process of the infinite scroll to avoid having to get by hand the link of the pages we wish to work on. We currently have to analyse the requests made when we are scrolling. In fact lichess does a POST request to create different html pages as long as we are scrolling.

Submit via command-line options the player we choose, clock-timer, how many month to review.

Data analysis on the different game/openings in order to get the most efficient opening, which lines are good/bad.  
