from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from selenium.webdriver.chrome.options import Options
import os

links = [] #stores links for each representation page
target = [] #stores name of targeted country
location = [] #stores name of targetted representation's location (country)
address = [] #stores email address for its respective row


#Gathering links for each embassy webpage
filename = 'linksource.txt'
f = open(filename, "r")
hold = f.read().splitlines()
for line in hold:
    links.append(line)
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
for i in range(len(links)):
    temp = links[i]
    driver.get(temp)

    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')

    country = ""

    for match in soup.findAll('h2', attrs={'class':'entry-title'}):
        country = match.text

    for match in soup.findAll('li', attrs={'id':'email'}):
        print("Fetched email " + match.text[5:] + " " + str(i) + "/" + str(numberofLinks) + " " + str(i/numberofLinks * 100)[:5] + "% for " + country)
        address.append(match.text[5:]) #prevents substring 'Email' from being added to email address string
        target.append(country)

#Package data into .csv file to be read and dealt with accordingly by mailer
df = pd.DataFrame({'Target':target,'Address':address})
df.to_csv('data.csv', index=False, encoding='utf-8')
