CATEGORIES = [
    # --- Indoor ---
    "bedroom", "master bedroom", "guest bedroom", "bathroom", "powder room", "kitchen", "pantry",
    "living room", "dining room", "office", "study room", "meeting room", "home theater",
    "library", "walk-in closet", "wardrobe", "dressing room", "laundry room", "garage", "storage room",
    "staircase", "hallway", "corridor", "foyer", "lobby", "basement", "attic", "utility room",

    # --- Outdoor ---
    "balcony", "terrace", "patio", "deck", "rooftop", "courtyard", "garden", "backyard", "front yard",
    "driveway", "parking lot", "carport", "porch", "outdoor lounge", "barbecue area", "fire pit",
    "building exterior", "facade", "entrance", "front entrance", "exterior", "building facade",

    # --- Water & Wellness ---
    "swimming pool", "infinity pool", "jacuzzi", "spa", "sauna", "steam room", "outdoor shower",
    "indoor pool", "cold plunge",

    # --- Sports & Fitness ---
    "gym", "fitness center", "basketball court", "football field", "tennis court", "squash court",
    "golf simulator", "bowling alley", "yoga room", "boxing ring",

    # --- Amenities & Entertainment ---
    "clubhouse", "reception", "game room", "arcade", "cinema room", "theater room", "music room",
    "wine cellar", "bar", "private lounge", "cigar room", "karaoke room", "conference hall",
    "banquet hall", "gallery", "art studio",

    # --- Luxury & Lifestyle ---
    "sky lounge", "rooftop bar", "helipad", "private elevator", "atrium", "balcony with view",
    "observation deck", "sunroom", "conservatory",

    # --- Kids & Family ---
    "kids play area", "nursery", "toy room", "study area",

    # --- Miscellaneous / Other ---
    "servant room", "maid’s quarters", "security room", "maintenance room", "storage", "other"
]

CATEGORY_MAP = {
    "Bedroom": [
        "bedroom", "master bedroom", "guest bedroom", "dressing room",
        "bed room", "master suite", "primary bedroom", "guest room", "bedroom with view"
    ],
    "Bathroom": [
        "bathroom", "powder room", "washroom", "restroom", "toilet", "lavatory", "wc", "bath",
    ],
    "Living Room": [
    "living room", "lounge", "family room", "sitting room", "great room", 
    "open plan living", "living area", "open space", "main hall"
    ],
    "Kitchen": [
        "kitchen", "pantry", "kitchenette", "cookhouse", "galley", 
        "open kitchen", "chef's kitchen", "island kitchen"
    ],
    "Dining Room": [
        "dining room", "dining area", "breakfast nook", "breakfast area",
    ],
    "Office": [
        "office", "study", "study room",
    ],
    "Garage": [
        "garage", "carport", "parking garage",
    ],
    "Storage": [
        "storage room", "storage",
    ],
    "Balcony": [
        "balcony", "terrace", "veranda", "verandah",
    ],
    "Patio": [
        "patio", "courtyard patio", "outdoor seating",
    ],
    "Rooftop": [
        "rooftop",
    ],
    "Exterior": [
        "building exterior", "facade", "entrance", "front entrance", "exterior", "building facade",
    ],
    "Amenities": [
        "clubhouse", "reception", "game room", "arcade", "cinema room", "theater room", "music room",
        "wine cellar", "bar", "private lounge", "cigar room", "karaoke room", "conference hall",
        "banquet hall", "gallery", "art studio",  "meeting room", "home theater",  "library", "walk-in closet", "wardrobe", "laundry room", 
        "swimming pool", "infinity pool", "jacuzzi", "spa", "sauna", "steam room", "outdoor shower",
        "indoor pool", "cold plunge", "barbecue area", "fire pit", "gym", "fitness center", "basketball court", "football field", "tennis court", "squash court",
        "golf simulator", "bowling alley", "yoga room", "boxing ring", "sky lounge", "rooftop bar", "helipad", "private elevator", "atrium", "balcony with view",
        "observation deck", "sunroom", "conservatory",  "kids play area", "nursery", "toy room", "study area",  "servant room", "maid's quarters", "security room", 
        "attic", "maintenance room",
        "staircase", "hallway", "corridor", "foyer", "lobby", "basement", "utility room",
        "deck", "courtyard", "garden", "backyard", "front yard", "driveway", "parking lot", "porch", "outdoor lounge"
    ],
    "Other": ["other"]
}

# Indoor/Outdoor classification mapping
INDOOR_LABELS = {
    # Indoor rooms
    "bedroom", "master bedroom", "guest bedroom", "bathroom", "powder room", "kitchen", "pantry",
    "living room", "dining room", "office", "study room", "meeting room", "home theater",
    "library", "walk-in closet", "wardrobe", "dressing room", "laundry room", "garage", "storage room",
    "staircase", "hallway", "corridor", "foyer", "lobby", "basement", "attic", "utility room",
    # Indoor amenities
    "clubhouse", "reception", "game room", "arcade", "cinema room", "theater room", "music room",
    "wine cellar", "bar", "private lounge", "cigar room", "karaoke room", "conference hall",
    "banquet hall", "gallery", "art studio", "gym", "fitness center", "golf simulator", "bowling alley",
    "yoga room", "boxing ring", "sky lounge", "private elevator", "atrium", "sunroom", "conservatory",
    "kids play area", "nursery", "toy room", "study area", "servant room", "maid's quarters",
    "security room", "maintenance room", "storage",
    # Indoor water/wellness
    "sauna", "steam room", "indoor pool", "cold plunge", "jacuzzi", "spa",
    # Additional mappings from CATEGORY_MAP
    "bed room", "master suite", "primary bedroom", "guest room", "bedroom with view",
    "washroom", "restroom", "toilet", "lavatory", "wc", "bath",
    "lounge", "family room", "sitting room", "great room", "open plan living", "living area", "open space", "main hall",
    "kitchenette", "cookhouse", "galley", "open kitchen", "chef's kitchen", "island kitchen",
    "dining area", "breakfast nook", "breakfast area",
    "study", "parking garage"
}

OUTDOOR_LABELS = {
    # Outdoor spaces
    "balcony", "terrace", "patio", "deck", "rooftop", "courtyard", "garden", "backyard", "front yard",
    "driveway", "parking lot", "carport", "porch", "outdoor lounge", "barbecue area", "fire pit",
    # Building exterior
    "building exterior", "facade", "entrance", "front entrance", "exterior", "building facade",
    # Outdoor water/wellness
    "swimming pool", "infinity pool", "outdoor shower",
    # Outdoor sports
    "basketball court", "football field", "tennis court", "squash court",
    # Outdoor luxury
    "rooftop bar", "helipad", "observation deck", "balcony with view",
    # Additional mappings
    "veranda", "verandah", "courtyard patio", "outdoor seating"
}
