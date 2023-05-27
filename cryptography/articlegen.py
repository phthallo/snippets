import requests
from bs4 import BeautifulSoup
import re 
from ciphers import caesar

done = False
score = 0
article_title = ""
article_summary = ""
def articleGen():
    arti = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(arti.content, 'html.parser')
    arti_title = soup.find(class_="firstHeading").text
    try:
        soup.i.unwrap()
        soup.b.unwrap()
    except:
        articleGen()
    arti_summ = soup.find('p')
    arti_summ = arti_summ.text
    arti_summ = re.sub(r'\[.*?\]+', '', arti_summ)
    return arti_title, arti_summ

while not done:
    article = articleGen()
    while article[1] == "\n": #sometimes the scraping fails and arti_summ only contains a new line. if this happens, find another new article
        article = articleGen()
    print(caesar(article[1]))
    print("Article name?")
    answer = input("> ")
    if answer == str(article[0]):
        score += 1 
        print(f"Correct! Your score is now {score}.")
    elif answer == "quit":
        done = True