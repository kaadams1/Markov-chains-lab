"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text = open(file_path).read()
    
    return text
    



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    i = 0
    words = text_string.split()

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []
        chains[key].append(value)
            
    return chains


def make_text(chains):
    """Return text from chains."""
    
    random_key = choice(list(chains.keys())) #gives sorted list of tuples
    
    if random_key[0][0].isupper():
        words = [random_key[0], random_key[1]] #gives us our first two words in the list
        random_word = choice(chains[random_key]) #gives us our next word to start the next tuple

        while random_word is not None: #while we still have words to choose from
            random_key = (random_key[1], random_word) #create new key from the second element in key plus the random word
            words.append(random_word) #add random word to the words list
            
            if random_key in chains:
                random_word = choice(chains[random_key])  #continue the choice loop/selection of random words until while loop breaks
            else:
                break

        return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
