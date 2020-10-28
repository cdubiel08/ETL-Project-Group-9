from flask import Flask, render_template, jsonify


# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create variable for our connection string
conn = 'mongodb://localhost:27017'

# Pass connection string to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. 
# If the database doesn't already exist, our code will 
# create it automatically as soon as we insert a record.
db = client.covidcrypto_db

# Index route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Covid/Crypto Info <br/><br/>"
        f"Available Routes:<br/>"
        f"/data-json/<br/>"
        f"/date"
        
    )


# Define index/home route
@app.route('/data-json')
def data ():
    # Store the entire team collection in a list
    complete_data = list(db.data.find())
    print(complete_data)

    # Return the template with the players list passed in
    return jsonify(complete_data)

# Define route to insert new players into the database
@app.route('/<date>')
def date(date):
    return 
    

if __name__ == "__main__":
app.run(debug=True)