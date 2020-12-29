#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Declare Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests


# In[2]:


# Set Executable Path & Initialize Chrome Browser 
mars= {}

def scrape_all():
    executable_path = {'executable_path': '/Users/rubalbhullar/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
# In[3]:
# Visit the NASA Mars News Site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)


# In[4]:


# Parse Results HTML with BeautifulSoup
    html = browser.html
    news_soup = BeautifulSoup(html, "html.parser")
    slide_element = news_soup.find_all("li",class_="slide")


# # NASA Mars News

# In[177]:


#Scrape the Latest News Title and Paragraph Text
    for i in range (0,len(slide_element)):
        news_title = slide_element[i].find("div",class_="content_title")
        news_text = slide_element[i].find("div",class_="article_teaser_body")
    
        print("news title = " , news_title.text.strip(),"\n")
        print("news paragraph = " , news_text.text.strip(),"\n------------------------------------------------------------------------------------------------------------------")
    
    mars['news title'] = news_title
    mars['news paragraph'] = news_text


# # JPL Mars Space Images - Featured Image

# In[120]:


# Visit the NASA JPL (Jet Propulsion Laboratory) Site
    executable_path = {'executable_path': '/Users/rubalbhullar/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)


# In[121]:


# Ask Splinter to Go to Site and Click Button with Class Name full_image
    full_image_button = browser.find_by_id("full_image")
    full_image_button.click()


# In[122]:


# Find "More Info" Button and Click It
    browser.is_element_present_by_text("more info", wait_time=1)
    more_info_element = browser.find_link_by_partial_text("more info")
    more_info_element.click()


# In[123]:


# Parse Results HTML with BeautifulSoup
    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")


# In[124]:


    img_url = image_soup.select_one("figure.lede a img").get("src")
    img_url


# In[125]:


# Use Base URL to obtain absolute URL
    img_url = f"https://www.jpl.nasa.gov{img_url}"
    print(img_url)
    mars['img_url'] = img_url

# # Space Facts-Mars

# In[156]:


# Visit the Mars Facts Site
    executable_path = {'executable_path': '/Users/rubalbhullar/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_facts ="https://space-facts.com/mars/"
    browser.visit(mars_facts)


# In[154]:


    html = browser.html
    soup = BeautifulSoup(html,"html.parser")


# In[155]:


# Visit the Mars Facts Site Using Pandas to Read
    mars_df = pd.read_html("https://space-facts.com/mars/")
    right = list(mars_df[0][0])
    left = list (mars_df[0][1])
    space_facts_df = pd.DataFrame({"Description":right,"Value":left})
    space_facts_df 


# In[152]:


#Convert the data to a HTML table string
    news_titles = soup.find("table",class_="tablepress tablepress-id-p-mars")
    print(news_titles)
    mars['mars_facts'] = news_titles
# # Mars Hemispheres

# In[165]:


# Visit the USGS Astrogeology Science Center Site
    executable_path = {'executable_path': '/Users/rubalbhullar/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)


# In[166]:


    hemisphere_image_urls = []

# Get a List of All the Hemispheres
    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
            hemisphere = {}
    
    # Find Element on Each Loop to Avoid a Stale Element Exception
            browser.find_by_css("a.product-item h3")[item].click()
    
    # Find Sample Image Anchor Tag & Extract <href>
            sample_element = browser.find_link_by_text("Sample").first
            hemisphere["img_url"] = sample_element["href"]
    
    # Get Hemisphere Title
            hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # Append Hemisphere Object to List
            hemisphere_image_urls.append(hemisphere)
    
    # Navigate Backwards
            browser.back()

    mars['hemispheres'] = hemisphere_image_urls
    return mars 



