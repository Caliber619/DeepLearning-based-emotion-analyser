# 📌 DeepLearning-Based Emotion Analyser
_A deep learning model to analyze facial expressions and predict emotions using Convolutional Neural Networks (CNNs)._



---

## 📝 Project Overview
The **DeepLearning-Based Emotion Analyser** is a deep learning model that classifies human emotions based on facial expressions. The model is trained using **Convolutional Neural Networks (CNNs)** to detect emotions from grayscale images.

✅ **Key Features:**
- Uses **CNN architecture** for accurate emotion detection.
- **Classifies emotions** into different categories.
- **Trained on grayscale images** for better feature extraction.
- Can be integrated into real-time applications.

---


---

## ⚙️ How It Works?

### 1️⃣ Data Preparation
- Loads images from `images/train/` and `images/test/`.
- Converts images to **grayscale** and resizes them to **(48,48,1)**.
- Labels are one-hot encoded for classification.

### 2️⃣ CNN Model Architecture
- **Three Convolutional Layers** (`Conv2D`) for feature extraction.
- **MaxPooling Layers** (`MaxPooling2D`) to reduce dimensions.
- **Dropout Layers** to prevent overfitting.
- **Fully Connected Layers** (`Dense`) for classification.

### 3️⃣ Training the Model
- Uses **Adam optimizer** and `categorical_crossentropy` loss function.
- Trained for **30 epochs** with a batch size of **64**.

### 4️⃣ Saving & Running the Model
- The trained model is saved as `trained_model.h5`.
- To **test and predict emotions**, run `run.ipynb`.

---

## 🚀 How to Run the Project?

### run run.py
