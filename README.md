# Mars-Rover-Web-Scrape-Mongo-App

### Task

* Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

#### Step 1 - Scraping

* Use Jupyter Notebook, BeautifulSoup, Pandas, and Splinter to complete the initial scraping and analysis.

* NASA Mars News:
   * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 
   * Assign the text to variables that you can reference later.
   
![NewsImage](https://github.com/michaellegg16/Mars-Rover-Web-Scrape-Mongo-App/blob/master/Mission_to_Mars/Screenshots/NewsInfo.png)
   
* JPL Mars Space Images - Featured Image:
   * Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
   * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
   * Make sure to find the image url to the full size `.jpg` image.
   * Make sure to save a complete url string for this image.   
   
![FeaturedImage](https://github.com/michaellegg16/Mars-Rover-Web-Scrape-Mongo-App/blob/master/Mission_to_Mars/Screenshots/FeaturedImage.png)

* Mars Weather:
   * Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. 
   * Save the tweet text for the weather report as a variable called `mars_weather`.
   
![MarsWeather](https://github.com/michaellegg16/Mars-Rover-Web-Scrape-Mongo-App/blob/master/Mission_to_Mars/Screenshots/MarsWeather.png)

* Mars Facts:
    * Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    * Use Pandas to convert the data to a HTML table string.

![MarsFacts](https://github.com/michaellegg16/Mars-Rover-Web-Scrape-Mongo-App/blob/master/Mission_to_Mars/Screenshots/SpaceFactsTable.png)
![HTMLTable](https://github.com/michaellegg16/Mars-Rover-Web-Scrape-Mongo-App/blob/master/Mission_to_Mars/Screenshots/HTMLTable.png)

* Mars Hemispheres:
    * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
    * Click each of the links to the hemispheres in order to find the image url to the full resolution image.
    * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 
    * Use a Python dictionary to store the data using the keys `img_url` and `title`.
    * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    
![Hemispheres](https://github.com/michaellegg16/Mars-Rover-Web-Scrape-Mongo-App/blob/master/Mission_to_Mars/Screenshots/HemisphereDictionary.png)


#### Step 2 - 
    
    
    
    
    
    
