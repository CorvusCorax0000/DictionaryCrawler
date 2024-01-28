import requests
from bs4 import BeautifulSoup
import os


def fetch_website_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    classes = ['hw dhw', 'pos dpos', 'pron dpron', 'def ddef_d db']
    elements = [soup.find(class_=class_name) for class_name in classes]
    return elements


def scrape(vocab):
    vocab = vocab.lower()
    url = f"https://dictionary.cambridge.org/dictionary/english/{vocab}"
    elements = fetch_website_content(url)
    newList = []
    for element in elements:
        if element:
            result = element.text
            newList.append(result)
    print(f'{newList[0]} ({newList[1]}) {newList[2]}: {newList[3]}')
    return newList


while True:
    vocabList = []
    while True:
        vocab = input("Enter a word (or press enter to stop): ")
        if vocab == "":
            break
        vocabList.append(vocab)

    for i in vocabList:
        i = scrape(i)
    
    again = input("Do you want to run the app again? (y/n): ")
    if again.lower() != 'y':
        break

os.system('pause')
