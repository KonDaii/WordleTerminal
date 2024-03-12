import requests
from bs4 import BeautifulSoup
import random
import re

# Replace 'https://www.thefreedictionary.com/5-letter-words.htm' with the URL of the website containing words
url = 'https://eslforums.com/5-letter-words/'

# Send a GET request to the website and fetch its content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the website using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all text from the HTML content
    text = soup.get_text()

    # Find all words using regular expression and convert them to lowercase
    words_list = re.findall(r'\b[A-Za-z]{5}\b', text.lower())

    # Remove duplicates from the list
    unique_words_list = list(set(words_list))

    # Pick a random word from the list
    random_word = random.choice(unique_words_list)

    # Print the randomly selected word
    print("Random word:", random_word)
else:
    print("Failed to fetch the website:", response.status_code)
