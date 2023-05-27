# swaps out the letters provided by the user in dict.json. replace the '-' with what you suspect the letter to be.
import json
from string import ascii_letters, digits, punctuation
alphanumeric = ascii_letters + digits
misc = punctuation + " "
print("CHARACTER SUBSTIUTION TOOL - Paste encrypted text:")
summary = input("> ")
with open('cryptography/dict.json') as json_file:
    dict = json.load(json_file)
split = []
for i in summary:
    split.append(i.upper()) 
encrypt = []
dict_keys = list(dict.keys())
dict_values = list(dict.values())
for letter in split:
    if letter in alphanumeric:
        for i in range (0,25):
            if dict_keys[i] == letter:
                encrypt.append(dict_values[i])
    else: #if letter is punctuation or space, just add it in. also since it doesn't support non-latin characters, it'll just add it in here too. 
        encrypt.append(letter)
encrypt = ''.join(encrypt)
print(encrypt)