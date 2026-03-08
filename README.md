# 🛡️ AI Phishing Website Detector

🌐 **Live Demo:** [Try the app here](https://ai-phishing-detector-xb6ggrfappfy6kt3chuuzxk.streamlit.app/)

An AI-powered machine learning tool that detects phishing websites with **96.92% accuracy** using Random Forest Classification.

---

## 📌 Overview

Phishing attacks are one of the most common cybersecurity threats today. This project uses machine learning to automatically classify websites as **legitimate or phishing** based on 30+ URL and website features — no manual analysis needed.

---

## 🎯 Key Results

| Metric | Score |
|--------|-------|
| ✅ Accuracy | **96.92%** |
| 🌲 Model | Random Forest Classifier |
| 📊 Dataset Size | 11,054 websites |
| 🔍 Features Analyzed | 30 website attributes |

---

## 🔍 How It Works

The model analyzes 30+ features of a website including:
- Whether the URL uses an IP address instead of a domain
- Presence of suspicious symbols like `@` in the URL
- URL length (phishing URLs tend to be unusually long)
- Use of URL shorteners
- Presence of HTTPS and SSL certificates
- Domain age and registration details
- And many more...

These features are fed into a **Random Forest Classifier** which learned patterns from thousands of real phishing and legitimate websites.

---

## 📊 Visualizations

### Confusion Matrix
![Confusion Matrix](results.png)

### Top Features Used by the AI
![Feature Importance](features.png)

---

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Scikit-learn** — Machine learning model
- **Pandas & NumPy** — Data processing
- **Matplotlib & Seaborn** — Visualizations
- **Streamlit** — Web app deployment
- **Google Colab** — Development environment

---

## 📁 Project Structure

```
ai-phishing-detector/
│
├── phishing_detector_model.ipynb  # Main notebook with full code
├── app.py                         # Streamlit web app
├── phishing_model.pkl             # Saved trained AI model
├── feature_names.pkl              # Feature names used by model
├── requirements.txt               # Python dependencies
├── results.png                    # Confusion matrix chart
└── features.png                   # Feature importance chart
```

---

## 🚀 How to Run Locally

1. Clone this repository
```bash
git clone https://github.com/shritamaacharyee/ai-phishing-detector.git
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run app.py
```

---

## 📚 Dataset

- **Source:** Kaggle — Phishing Website Detector Dataset
- **Size:** 11,054 samples
- **Features:** 30 website attributes
- **Labels:** Phishing or Legitimate

---

## 👩‍💻 Author

**Shritama Acharyee**  
Cybersecurity & AI Enthusiast  
📧 shritamaacharyee@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/shritama-acharyee-4033b6307)  
🐙 [GitHub](https://github.com/shritamaacharyee)

---

## ⭐ If you found this useful, please star the repository!
