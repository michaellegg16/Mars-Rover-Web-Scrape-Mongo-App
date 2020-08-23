# Import libraries

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)



# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)



# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database    
    mars = mongo.db.mars.find_one()
    
    # Return the templace and Mars data
    return render_template("index.html", mars=mars)



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Store the Mars database in a variable
    mars = mongo.db.mars

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
