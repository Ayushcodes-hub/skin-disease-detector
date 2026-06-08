# skin-disease-detector

https://huggingface.co/spaces/AyushAryaman/skin-disease-detector --> Link to the website on hugging face
# 🔬 AI Dermatology Platform (Advanced Prototype)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C.svg)](https://pytorch.org/)
[![Gradio](https://img.shields.io/badge/Gradio-UI%20Framework-FF6B6B.svg)](https://gradio.app/)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hosted-Hugging%20Face%20Spaces-yellow.svg)]([PASTE_YOUR_LIVE_HUGGING_FACE_URL_HERE])

An enterprise-grade, direct-to-consumer deep learning web application designed to bring advanced visual computer vision diagnostics straight to the browser. 

### 🌐 [Live Production Interface Workspace]([https://huggingface.co/spaces/AyushAryaman/skin-disease-detector])

---

## ⚡ Key Architectural Features

* **Deep Learning Core:** Leverages a pre-trained **ResNet50** convolutional neural network engine via PyTorch, fine-tuned on clinical imagery.
* **Imbalanced Class Weighting:** Optimized loss metrics featuring custom mathematical weights to handle ultra-rare pathologies alongside common anomalies.
* **TrumpRx-Inspired UI:** A premium, custom-styled CSS framework delivering a clean dark interface, metric tracking blocks, and direct camera-to-inference integrations.
* **Dynamic Learning Rate Scheduler:** Uses an automated `ReduceLROnPlateau` training loop to fine-tune network weights on complex, hard-to-classify skin textures.

---

## 📊 Dataset & Medical Categories

The network was trained on **10,015+ dermatoscopic images** sourced from the HAM10000 medical archive. The system evaluates classifications across 7 critical disease groups:

| Medical Shortcode | Clinical Designation |
| :--- | :--- |
| **nv** | Melanocytic nevi (Common Mole) |
| **mel** | Melanoma (High-Severity Skin Cancer) |
| **bkl** | Benign keratosis-like lesions |
| **bcc** | Basal cell carcinoma |
| **akiec** | Actinic keratoses |
| **vasc** | Vascular lesions |
| **df** | Dermatofibroma |

---

## 🛠️ The Tech Pipeline Ecosystem
