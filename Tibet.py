#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:21:24 2020

@author: mpang
"""

import os
import re
import random
from bs4 import BeautifulSoup
import requests
import time
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Counter
from urllib.request import urlopen


os.chdir('/Users/mpang/Desktop/XizangFull')

counter = 1883
text_cont = ''

path_to_chromedriver = '/Users/mpang/Downloads/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.get('http://epaper.chinatibetnews.com/xzrb/xzrb/html/2010-01/31/node_7.htm')

for i in range(0,1):
    elems = browser.find_elements_by_xpath('//*[@id="logoTable"]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td[1]/table[2]/tbody/tr/td/table[2]/tbody/tr[4]/td/div/table/tbody/tr/td/a[@href]')
    elems = [a.get_attribute('href') for a in elems]
    print(elems)

        
    for j in elems:
        time.sleep(1)
        browser.get(j)
        html = browser.find_element_by_xpath(".//html")
        text_cont = html.text
            
        counter += 1
        fileName = "Case" + str(counter) + ".txt"
        print(fileName)
        textFile = open(fileName, 'w')
        textFile.write(text_cont)
        textFile.close()
        print("File has been closed")

