import requests
import argparse
from string import Template
from datetime import datetime
import re
import os
difficulties = {
    "8 kyu": "Easy",
    "7 kyu": "Easy",
    "6 kyu": "Intermediate",
    "5 kyu": "Intermediate"
}

endpoint = "https://www.codewars.com/api/v1/code-challenges/"
parser = argparse.ArgumentParser(prog="Codewars Formatter",
                                 description="Takes a Codewars Challenge URL and autoformats it into a .md file so I don't have to do it myself (tracking questions for my Obsidian PKM).")
parser.add_argument('-source', nargs = "?", choices = [
    "url",
    "file"], help="Specify to download from a URL (for a single challenge) or from a text file (for multiple challenges)")
parser.add_argument('path', type=str, help="Enter the path for the source")
args = parser.parse_args()
source, path = args.source, args.path


def link_data(url):
    challenge = requests.get(endpoint+(url).split('/')[4])
    response = challenge.json()
    name = response["name"]
    description = response["description"].split("```")
    description.append('')
    template = {
        'difficulty': difficulties[response["rank"]["name"]],
        'link': response["url"],
        'description': ''.join(["\n> " + i for i in (re.split(r'(\n+)',description[0])) if '\n\n' not in i]),
        'testcases': "```python" + description[1] + "```",
        'date': datetime.today().strftime('%Y/%m/%d')
    }
    return name, template


def f_temp(name, template):
    source = os.getcwd() + "/codewars/template.txt"
    name = ''.join(i for i in name if i not in '''\/:*?"<>|''')
    name = ' '.join([i.capitalize() for i in name.split()])
    destination = r"C:\Users\Annabel\Documents\class notes\04 - code" + "/" + name +'.md'
    with open(source, 'r') as f:
        src = Template(f.read())
        result = src.substitute(template)

    with open(destination, 'w+') as f:
        f.write(result)

if source == "file":
    with open(args.path) as file:
        for line in file:
            name, template = link_data(line.strip())
            f_temp(name, template)

elif source == "url":
    name, template = link_data(args.path)
    f_temp(name, template)
