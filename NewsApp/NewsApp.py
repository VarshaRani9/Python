import requests
import json
from termcolor import colored

apikey = "ef451d1605394a868173294be6ff1232"
query = input("What type of news you are looking for? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-05-25&sortBy=publishedAt&apiKey={apikey}"

r = requests.get(url)
news = json.loads(r.text)
# print(news)

for article in news["articles"]:
    print(colored('\033[1m'+article["title"], 'green'))
    print('\033[0m'+article["description"])
    print("\n\n")
