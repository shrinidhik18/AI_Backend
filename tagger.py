from PIL import Image
from model_loader import ModelLoader

loader = ModelLoader()

def get_tags(image_path):
    image = Image.open(image_path).convert("RGB")
    preds = loader.predict(image)

    tags = []
    for (_, label, score) in preds:
        tags.append({
            "label": label,
            "confidence": float(score)
        })

    return tags
