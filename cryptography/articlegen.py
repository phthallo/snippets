import requests
from bs4 import BeautifulSoup
import re 
from ciphers import caesar, piglatin
import random

done = False
score = 0
article_title = ""
article_summary = ""
ciphers = [caesar, piglatin]
class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def articleGen():
    arti = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(arti.content, 'html.parser')
    arti_title = soup.find(class_="firstHeading").text
    try:
        soup.i.unwrap()
        soup.b.unwrap()
    except:
        articleGen()
    arti_summ = soup.find('p') #extract test that is contained with the <p> tags
    arti_summ = arti_summ.text
    arti_summ = re.sub(r'\[.*?\]+', '', arti_summ) #remove linked references to other articles [[like so]]
    return arti_title, arti_summ

print(f"""   _    _ _   _ _____ _   _____________ ___________ _____ ___ 
  | |  | | | | |  _  | | / |_   _| ___ |  ___|  _  |_   _/ _ \ 
  | |  | | |_| | | | | |/ /  | | | |_/ | |__ | | | | | |/ /_\ \ 
  | |/\| |  _  | | | |    \  | | |  __/|  __|| | | | | ||  _  | 
  \  /\  | | | \ \_/ | |\  \_| |_| |   | |___| |/ / _| || | | | 
   \/  \/\_| |_/\___/\_| \_/\___/\_|   \____/|___/  \___\_| |_/
  ═════════════════════════════════════════════════════════════
  The aim of the game is to guess the name of a random encoded Wikipedia article.
  For ones that are encoded using ciphers {color.BOLD}cipherhelp.py{color.END} and {color.BOLD}commonletters.py{color.END} exist 
  to help with manual deciphering. Type "quit" to end the game.
""")

while not done:
    article = articleGen()
    while article[1] == "\n": #sometimes the scraping fails and arti_summ only contains a new line. if this happens, find another new article
        article = articleGen()
    print("\n"+random.choice(ciphers)(article[1])) #selects a random cipher and calls it using the summary 
    print(f"{color.BOLD}\n// Article name?{color.END}")
    answer = input("> ")
    if answer.lower() == str(article[0]).lower(): # case insensitive
        score += 1 
        print(f"// Correct! Your score is now {score}.")
    elif answer == "quit":
        print(f"// Game ended. Your score was {score}.")
        done = True
    else: 
        print(f"// The answer was '{str(article[0])}'!")

