from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from PIL import Image
import requests
from io import BytesIO
from contextlib import asynccontextmanager
from categories import CATEGORIES, CATEGORY_MAP, INDOOR_LABELS, OUTDOOR_LABELS

classifier = None

class ImageURL(BaseModel):
    url: str
    accessKey: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    global classifier
    print("🚀 Loading CLIP model...")
    classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
    print("✅ Model loaded successfully.")
    yield  # --- app runs here ---
    print("🛑 Shutting down, cleaning resources...")

app = FastAPI(title="Real Estate Image Classifier API", lifespan=lifespan)


def get_category(label: str):
    for category, items in CATEGORY_MAP.items():
        if label.lower() in items:
            return category
    return "Other"


def get_indoor_outdoor(label: str):
    label_lower = label.lower()
    if label_lower in INDOOR_LABELS:
        return "indoor"
    elif label_lower in OUTDOOR_LABELS:
        return "outdoor"
    else:
        return "unknown"


def classify_image(image: Image.Image):
    results = classifier(image, candidate_labels=CATEGORIES)
    top = results[0]
    label = top["label"]
    score = top["score"]

    if score < 0.20:
        return {
            "label": "unknown",
            "category": "Other",
            "indoor_outdoor": "unknown",
            "confidence": round(score * 100, 2)
        }

    # Handle ambiguous cases: if top prediction is indoor but next predictions are outdoor
    # and combined outdoor confidence is significant, prefer outdoor classification
    ambiguous_indoor_labels = {"conservatory", "sunroom", "atrium", "gallery"}
    label_lower = label.lower()
    
    if label_lower in ambiguous_indoor_labels and len(results) > 1:
        # Check top 5 predictions for outdoor indicators and find the best outdoor one
        outdoor_score = 0
        best_outdoor = None
        best_outdoor_score = 0
        
        for i in range(1, min(6, len(results))):
            result_label = results[i]["label"].lower()
            if result_label in OUTDOOR_LABELS:
                outdoor_score += results[i]["score"]
                if results[i]["score"] > best_outdoor_score:
                    best_outdoor = results[i]
                    best_outdoor_score = results[i]["score"]
        
        # If outdoor predictions have significant combined confidence, use the best outdoor prediction
        if outdoor_score > 0.15 and best_outdoor is not None:
            label = best_outdoor["label"]
            score = best_outdoor["score"]

    category = get_category(label)
    indoor_outdoor = get_indoor_outdoor(label)
    return {
        "label": label,
        "category": category,
        "indoor_outdoor": indoor_outdoor,
        "confidence": round(score * 100, 2)
    }


@app.post("/classify/url")
def classify_by_url(req: ImageURL):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        )
    }
    try:
        if req.accessKey != "9Lx7fV_q2Y6sBvD3G1hK8wZ0aR5mTnUcO4pSjHq":
            raise HTTPException(status_code=403, detail="You are not authorized to use this API")
        response = requests.get(req.url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=403, detail=str(e))
    image = Image.open(BytesIO(response.content)).convert("RGB")
    return classify_image(image)


@app.post("/classify/upload")
def classify_by_upload(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file).convert("RGB")
        return classify_image(image)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
