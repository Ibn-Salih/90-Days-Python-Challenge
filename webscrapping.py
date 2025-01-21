# - Topics:
# - Introduction to web scraping using BeautifulSoup and requests.
# - Parsing HTML and extracting data.
# - Project:
# - Create a program that scrapes a website 
# (e.g., news headlines from a news site) and displays the results.




import requests
from bs4 import BeautifulSoup

def get_headlines():
    url = input("Enter url eg'https://www.bbc.com/news' : ")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    while True:
        change_tag = input("Enter tag 'a', 'h1', 'h2', etc: ")
        if change_tag == "h1":
            headlines = soup.find_all("h1")
        else:
            headlines = soup.find_all(change_tag)
        
        for headline in headlines[:5]:
            print(headline.get_text())

        more_headlines = input("Do you want to see more headlines? (yes/no): ")
        if more_headlines.lower() != "yes":
            break

    

if __name__ == "__main__":
    get_headlines()
