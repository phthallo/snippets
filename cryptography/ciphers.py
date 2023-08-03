import random
from string import ascii_lowercase, ascii_uppercase, punctuation
caes_alphabets = [ascii_lowercase,ascii_uppercase] #to make it easier for players and similar to the original, numbers and punctuation are not shifted. works for ones that require shifts.
lowercase = ' '.join(ascii_lowercase).split() 
uppercase = ' '.join(ascii_uppercase).split()
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
def caesar(summary):
    step = random.randint(1,25) #step is randomly generated
    def shift(alphabet):
        return (alphabet[step:]) + ((alphabet[:step])) #returns the letters of the alphabet from the step to the end, then adds the letters from the begnning to the step. 
    joined_shifted_alphabets = ''.join(tuple(map(shift, caes_alphabets)))
    joined_alphabets = ''.join(caes_alphabets)
    table = str.maketrans(joined_alphabets, joined_shifted_alphabets) #creates a translation guide between the entire alphabet and the caesar shifted ones
    return summary.translate(table) #uses this guide to translate and return the summary. 

def piglatin(summary): # i know pig latin isn't a cipher but shush. currently it does not piglatinify stuff in brackets. 
    mus = summary.split() # to fix: work with punctuation properly
    trans = []
    for word in mus: 
        if word[0] not in vowels and word[0] in (lowercase + uppercase) and word[-1] in (lowercase+uppercase):
            trans.append(word[1:]+(word[0]).lower()+"ay")
        else:
            trans.append(word)
    return ' '.join(trans)

# more to come - basic substitution cipher and mixed substituion cipher
