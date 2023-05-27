import random
from string import ascii_lowercase, ascii_uppercase
alphabets = (ascii_lowercase, ascii_uppercase) #to make it easier for players and similar to the original, numbers and punctuation are not shifted.
def caesar(summary):
    step = random.randint(1,25) #step is randomly generated
    def shift(alphabet):
        return (alphabet[step:]) + ((alphabet[:step])) #returns the letters of the alphabet from the step to the end, then adds the letters from the begnning to the step. 
    joined_shifted_alphabets = ''.join(tuple(map(shift, alphabets)))
    joined_alphabets = ''.join(alphabets)
    table = str.maketrans(joined_alphabets, joined_shifted_alphabets) #creates a translation guide between the entire alphabet and the caesar shifted ones
    return summary.translate(table) #uses this guide to translate and return the summary. 

# more to come - basic substitution cipher and mixed substituion cipher