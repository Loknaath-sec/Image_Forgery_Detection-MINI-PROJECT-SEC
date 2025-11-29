# Image Forgery Detection using ELA + CNN

This project detects whether an image is **Authentic** or **Forged** using a combination of **Error Level Analysis (ELA)** 🔍 and a **Convolutional Neural Network (CNN)** 🤖.  
It highlights manipulation traces such as splicing, copy-move, and image tampering using ELA-based forensic analysis.

---

## 🚀 Project Overview

Upload an image and the system will automatically:
1. 🔧 Convert it to its ELA representation  
2. 🧠 Analyze it using a trained EfficientNetB0 CNN model  
3. 🟢 Predict: **Authentic** or 🔴 **Forged**  
4. 📊 Display confidence scores  
5. 🖥️ Show the ELA visualization  

This tool is deployed using **Gradio** and hosted on **Hugging Face Spaces**.

---

## 🔬 How It Works

### 1️⃣ Error Level Analysis (ELA)
ELA highlights areas with inconsistent JPEG compression.  
Tampered or digitally edited regions often show **brighter artifacts** due to recompression inconsistencies. ✨

### 2️⃣ CNN Classification (EfficientNetB0)
ELA images are fed into a deep learning model trained on:
- ⭐ Authentic images  
- ❌ Forged images  

The model outputs:
- **Authentic** ✔️  
- **Forged** ❌  
along with confidence scores.

---

## 📂 Dataset Used

### **CASIA 2.0 Image Tampering Detection Dataset**

https://www.kaggle.com/datasets/divg07/casia-20-image-tampering-detection-dataset

Includes real-world manipulated images involving:
- ✂️ Splicing  
- 🔁 Copy-Move  
- 🧽 Object removal  
- 🖼️ Image composition  

Dataset split:
- 🏋️ 80% Training  
- 🧪 20% Validation  

---

## 🛠️ Technologies Used

- 🐍 Python  
- 🧠 TensorFlow / Keras  
- ⚙️ EfficientNetB0  
- 🖼️ Pillow (PIL)  
- 📦 NumPy  
- 🌐 Gradio  
- ☁️ Hugging Face Spaces  

---

## 📁 Project Structure
```powershell
project/
│
├── app.py # Gradio web app
├── requirements.txt
├── preprocess_ela.py # ELA processing
├── model_def.py # CNN architecture
├── forgery_cnn_best.h5 # Trained model
└── data/ # Dataset (optional)
```

---

## ▶️ Running Locally

```bash
git clone https://github.com/Loknaath-sec/Image_Forgery_Detection-MINI-PROJECT-SEC.git
cd image-forgery-detection
pip install -r requirements.txt
python app.py
```

## Open in browser:
```arduino
http://localhost:7860
```
## 🌐 Live Demo (Hugging Face Space)
https://huggingface.co/spaces/Loknaath/Image_forgery_detection

---

## 👥 Team Members

- 👤 Loknaath P – Reg No: 212223240080
- 👤 Lokhnath J – Reg No: 212223240079  

---

## 🌍 Applications

- 🕵️ Digital Forensics  
- 📰 Journalism & Fact-Checking  
- ⚖️ Legal and Cybercrime Investigations  
- 🎓 Academic Integrity  
- 📱 Social Media Content Verification  

---

## 🎯 Objective

To build a simple, accurate, and accessible tool that identifies digitally manipulated images using forensic techniques and deep learning.

---

## Conclusion
This project successfully demonstrates how combining Error Level Analysis (ELA) with a Convolutional Neural Network (CNN) can effectively identify manipulated images. By exposing compression inconsistencies and analyzing them with a trained deep-learning model, the system provides accurate classification of Authentic vs Forged images. The final web application is simple, fast, and accessible, making image forgery detection easy for everyday users as well as useful for digital forensics, journalism, and academic environments.
