from app import app, mongo  # Import the Flask app and MongoDB connection

# Run inside Flask's application context
with app.app_context():
    plants_collection = mongo.db.plants  # Access MongoDB collection

    # Sample plant data
    sample_plants = [
        {"name": "Basil", "type": "Herb", "watering_frequency": 3, "sunlight_required": "Full Sun"},
        {"name": "Rosemary", "type": "Herb", "watering_frequency": 4, "sunlight_required": "Full Sun"},
        {"name": "Lavender", "type": "Herb", "watering_frequency": 7, "sunlight_required": "Full Sun"},
        {"name": "Tomato", "type": "Vegetable", "watering_frequency": 2, "sunlight_required": "Full Sun"},
        {"name": "Cucumber", "type": "Vegetable", "watering_frequency": 3, "sunlight_required": "Partial Shade"},
        {"name": "Carrot", "type": "Vegetable", "watering_frequency": 5, "sunlight_required": "Full Sun"},
        {"name": "Sunflower", "type": "Flower", "watering_frequency": 4, "sunlight_required": "Full Sun"},
        {"name": "Daisy", "type": "Flower", "watering_frequency": 5, "sunlight_required": "Partial Shade"},
        {"name": "Cactus", "type": "Succulent", "watering_frequency": 14, "sunlight_required": "Full Sun"},
        {"name": "Aloe Vera", "type": "Succulent", "watering_frequency": 10, "sunlight_required": "Partial Shade"},
        {"name": "Snake Plant", "type": "Succulent", "watering_frequency": 21, "sunlight_required": "Shade"},
        {"name": "Fern", "type": "Indoor", "watering_frequency": 7, "sunlight_required": "Shade"},
        {"name": "Spider Plant", "type": "Indoor", "watering_frequency": 5, "sunlight_required": "Partial Shade"},
        {"name": "Mint", "type": "Herb", "watering_frequency": 2, "sunlight_required": "Partial Shade"},
        {"name": "Lettuce", "type": "Vegetable", "watering_frequency": 3, "sunlight_required": "Partial Shade"}
    ]

    # Insert sample data
    plants_collection.insert_many(sample_plants)

print("Sample plants added successfully!")
