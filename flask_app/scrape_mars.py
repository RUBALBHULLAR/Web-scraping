#################################################
# Jupyter Notebook Conversion to Python Script
#################################################

# Dependencies and Setup  
from bs4 import BeautifulSoup
from splinter import Browser
import splinter
import pandas as pd
import datetime as dt

# # Set Executable Path & Initialize Chrome Browser 
executable_path = {'executable_path': '/Users/rubalbhullar/Downloads/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

#################################################
# NASA Mars News
#################################################
# NASA Mars News Site Web Scraper
def mars_news(browser):
    # Visit the NASA Mars News Site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    