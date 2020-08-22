from splinter import Browser
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
from selenium import webdriver
from lxml import html
import time

def init_browser():
    executable_path = {"executable_path": "../chromedriver/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    # Mars News Data 
    browser = init_browser()
    mars = {}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    text = soup.find('div', class_='list_text')

    title = text.find('div', class_='content_title')
    clean_title = title.text.strip()
    newsP = text.find('div', class_='article_teaser_body')
    clean_newsP = newsP.text.strip()

    mars['title'] = clean_title
    mars['paragraph'] = clean_newsP

    # Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_path = soup.find('a', class_='button fancybox')['data-fancybox-href']
    full_path = 'https://www.jpl.nasa.gov' + image_path

    mars['Featured_Image'] = full_path

    # Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    # time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html)

    mars_weather = soup.find("div", attrs={"class": "css-1dbjc4n r-18u37iz", "data-testid": "tweet"})
    
    # mars_weather = mars_weather.text

    mars['Weather'] = mars_weather

    # mars_weather_tweet = mars_weather.find("p", "tweet-text").get_text()
    # test = soup.find("span", class_= "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0").text

    # spans = soup.find_all('span')

    # for span in spans:
        # if 'sol' and 'low' and 'high' in span.text.lower():
            # mars_weather = span.text
            # mars['Weather'] = mars_weather
            # break
        # else:
            # pass

    # Mars Facts
    url = 'https://space-facts.com/mars/'

    table = pd.read_html(url)
    table = pd.DataFrame(table[0])
    table.columns = ['Measurement', 'Record']
    table = table.set_index("Measurement")
    mars_facts = table.to_html(index = True, header =True)
    mars_facts = mars_facts.replace("/n", "")

    mars['Mars_Facts'] = mars_facts

    # Hemispheres
    import time
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    browser.visit(hemi_url)

    # Create and empty list for the data
    hemi_data = []

    # Find all the hemispheres and store them in a variable
    hems = soup.find_all('div', class_='item')


    for description in descriptions:
            link = description.a['href']
            hemi_data.append(link)

    # Base url
    base = 'https://astrogeology.usgs.gov'

    # Loop through each hemisphere and print the its image link
    for hem in hems:
        hem_name = hem.find('h3').text
        link = hem.find('a', 'href')
        
        browser.visit(base + link)
        soup = BeautifulSoup(browser.html, "html.parser")
        
        time.sleep(5)
        
        image = soup.find('div', class_='downloads')
        imageLink = image.find('a', target='_blank')['href']
        
        browser.back()
        
        hem_info = {}
        hem_info['title'] = hem_name
        hem_info['img_url'] = imageLink
        
        hemi_data.append(hem_info)
        print(imageLink)
        

    mars['Hemispheres'] = hemi_data

    # mars['Hems'] = hems

    browser.quit()

    return mars
