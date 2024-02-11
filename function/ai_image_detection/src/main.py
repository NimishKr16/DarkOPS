# main.py

import argparse
import torch
from PIL import Image
from model import get_model 
from custom_dataset import get_transform 
import glob
import os
import requests
from io import BytesIO



weights_folder = r"/Users/nimish/Desktop/dpbh/genaicpics/ai-image-detector/models"
def predict_single_image(image, model, device, transform):
    # Load and transform the image
    transformed_image = transform(image).unsqueeze(0).to(device)

    # Make a prediction
    model.eval()
    with torch.no_grad():
        outputs = model(transformed_image)
        _, predicted = outputs.logits.max(1)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=1)

    # Map numeric labels to string labels
    label_map = {0: "real", 1: "fake"}
    predicted_label = label_map[predicted.item()]

    return predicted_label, probabilities

def load_latest_model(model, device, weights_folder):
    # Use the specified folder or the default path to find the latest model
    list_of_files = glob.glob(os.path.join(weights_folder, 'model_epoch_*.pth'))
    if not list_of_files:
        raise FileNotFoundError(f"No model files found in {weights_folder}.")
    latest_file = max(list_of_files, key=os.path.getctime)
    checkpoint = torch.load(latest_file, map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    return model


# ------------- USE THIS TO CHECK IMAGE VIA IMAGE PATH ------------------ #

# def checkViaPath(image_path, weights_folder):
#     device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#     model = get_model(device)
#     model = load_latest_model(model, device, weights_folder)

#     transform = get_transform()
#     predicted_label, probabilities = predict_single_image(image_path, model, device, transform)
    
#     print(f'Predicted label: {predicted_label}')
#     print(f'Class probabilities: {probabilities}')

# ------------------------------------ CHECK USING IMG URL ----------------------------------------------- #

def checkimg(image_url, weights_folder = weights_folder):
    # Download the image from the URL
    response = requests.get(image_url)
    if response.status_code != 200:
        print(f"Failed to download image from {image_url}. Status code: {response.status_code}")
        return

    image = Image.open(BytesIO(response.content))

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = get_model(device)
    model = load_latest_model(model, device, weights_folder)

    transform = get_transform()
    predicted_label, probabilities = predict_single_image(image, model, device, transform)
    
    print(f'Predicted label: {predicted_label}')
    print(f'Class probabilities: {probabilities}')
    return predicted_label

# image_url =  "https://m.media-amazon.com/images/I/811meQOcCEL._SX695_.jpg"  
# weights_folder = r"/Users/nimish/Desktop/dpbh/genaicpics/ai-image-detector/models"
# main(image_url=image_url)


