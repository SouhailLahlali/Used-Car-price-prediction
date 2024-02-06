import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_links(index):
    list_of_links = []
    url = f'https://www.wandaloo.com/occasion/?marque=0&modele=0&budget=0&categorie=0&moteur=0&transmission=0&equipement=-&ville=0&vendeur=0&abonne=0&za&pg={index}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        li_tags = soup.find_all("li", class_=["even", "odd"])
        for li in li_tags:
            a_tag = li.find("a", class_="img")
            list_of_links.append(a_tag["href"])
        return list_of_links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching links from page {index}: {e}")
        return []

def save_links():
    data = {"links": []}
    start_time = time.time()
    for i in range(100, 161):
        print(f"Fetching links from page {i}")
        links = get_links(i)
        if links:
            data["links"].extend(links)
        else:
            print(f"No links fetched from page {i}")

    df = pd.DataFrame(data, columns=['links'])
    df.to_csv("links3.csv", index=False, header=True)
    print("Total time taken:", time.time() - start_time)

save_links()
