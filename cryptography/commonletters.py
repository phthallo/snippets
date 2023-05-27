# takes input and analyses input for top 5 encrypted letters, determines percentage
from string import ascii_letters, digits
import collections
from collections import Counter
print("COMMON LETTERS - Paste encrypted text:")
summary = input("> ")
split = []
for i in summary:
    if i in ascii_letters or i in digits: 
        split.append(i.upper()) #strip out punctuation and change all to upper
common = collections.Counter(split).most_common(5)
counter = Counter((''.join(split))) # counts number of occurrences of every letter in the string w/ stripped out punctuation
print("MOST COMMON LETTERS BY %: \n(The five most common letters in the English language are E, T, A, O and I.)")
for i in range(0,5):
    print(f"{i+1}. {common[i][0]} - {round(((common[i][1]))/len(split),4)*100}%") 
    # where i refers to how common it is 
    # common[i][0] takes the value of the letter itself 
    # common[i][1] takes the value of its occurrences
    # turned into a percentage/overall characters, rounded (kinda) but it's *sort of* broken.


