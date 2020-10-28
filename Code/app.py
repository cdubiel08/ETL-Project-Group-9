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
        f"Available Routes: <br/>"
        f"/data-json/ <br/>"
        f"    - Returns JSON of entire dataset <br/>"
        f"/date/ <br/>"
        f"    - input date format: YYYY-MM-DD, returns data for specific date <br/>"
        f"/covid_countries/country <br/>"
        f"    - input country name requires proper casing (e.g. \"Canada\" not \"canada\"), returns data for specific country over entire date range of dataset"      
    )


# Define index/home route
@app.route('/data-json')
def data ():
    # Store the entire team collection in a list
    complete_data = list(db.data.find())
    for item in complete_data:
        item.pop('_id')

    # Return the template with the players list passed in
    return jsonify(complete_data)

# Define route to insert new players into the database
@app.route('/<date>')
<<<<<<< HEAD
def date_search(date):
    result = list(db.data.find({'date': date}))
    result[0].pop('_id')
    return jsonify(result)

@app.route('/covid_countries/<country>')
def countries(country):
    results=list(db.data.find())
    result_json = []
    for result in results:
        date = str(result['date'])
        for _country in result['countries']:
            if _country['country_name'] == country:
                result_json.append({date:_country})

                #to use pymongo query instead of the mess above: MongoDB -- db.data.find({ country.country_name : country })
    
    return jsonify(result_json)

=======
def date(date):
    return 
    
>>>>>>> ff46ec7ac5332a8c2987a8c8306ed4cdca7a14f3

if __name__ == "__main__":
app.run(debug=True)