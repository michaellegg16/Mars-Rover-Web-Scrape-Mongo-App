from splinter import Browser
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
from selenium import webdriver
import time

def init_browser():
    executable_path = {"executable_path": "/chromedriver/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    # Mars News Data 
    browser = init_browser()
    mars = {}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # text = soup.find('div', class_='list_text')

    title = soup.find('div', class_='content_title')
    clean_title = title.text.strip()
    newsP = soup.find('div', class_='article_teaser_body').text
    # clean_newsP = newsP.text.strip()

    mars['title'] = title
    mars['paragraph'] = newsP

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

    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find('article', class_= "css-1dbjc4n r-1loqt21 r-16y2uox r-1wbh5a2 r-1udh08x r-1j3t67a r-o7ynqc r-6416eg")
    mars_weather_text = mars_weather.text.strip()

    mars['Weather'] = mars_weather_text

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

    hemi_data = []
    hems = soup.find_all('div', class_='item')

    for hem in hems:
        hem_name = hem.h3.text
        link = hem.a['href']
        browser.visit(url + link)
        soup = BeautifulSoup(browser.html, "html.parser")
    
        time.sleep(5)
        image = soup.find('div', class_='downloads')
        imageLink = image.find('a', target='_blank')['href']
    
        hem_info = {}
        hem_info['title'] = hem_name
        hem_info['img_url'] = imageLink
    
        hemi_data.append(hem_info)

    mars['Hemispheres'] = hemi_data

    browser.quit()


    return mars