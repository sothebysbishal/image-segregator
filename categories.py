CATEGORIES = [
    # --- Indoor ---
    "bedroom", "master bedroom", "guest bedroom", "bathroom", "powder room", "kitchen", "pantry",
    "living room", "dining room", "office", "study room", "meeting room", "home theater",
    "library", "walk-in closet", "wardrobe", "dressing room", "laundry room", "garage", "storage room",
    "staircase", "hallway", "corridor", "foyer", "lobby", "basement", "attic", "utility room",

    # --- Outdoor ---
    "balcony", "terrace", "patio", "deck", "rooftop", "courtyard", "garden", "backyard", "front yard",
    "driveway", "parking lot", "carport", "porch", "outdoor lounge", "barbecue area", "fire pit",

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
    "Indoor": [
        "bedroom", "bathroom", "kitchen", "living room", "dining room", "office", "garage", "storage room", "lobby",
    ],
    "Outdoor": [
        "balcony", "terrace", "outdoor space",
    ],
    "Amenities": [
        "clubhouse", "reception", "game room", "arcade", "cinema room", "theater room", "music room", "patio",
        "wine cellar", "bar", "private lounge", "cigar room", "karaoke room", "conference hall",
        "banquet hall", "gallery", "art studio",  "meeting room", "home theater",  "library", "walk-in closet", "wardrobe", "dressing room", "laundry room", 
        "swimming pool", "infinity pool", "jacuzzi", "spa", "sauna", "steam room", "outdoor shower",
        "indoor pool", "cold plunge", "barbecue area", "fire pit", "gym", "fitness center", "basketball court", "football field", "tennis court", "squash court",
        "golf simulator", "bowling alley", "yoga room", "boxing ring", "sky lounge", "rooftop bar", "helipad", "private elevator", "atrium", "balcony with view",
        "observation deck", "sunroom", "conservatory",  "kids play area", "nursery", "toy room", "study area",  "servant room", "maid’s quarters", "security room", 
        "attic", "maintenance room", "storage"
    ],
    "Other": ["others"]
}
