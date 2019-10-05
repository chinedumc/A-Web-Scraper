# -*- coding: utf-8 -*-
"""
A Web scraper which fetches the names and h-index of Computer Science 
Professors on the first 25 pages of google scholar

"""
#Import necessary utilities
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#Opening The file we will write our details to
FILENAME = 'Computer_Science_Professors_and_Their_h-indices.csv'
F = open(FILENAME, 'w')

HEADERS = 'Name Of Professor, h-index \n'
F.write(HEADERS)


#container = containers[0]
INIT_PG = 0
URL = ('https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=computer+science+professor&before_author=i-Gn_w-KAQAJ&astart=0')


while INIT_PG <= 240:
    #Opening up the content and grabbing the page
    UCLIENT = uReq(URL)

    #Read the Webpage
    PAGE_HTML = UCLIENT.read()

    #html parsing
    PAGE_SOUP = soup(PAGE_HTML, "html.parser")
    CONTAINERS = PAGE_SOUP.findAll("div", {"class":"gs_ai_t"})
    CONTAINER = CONTAINERS[0]
    #Grab Prof details on page
    for CONTAINER in CONTAINERS:
        PROF_NAME = CONTAINER.a.text
        PROF_WEBPAGE_TAG = CONTAINER.a['href'].split('?')[1].split('=')[2]

        #Fetching the h-index for each Prof
        PROF_PAGE_URL = 'https://scholar.google.com/citations?hl=en&user=' + PROF_WEBPAGE_TAG

        #Opening up the content and grabbing the page for each prof
        UCLIENT = uReq(PROF_PAGE_URL)

        #Read the Webpage
        PROF_PAGE_HTML = UCLIENT.read()

        #html parsing
        PROF_SOUP = soup(PROF_PAGE_HTML, "html.parser")

        PROF_H_INDEX = PROF_SOUP.findAll('td', {'class':'gsc_rsb_std'})[2].text


        #Print out all of the names and Ids of the profs on current page
        F.write(PROF_NAME.replace(',', '') + ',' + PROF_H_INDEX + '\n')

        #Checking the data collected
        print(PROF_NAME + ',' + PROF_H_INDEX + '\n')

    #Grab the next page
    PAGE_CONTAINERS = PAGE_SOUP.findAll("button", {"aria-label":"Next"})
    PAGE_CONTAINER = PAGE_CONTAINERS[0]

    NXT_PG = PAGE_CONTAINER['onclick'].split('\\')[9]

    INIT_PG = INIT_PG + 10

    URL = ('https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=computer+science+professor&after_author=' + NXT_PG[3:] +'&astart='+ str(INIT_PG))

    #Closing the webpage
    UCLIENT.close()
F.close()
    #print(url)
