import requests
import selenium
import os
import pandas as pd
import numpy as np
from selenium import webdriver
import time as time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options

link = 'link_entered_here'

get_soup = requests.get(link)

#get all the cell in the table

import bs4 as BeautifulSoup

parsed_soup = BeautifulSoup.BeautifulSoup(get_soup.text, 'html.parser')
rows = parsed_soup.find_all('td')

tables = [str(row.text) for row in rows]
links = [link for link in tables if 'link_contains' in link]

import time

def scrape_diamag(linker):

    options = Options()

    options.headless = True #making this driver headless so it can work in the background
    
    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
                
    driver.get(linker)

    make_soup = driver.page_source

    made_soup = BeautifulSoup.BeautifulSoup(make_soup, 'html.parser')

    content = [para.text for para in made_soup.select('p')[1:-21] if 'Output' not in para.text]

    code = [code.text for code in made_soup.select('code')]

    time.sleep(5)

    driver.quit()
    
    print(f'{linker[:5]} done')

    return content, code

def scrape_premag(linker):

    options = Options()

    options.headless = True #making this driver headless so it can work in the background
    
    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
                
    driver.get(linker)

    make_soup = driver.page_source

    made_soup = BeautifulSoup.BeautifulSoup(make_soup, 'html.parser')

    #content = [para.text for para in made_soup.select('p')[1:-21] if 'Output' not in para.text]

    code = [code.text for code in made_soup.select('pre')]

    time.sleep(15)

    driver.quit()
    
    print(f'{linker[-5:]} done')

    return code

topic_head = ['_'.join(link.split('-')[-4:]) for link in links]

data_collector = pd.DataFrame({'topic_head':topic_head, 'links' : links})

#if links don't begin with https, then it needs to be cleaned

#cleaning the links that have numbers at the starting

data_collector['links'] = [link[3:] if link[:3] != 'htt' else link for link in data_collector.links]

data_collector['data_code'] = [scrape_diamag(linker=link) for link in data_collector.links]

data_collector['data'] = data_collector.data_code.apply(lambda x: x[0])

data_collector['code'] = data_collector.data_code.apply(lambda x: x[1])

#below links did not get the code, so trying another tag 'xxx'
data_collector.loc[data_collector.code.apply(lambda x: len(x) == 0),'links']

#Long one, the link that did not collect any code is re-checked with a different tag for the code
data_collector.loc[data_collector.code.apply(lambda x: len(x) == 0),'code'] = data_collector.loc[data_collector.code.apply(lambda x: len(x) == 0),'links'].apply(lambda y: scrape_premag(y))

#Program completes by storing the data to csv
data_collector.to_csv('Data_to_store.csv')