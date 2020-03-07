from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from selenium.webdriver.chrome.options import Options
import os
from time import sleep

links = [] #stores links for each representation page
target = [] #stores name of targeted country
location = [] #stores name of targetted representation's location (country)
address = [] #stores email address for its respective row


#Gathering links for each embassy webpage
filename = 'data/linksource.txt'
f = open(filename, "r")
hold = f.read().splitlines()
i = 0;
targetnum = [] #stores how long target occurs
targetraw = [] #stores occuring target countries in data
for line in hold:
    temp = line
    if temp[0] == '$':
        targetraw.append(line[1:])
        targetnum.append(i)
        i = 0
    else:
        i += 1
        links.append(temp)
numberofLinks = len(links)

#Make chromedriver headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_dir = "/usr/lib/chromium-browser/chromedriver"

#Get embassy page (contains email element) and initialize webdriver with test link
driver = driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_dir)
driver.get("https://www.google.com")


#iterate through different embassy links stored
#scrape each email from each link
set = False
for i in range(len(links)):
    driver.get(links[i])

    country = ""
    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')

    for match in soup.findAll('h2', attrs={'class':'entry-title'}):
        country = match.text

    for nation in range(len(targetraw)):
        if(targetraw[nation] in country):
            country = targetraw[nation]

    for match in soup.findAll('li', attrs={'id':'email'}):
        print("Fetched email " + match.text[5:] + " " + str(i) + "/" + str(numberofLinks) + " " + str(i/numberofLinks * 100)[:5] + "% for " + country)
        address.append(match.text[5:]) #prevents substring 'Email' from being added to email address string
        target.append(country)


#Package data into .csv file to be read and dealt with accordingly by mailer
print(str(len(target)) + " | " + str(len(address)))

for f in range(abs(len(address) - len(target))):
    target.append("blank")

df = pd.DataFrame({'Target':target,'Address':address})
df.to_csv('data/data.csv', index=False, encoding='utf-8')
