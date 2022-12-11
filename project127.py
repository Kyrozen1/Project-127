from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
data = requests.get(START_URL)

time.sleep(10)


#table1 = BeautifulSoup.find('table') 
#templist= [] 
#tablerows = table1.find_all('tr') 
#for tr in tablerows: 
    #td = tr.find_all('td') 
#row = [i.text.rstrip() for i in td] 
#temp_list.append(row)



def scrape():
    headers = {"name",	"distance",	"mass",	"radius"}
    sun_data = []

    soup = BeautifulSoup(data.text,"html.parser")
    table = BeautifulSoup.find("table")
    temp_list = []
    tablerows = table.find_all('tr') 

    for tr_tag in tablerows("tr"):

        td_tags = tr_tag.find_all("td")
    
        for index,td_tag in enumerate(td_tags):
            if index == 0:
                temp_list.append(td_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(td_tag.contents[0])
                except:
                    temp_list.append("")
        sun_data.append(temp_list)
    row = [i.text.rstrip() for i in td_tags] 
    temp_list.append(row)
    with open("Pscrapper.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(sun_data)
scrape()