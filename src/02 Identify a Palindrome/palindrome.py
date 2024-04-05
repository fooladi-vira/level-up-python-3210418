import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards
    
def is_my_palindrome(s):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned = ''.join(filter(str.isalpha, s)).lower()
    # Check if the cleaned string is the same as its reverse
    return cleaned == cleaned[::-1]


# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_my_palindrome('hello world'))  # false
    print(is_my_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    
