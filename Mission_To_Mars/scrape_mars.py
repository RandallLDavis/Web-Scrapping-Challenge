from flask import Flask, render_template, redirect
import scrape_mars
import pymongo

app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient()
db = client.mars_db
collection = df.mars_facts

@app.route('/')
def home():
    mars = list(df.mars_facts.find())
    print(mars)
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = scrape_mars.scrape()
    print(mars)
    mongo.db.collection.update({}, scrape_mars, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
