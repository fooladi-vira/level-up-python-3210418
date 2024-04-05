import random

def load_diceware_wordlist(filename):
    wordlist = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:  # Make sure the line has at least two parts
                wordlist.append(parts[1])  # Assuming the word is the second part
    return wordlist



def generate_passphrase(num_words, wordlist):
    # Generate a passphrase by selecting random words from the wordlist
    passphrase = ' '.join([random.choice(wordlist) for _ in range(num_words)])
    return passphrase

# Load the Diceware word list
filename = 'diceware.wordlist.asc'
wordlist = load_diceware_wordlist(filename)

# Generate a passphrase
num_words = 5  # Choose the number of words for the passphrase
passphrase = generate_passphrase(num_words, wordlist)
print(passphrase)
