import mechanicalsoup

url = "https://lichess.org/"
user = "bialx"
browser = mechanicalsoup.StatefulBrowser()

page = browser.get(url)
login_form = page.soup.find("form", {"class":"signin"})

# browser.get_current_form().print_summary()
# browser.launch_browser()
