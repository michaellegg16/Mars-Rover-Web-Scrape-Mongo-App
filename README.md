# Mars-Rover-Web-Scrape-Mongo-App

### Task

* Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

#### Step 1:

* Use Jupyter Notebook, BeautifulSoup, Pandas, and Splinter to complete the initial scraping and analysis.
* NASA Mars News:
   * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
* JPL Mars Space Images - Featured Image
   * Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

   * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

   * Make sure to find the image url to the full size `.jpg` image.

   * Make sure to save a complete url string for this image.   
