from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

from bson.objectid import ObjectId  # Import ObjectId for MongoDB IDs





app = Flask(__name__)

# Replace this with your actual MongoDB Atlas connection string
app.config["MONGO_URI"] = "mongodb+srv://gardenUser:V1XvFlA5snxPrnZQ@mikesgardentest.4ixuq.mongodb.net/garden_db?retryWrites=true&w=majority&appName=MikesGardenTest"
mongo = PyMongo(app)

# Reference the collection
plants_collection = mongo.db.plants

@app.route("/")
def index():
    plants = plants_collection.find()  # Fetch all plants from MongoDB
    return render_template("index.html", plants=plants)

@app.route("/add", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        name = request.form["name"]
        type = request.form["type"]
        watering_frequency = int(request.form["watering_frequency"])
        sunlight_required = request.form["sunlight_required"]

        new_plant = {
            "name": name,
            "type": type,
            "watering_frequency": watering_frequency,
            "sunlight_required": sunlight_required
        }

        plants_collection.insert_one(new_plant)
        return redirect(url_for("index"))

    return render_template("add_plant.html")

@app.route("/delete/<plant_id>", methods=["POST"])
def delete_plant(plant_id):
    plants_collection.delete_one({"_id": ObjectId(plant_id)})  # Convert ID to ObjectId
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
