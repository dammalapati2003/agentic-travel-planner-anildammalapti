# data_feed.py

# WEATHER DATA
WEATHER_DATA = {
    "New Delhi": {
        "pattern": ["Sunny", "Hot", "Cloudy"],
        "avg_temp": 33
    },
    "Paris": {
        "pattern": ["Sunny", "Cloudy", "Rainy"],
        "avg_temp": 25
    },
    "Tokyo": {
        "pattern": ["Rainy", "Humid", "Cloudy"],
        "avg_temp": 28
    },
    "London": {
        "pattern": ["Cloudy", "Rainy", "Windy"],
        "avg_temp": 20
    },
    "Dubai": {
        "pattern": ["Hot", "Sunny", "Dry"],
        "avg_temp": 38
    },
    "Rome": {
        "pattern": ["Sunny", "Mild", "Windy"],
        "avg_temp": 27
    },
    "New York": {
        "pattern": ["Sunny", "Windy", "Rainy"],
        "avg_temp": 22
    },
    "Singapore": {
        "pattern": ["Humid", "Rainy", "Cloudy"],
        "avg_temp": 30
    },
    "Sydney": {
        "pattern": ["Mild", "Windy", "Sunny"],
        "avg_temp": 26
    },
    "Bangkok": {
        "pattern": ["Hot", "Humid", "Rainy"],
        "avg_temp": 32
    },
    "Default": {
        "pattern": ["Sunny", "Cloudy", "Windy"],
        "avg_temp": 27
    }
}

#  POINTS OF INTEREST DATA
POI_DATA = {
    "New Delhi": {
        "historic": [
            {"name": "Red Fort", "desc": "Historic Mughal fortress", "visit_time": "2 hrs", "cost": "₹300", "travel_time_to_next": "15 min"},
            {"name": "Qutub Minar", "desc": "UNESCO world heritage site", "visit_time": "1.5 hrs", "cost": "₹200", "travel_time_to_next": "20 min"},
            {"name": "Humayun’s Tomb", "desc": "Mughal era monument", "visit_time": "1 hr", "cost": "₹250", "travel_time_to_next": "20 min"},
            {"name": "India Gate", "desc": "War memorial and national landmark", "visit_time": "30 min", "cost": "Free", "travel_time_to_next": "10 min"},
            {"name": "Rashtrapati Bhavan", "desc": "Presidential residence", "visit_time": "1 hr", "cost": "₹50", "travel_time_to_next": "15 min"}
        ],
        "food": [
            {"name": "Karim’s", "desc": "Iconic Mughlai restaurant", "visit_time": "1 hr", "cost": "₹500", "travel_time_to_next": "10 min"},
            {"name": "Connaught Place", "desc": "Street food and cafes", "visit_time": "2 hrs", "cost": "₹800", "travel_time_to_next": "15 min"},
            {"name": "Saravana Bhavan", "desc": "Famous South Indian restaurant", "visit_time": "1 hr", "cost": "₹300", "travel_time_to_next": "10 min"}
        ],
        "nature": [
            {"name": "Lodhi Garden", "desc": "Beautiful historical park", "visit_time": "2 hrs", "cost": "Free", "travel_time_to_next": "20 min"},
            {"name": "Garden of Five Senses", "desc": "Themed garden with sculptures", "visit_time": "1.5 hrs", "cost": "₹100", "travel_time_to_next": "15 min"}
        ],
        "shopping": [
            {"name": "Dilli Haat", "desc": "Cultural crafts bazaar", "visit_time": "1.5 hrs", "cost": "₹30 entry", "travel_time_to_next": "15 min"},
            {"name": "Sarojini Nagar Market", "desc": "Affordable fashion and accessories", "visit_time": "2 hrs", "cost": "Varies", "travel_time_to_next": "20 min"}
        ]
    },

    "Paris": {
        "historic": [
            {"name": "Eiffel Tower", "desc": "Iconic landmark of Paris", "visit_time": "2 hrs", "cost": "€25", "travel_time_to_next": "10 min"},
            {"name": "Louvre Museum", "desc": "World’s largest art museum", "visit_time": "3 hrs", "cost": "€17", "travel_time_to_next": "15 min"},
            {"name": "Notre-Dame Cathedral", "desc": "Gothic cathedral", "visit_time": "1 hr", "cost": "Free", "travel_time_to_next": "10 min"},
            {"name": "Arc de Triomphe", "desc": "Monument honoring French soldiers", "visit_time": "45 min", "cost": "€13", "travel_time_to_next": "15 min"},
            {"name": "Palace of Versailles", "desc": "Royal château with gardens", "visit_time": "3 hrs", "cost": "€18", "travel_time_to_next": "40 min"}
        ],
        "food": [
            {"name": "Le Jules Verne", "desc": "Fine dining in Eiffel Tower", "visit_time": "1.5 hrs", "cost": "€120", "travel_time_to_next": "10 min"},
            {"name": "Montmartre Café", "desc": "Local food and coffee culture", "visit_time": "1 hr", "cost": "€30", "travel_time_to_next": "15 min"},
            {"name": "L’As du Fallafel", "desc": "Popular falafel eatery", "visit_time": "45 min", "cost": "€12", "travel_time_to_next": "10 min"}
        ],
        "shopping": [
            {"name": "Champs-Élysées", "desc": "Famous shopping avenue", "visit_time": "2 hrs", "cost": "Varies", "travel_time_to_next": "20 min"},
            {"name": "Galeries Lafayette", "desc": "Luxury department store", "visit_time": "1.5 hrs", "cost": "Varies", "travel_time_to_next": "15 min"}
        ],
        "nature": [
            {"name": "Luxembourg Gardens", "desc": "Peaceful gardens in the city center", "visit_time": "1.5 hrs", "cost": "Free", "travel_time_to_next": "10 min"},
            {"name": "Seine River Walk", "desc": "Scenic riverside promenade", "visit_time": "1 hr", "cost": "Free", "travel_time_to_next": "10 min"}
        ]
    },

    "Tokyo": {
        "culture": [
            {"name": "Senso-ji Temple", "desc": "Ancient Buddhist temple", "visit_time": "1.5 hrs", "cost": "Free", "travel_time_to_next": "15 min"},
            {"name": "Meiji Shrine", "desc": "Shinto shrine surrounded by forest", "visit_time": "1 hr", "cost": "Free", "travel_time_to_next": "20 min"},
            {"name": "Tokyo National Museum", "desc": "Japan’s oldest national museum", "visit_time": "2 hrs", "cost": "¥1000", "travel_time_to_next": "15 min"}
        ],
        "shopping": [
            {"name": "Akihabara", "desc": "Electronics and anime hub", "visit_time": "2 hrs", "cost": "Varies", "travel_time_to_next": "10 min"},
            {"name": "Shibuya Crossing", "desc": "Famous intersection with shops", "visit_time": "1 hr", "cost": "Varies", "travel_time_to_next": "15 min"},
            {"name": "Ginza District", "desc": "Luxury shopping and dining area", "visit_time": "2 hrs", "cost": "Varies", "travel_time_to_next": "20 min"}
        ],
        "food": [
            {"name": "Tsukiji Market", "desc": "World-famous sushi market", "visit_time": "1.5 hrs", "cost": "¥3000", "travel_time_to_next": "15 min"},
            {"name": "Ichiran Ramen", "desc": "Popular ramen chain", "visit_time": "1 hr", "cost": "¥1200", "travel_time_to_next": "10 min"}
        ],
        "nature": [
            {"name": "Ueno Park", "desc": "Cherry blossom viewing spot", "visit_time": "2 hrs", "cost": "Free", "travel_time_to_next": "10 min"}
        ]
    },

    "London": {
        "historic": [
            {"name": "Big Ben", "desc": "Iconic clock tower", "visit_time": "1 hr", "cost": "Free", "travel_time_to_next": "15 min"},
            {"name": "Buckingham Palace", "desc": "Royal residence", "visit_time": "2 hrs", "cost": "£30", "travel_time_to_next": "20 min"},
            {"name": "British Museum", "desc": "Vast museum of history & art", "visit_time": "3 hrs", "cost": "Free", "travel_time_to_next": "20 min"},
            {"name": "Tower of London", "desc": "Historic castle and prison", "visit_time": "2 hrs", "cost": "£33", "travel_time_to_next": "20 min"}
        ],
        "nature": [
            {"name": "Hyde Park", "desc": "Large city park", "visit_time": "2 hrs", "cost": "Free", "travel_time_to_next": "15 min"},
            {"name": "Kew Gardens", "desc": "Botanical garden with glasshouses", "visit_time": "2 hrs", "cost": "£15", "travel_time_to_next": "30 min"}
        ],
        "food": [
            {"name": "Borough Market", "desc": "Famous food market", "visit_time": "1.5 hrs", "cost": "£20", "travel_time_to_next": "10 min"},
            {"name": "Dishoom", "desc": "Popular Indian restaurant", "visit_time": "1.5 hrs", "cost": "£35", "travel_time_to_next": "15 min"}
        ],
        "shopping": [
            {"name": "Oxford Street", "desc": "Major retail street", "visit_time": "2 hrs", "cost": "Varies", "travel_time_to_next": "15 min"}
        ]
    },

    "Dubai": {
        "shopping": [
            {"name": "Dubai Mall", "desc": "One of the world’s largest malls", "visit_time": "2 hrs", "cost": "Free", "travel_time_to_next": "15 min"},
            {"name": "Souk Madinat Jumeirah", "desc": "Traditional market", "visit_time": "1.5 hrs", "cost": "Varies", "travel_time_to_next": "15 min"},
            {"name": "Gold Souk", "desc": "Famous market for gold jewelry", "visit_time": "1 hr", "cost": "Varies", "travel_time_to_next": "20 min"}
        ],
        "adventure": [
            {"name": "Desert Safari", "desc": "Dune bashing and camel ride", "visit_time": "4 hrs", "cost": "AED 300", "travel_time_to_next": "30 min"},
            {"name": "Skydiving over Palm Jumeirah", "desc": "Aerial adventure experience", "visit_time": "2 hrs", "cost": "AED 2000", "travel_time_to_next": "20 min"}
        ],
        "food": [
            {"name": "Al Fanar Restaurant", "desc": "Authentic Emirati cuisine", "visit_time": "1.5 hrs", "cost": "AED 100", "travel_time_to_next": "10 min"},
            {"name": "Pierchic", "desc": "Fine dining over the sea", "visit_time": "2 hrs", "cost": "AED 600", "travel_time_to_next": "15 min"}
        ],
        "nature": [
            {"name": "Dubai Miracle Garden", "desc": "Massive floral garden", "visit_time": "2 hrs", "cost": "AED 75", "travel_time_to_next": "20 min"}
        ]
    },

    "Rome": {
        "historic": [
            {"name": "Colosseum", "desc": "Ancient Roman amphitheater", "visit_time": "2 hrs", "cost": "€18", "travel_time_to_next": "10 min"},
            {"name": "Roman Forum", "desc": "Historic ruins of ancient Rome", "visit_time": "1.5 hrs", "cost": "€12", "travel_time_to_next": "10 min"},
            {"name": "Pantheon", "desc": "Ancient temple with dome", "visit_time": "45 min", "cost": "Free", "travel_time_to_next": "10 min"},
            {"name": "Vatican Museums", "desc": "Art and history museum", "visit_time": "3 hrs", "cost": "€17", "travel_time_to_next": "20 min"}
        ],
        "food": [
            {"name": "Trattoria da Enzo", "desc": "Classic Roman cuisine", "visit_time": "1 hr", "cost": "€25", "travel_time_to_next": "10 min"},
            {"name": "Gelateria del Teatro", "desc": "Famous gelato spot", "visit_time": "30 min", "cost": "€6", "travel_time_to_next": "10 min"}
        ],
        "nature": [
            {"name": "Villa Borghese Gardens", "desc": "Lush park in central Rome", "visit_time": "1.5 hrs", "cost": "Free", "travel_time_to_next": "15 min"}
        ]
    },

    "Default": {
        "general": [
            {"name": "City Museum", "desc": "Explore local history", "visit_time": "2 hrs", "cost": "$10", "travel_time_to_next": "15 min"},
            {"name": "Central Park", "desc": "Relaxing urban park", "visit_time": "2 hrs", "cost": "Free", "travel_time_to_next": "15 min"},
            {"name": "Old Town Square", "desc": "Cultural and shopping area", "visit_time": "1.5 hrs", "cost": "Free", "travel_time_to_next": "10 min"},
            {"name": "Local Market", "desc": "Buy souvenirs and snacks", "visit_time": "1 hr", "cost": "Varies", "travel_time_to_next": "10 min"}
        ]
    }
}
