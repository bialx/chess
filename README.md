# CHESS ANALYZE

Tool to analyse game played on lichess. Maleability isnt great tho, i have to change the url used in my code if i want a different player, haven't automized the process yet for openings

MENU
------------

Menu -> 1. Use hard-coded url of a player on lichess to provide stats on the differents opening played by the player
               
               -> most played opening
               
               -> best/worst opening in term of win ratio
               
               -> details on a given opening (win ration according to every variation played)
         
         
     -> 2. You can give a player as a command line argument to display his overall rating and games played
           
           in bullet/blitz/rapid/classical


Parameters
------------

-v --verbose : increase verbosity

-p --player: name of the player on lichess you wish to analyze (atm works to display overall information such as rating/numbers of games played)

-o --old: how old are the game you wish to analyze in terms of months

Hard coded parameters : for menu 1. uses "Bialx" as base player

Default parameters: -o = 6 months // -p = bialx


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





## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


