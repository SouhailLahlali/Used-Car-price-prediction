import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from Save_csv import save_data


##global variables
columns=["Name","Year","Location","Vendeur","Owner_type","Kilometers_Driven","Fuel_Type","Transmission","Puissance_fiscale","Puissance_dynamique","Price"]



def get_links(link):
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
        alert=soup.select(".col-c11  .alert")
        if alert==[]:

            name= soup.select_one('#details h3').text.replace("Occasion Maroc", "").strip()
            price=soup.find("p", class_="prix").text.replace("VENDUE", "").strip()
            #clearfix =[year,location ,owner ...]
            clearfix_values=soup.find_all("p",class_="tag")
            cell=soup.find("div",class_="cell")
            Puissance_fiscale=cell.find_all("p",class_='value')[4].text
            Puissance_dynamique=cell.find_all("p",class_='value')[5].text
            data["Name"]=name
            for i in range(1,8):
                data[columns[i]]=clearfix_values[i-1].text.strip()
            data["Puissance_fiscale"]=Puissance_fiscale.replace('\n','')
            data["Puissance_dynamique"]=Puissance_dynamique.replace('\n','')
            data["Price"]=price
            return data
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error fetching links from page : {e}")
        return []
#get_data("https://www.wandaloo.com/occasion/ford-focus-diesel-occasion-casablanca-maroc/41617.html")
i=0   

#put your cvs file of links here
for link in get_links("./csv_files/links2.csv"):
    i+=1
    print("Car n :",i)
    data = get_data(link)
    if data != 0:  
        save_data(data, columns, name="./csv_files/data.csv")
