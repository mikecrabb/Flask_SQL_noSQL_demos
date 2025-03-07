from app import app, db, Plant

# Ensure we run inside Flask's application context
with app.app_context():
    sample_plants = [
        Plant(name="Basil", type="Herb", watering_frequency=3, sunlight_required="Full Sun"),
        Plant(name="Rosemary", type="Herb", watering_frequency=4, sunlight_required="Full Sun"),
        Plant(name="Lavender", type="Herb", watering_frequency=7, sunlight_required="Full Sun"),
        Plant(name="Tomato", type="Vegetable", watering_frequency=2, sunlight_required="Full Sun"),
        Plant(name="Cucumber", type="Vegetable", watering_frequency=3, sunlight_required="Partial Shade"),
        Plant(name="Carrot", type="Vegetable", watering_frequency=5, sunlight_required="Full Sun"),
        Plant(name="Sunflower", type="Flower", watering_frequency=4, sunlight_required="Full Sun"),
        Plant(name="Daisy", type="Flower", watering_frequency=5, sunlight_required="Partial Shade"),
        Plant(name="Cactus", type="Succulent", watering_frequency=14, sunlight_required="Full Sun"),
        Plant(name="Aloe Vera", type="Succulent", watering_frequency=10, sunlight_required="Partial Shade"),
        Plant(name="Snake Plant", type="Succulent", watering_frequency=21, sunlight_required="Shade"),
        Plant(name="Fern", type="Indoor", watering_frequency=7, sunlight_required="Shade"),
        Plant(name="Spider Plant", type="Indoor", watering_frequency=5, sunlight_required="Partial Shade"),
        Plant(name="Mint", type="Herb", watering_frequency=2, sunlight_required="Partial Shade"),
        Plant(name="Lettuce", type="Vegetable", watering_frequency=3, sunlight_required="Partial Shade")
    ]

    db.session.add_all(sample_plants)
    db.session.commit()

    print("Sample plants added successfully!")
