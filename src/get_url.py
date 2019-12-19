from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
import src.parse as parse
import src.thread as thread
import time

#Global variable used in the following .py
args = parse.make_parser() #build parser for command line arguments
working = 0
player = "bialx"



def get_url(dict_settings):
    global player, args
    if args.player: player = args.player
    dict_timing = {'bullet': 1, 'blitz': 2, 'rapid': 6, 'classical': 3}

    if dict_settings['clock'] == 'all': return f"https://lichess.org/@/{player}/all"
    else:
        return f"https://lichess.org/@/{dict_settings['player']}/search?perf={dict_timing[dict_settings['clock']]}&players.a=bialx&sort.field=d&sort.order=desc"



def scroll(base_url):
    global working, player, args
    working = 1
    thread_spin = thread.Spin()
    thread_spin.start()

    browser = webdriver.Firefox()
    browser.get(base_url)
# Selenium script to scroll to the bottom, wait 3 seconds for the next batch of data to load, then continue scrolling.  It will continue to do this until the page stops loading new data.
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(5)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            working = 0
            match=True

# Now that the page is fully scrolled, grab the source code.
    source_data = browser.page_source
    return source_data
