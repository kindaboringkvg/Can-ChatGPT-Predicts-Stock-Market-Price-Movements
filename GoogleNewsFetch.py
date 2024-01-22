from bs4 import BeautifulSoup
import requests
import csv


url = "ENTER URL OF GOOGLE NEWS WEBSITE"
response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, "html.parser")


articles = soup.find_all("article")


data_list = []


for article in articles:
   
    headline_element = article.find("h3", class_="ipQwMb ekueJc RD0gLb")
    headline = headline_element.get_text() if headline_element else "N/A"
    
    
    source_element = article.find("a", class_="wEwyrc AVN2gc uQIVzc Sksgp")
    source = source_element.get_text() if source_element else "N/A"
    
   
    published_date_element = article.find("time")
    published_date = published_date_element["datetime"] if published_date_element else "N/A"
    
    
    data_list.append({"headline": headline, "source": source, "published_date": published_date})


csv_filename = "google_news.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["headline", "source", "published_date"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for data in data_list:
        writer.writerow(data)

print("Data inserted", csv_filename)
