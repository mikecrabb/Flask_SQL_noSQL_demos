from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gardening.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define the Plant model
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    watering_frequency = db.Column(db.Integer, nullable=False)
    sunlight_required = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Plant {self.name}>"

# ✅ Ensuring tables exist before running the app
with app.app_context():
    db.create_all()

# Route to display all plants
@app.route("/")
def index():
    plants = Plant.query.all()
    return render_template("index.html", plants=plants)

# Route to add a new plant
@app.route("/add", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        name = request.form["name"]
        type = request.form["type"]
        watering_frequency = int(request.form["watering_frequency"])
        sunlight_required = request.form["sunlight_required"]

        new_plant = Plant(
            name=name, type=type,
            watering_frequency=watering_frequency,
            sunlight_required=sunlight_required
        )
        db.session.add(new_plant)
        db.session.commit()

        return redirect("/")
    return render_template("add_plant.html")

# Route to delete a plant
@app.route("/delete/<int:plant_id>", methods=["POST"])
def delete_plant(plant_id):
    plant = Plant.query.get(plant_id)
    if plant:
        db.session.delete(plant)
        db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
