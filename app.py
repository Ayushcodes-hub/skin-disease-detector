import gradio as gr
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

# 1. Re-initialize the ResNet50 framework structure
model = models.resnet50()
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 7)

# 2. Load the trained weights we created in Colab
# (Assuming the file skin_disease_model.pth is in the same folder)
model.load_state_dict(torch.load('skin_disease_model.pth', map_location=torch.device('cpu')))
model.eval()

# 3. Label list mapping back to plain English
labels = [
    'Melanocytic nevi (Common Mole)',
    'Melanoma (Skin Cancer - Please Consult a Doctor)',
    'Benign keratosis-like lesions',
    'Basal cell carcinoma',
    'Actinic keratoses',
    'Vascular lesions',
    'Dermatofibroma'
]

# 4. Image transformations matching what we did in training
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 5. Define prediction functionality
def predict_skin_condition(img):
    if img is None:
        return "Please upload or snap an image."
    
    # Convert image and run through model
    img = Image.fromarray(img.astype('uint8'), 'RGB')
    img_t = preprocess(img).unsqueeze(0)
    
    with torch.no_grad():
        outputs = model(img_t)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
    
    # Return dictionary of labels and their score values
    return {labels[i]: float(probabilities[i]) for i in range(7)}

# 6. Build UI with Gradio
interface = gr.Interface(
    fn=predict_skin_condition,
    inputs=gr.Image(label="Take a photo of your skin or upload an image"),
    outputs=gr.Label(num_top_classes=3, label="Top 3 AI Predictions"),
    title="AI Dermatology Assistant Prototype",
    description="⚠️ DISCLAIMER: This app is an educational prototype built using machine learning. It is NOT a replacement for a professional medical diagnosis or clinical evaluation.",
    theme="soft"
)

if __name__ == "__main__":
    interface.launch()
