import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import csv


def read_cvs_file(link):
    links_list=[]
    # Open the CSV file
    with open(link, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)
        # Skip the first row
        next(reader)
        # Iterate over each row in the CSV file
        for row in reader:
            links_list.append(row[0])
    return links_list
            
def get_data(url):
    data = {}
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        name= soup.select_one('#details h3').text.replace("Occasion Maroc", "").strip()
        prix=soup.find("p", class_="prix").text.replace("VENDUE", "").strip()
        print(prix)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching links from page : {e}")
        return []
    
url="https://www.wandaloo.com/occasion/ford-kuga-diesel-occasion-agadir-maroc/38140.html"
get_data(url)