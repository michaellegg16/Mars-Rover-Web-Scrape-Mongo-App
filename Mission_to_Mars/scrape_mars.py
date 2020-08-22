from splinter import Browser
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
from selenium import webdriver
from lxml import html
import time

# Create the init_browser function
def init_browser():
    # Set the path for chromedriver
    executable_path = {"executable_path": "../chromedriver/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# Create the scrape function
def scrape():
    browser = init_browser()

    # First, scrape the mars News Data 

    #Create a dictionary to hold all the data to upload to the database
    mars = {}

    # Set the url and have the browser visit it
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Scrape the page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Get the text from the page
    text = soup.find('div', class_='list_text')

    # Get the News Title test and strip it
    title = text.find('div', class_='content_title')
    clean_title = title.text.strip()

    # Get the paragraph text and strip it
    newsP = text.find('div', class_='article_teaser_body')
    clean_newsP = newsP.text.strip()

    # Store the news title and paragraph text in the dictionary
    mars['title'] = clean_title
    mars['paragraph'] = clean_newsP

    # Next, save the url of the featured image on the provided NASA link

    # SEt the Featured Image url and have the browser visit it
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=mars'
    browser.visit(url)

    # time.sleep(5)

    # Srape the page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Get the featured image path
    image_path = soup.find('a', class_='button fancybox')['data-fancybox-href']
    full_path = 'https://www.jpl.nasa.gov' + image_path

    # Store the featured image path in the dictionary
    mars['Featured_Image'] = full_path


    # Next, scrape the latest Mars weather tweet


    # Set the new url and have the browser visit it
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    # time.sleep(5)

    # Scrape the page into soup
    html = browser.html
    soup = BeautifulSoup(html)

    # Get the latest tweet's text
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

    # mars Facts

    # Next, use Pandas to scrape the facts table from the url provided

    # Set the url
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    # Use Pandas to read the HTML and store it in a dataframe
    table = pd.read_html(url)
    table = pd.DataFrame(table[0])

    # Label the table columns and set the index
    table.columns = ['Measurement', 'Record']
    table = table.set_index("Measurement")

    # Convert the table to HTML and clean it a bit
    mars_facts = table.to_html(index = True, header =True)
    mars_facts = mars_facts.replace("/n", "")

    # Store the table in the dictionary
    mars['mars_Facts'] = mars_facts


    # Last, obtain information and images of the Mars Hemispheres


    # Hemispheres
    import time

    # Set new url
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # Visit the new url
    browser.visit(hemi_url)

    # Select the html and parse it
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Create an empty list for the data
    # hemi_data = []
    hem_names = []
    hem_imgs = []

    # Find all the hemispheres and store them in a variable
    hems = soup.find_all('div', class_='item')

    # Base url
    base = 'https://astrogeology.usgs.gov'

    # Loop through each hemisphere and print the its image link
    for hem in hems:
        hem_name = hem.h3.text
        link = hem.a['href']
        
        browser.visit(base + link)
        soup = BeautifulSoup(browser.html, "html.parser")
        
        # time.sleep(5)
        
        image = soup.find('div', class_='downloads')
        imageLink = image.find('a', target='_blank')['href']
        
        browser.back()
        
        hem_info = {}
        hem_info['Hemisphere_name'] = hem_name
        hem_info['img_url'] = imageLink
        
        hem_names.append(hem_info['Hemisphere_name'])
        hem_imgs.append(hem_info['img_url'])
        print(imageLink)

    browser.quit()
        

    mars['HemisphereNames'] = hem_names
    mars['HemisphereImgs'] = hem_imgs

    # mars['Hems'] = hems

    browser.quit()

    return mars
