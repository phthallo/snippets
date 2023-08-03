# checks your characters against another person's favourites to determine whether any of your characters are in their favourites.
# useful if you don't wanna go through 50 pages just to see if they've liked an OC of yours
# requires login in case of logged in users only, 
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
url = "https://toyhou.se/~account/login"


def auth(username, password):
    with requests.Session() as sess:
        r = sess.get(url)
        soup = BeautifulSoup(r.content, features="lxml")
        csrf = soup.find("meta", {"name":"csrf-token"})["content"]
        creds = {"username": username,
                "password": password,
                "_token": csrf}
        sess.post(url, data=creds)
        login = sess.get("https://toyhou.se/")
    return BeautifulSoup(login.content).prettify()
