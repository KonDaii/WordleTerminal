import requests
from bs4 import BeautifulSoup
import random

url = 'https://www.thefreedictionary.com/5-letter-words.htm'

# Send a GET request to the website and fetch its content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the website using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all text from the HTML content
    text = soup.get_text()

    # Split the text into a list of words
    words_list = text.split()

    # Filter words that are 5 characters long
    words_list = [word for word in words_list if len(word) == 5]

    # Pick a random word from the filtered list
    random_word = random.choice(words_list)

    # Print the randomly selected word
    print("Random word:", random_word)
else:
    print("Failed to fetch the website:", response.status_code)
