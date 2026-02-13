# 📄 ATS Resume Analyzer

An **AI-powered ATS Resume Analyzer** built using **Python, NLP, and Machine Learning**.  
This project compares a Resume with a Job Description and provides an **ATS Score**, matched keywords, missing keywords, and improvement suggestions.

This helps job seekers optimize their resumes for better shortlisting chances.

---

## 🚀 Features
✅ Upload Resume in PDF format  
✅ Paste Job Description  
✅ Calculates ATS Score (0–100)  
✅ TF-IDF + Cosine Similarity Matching  
✅ Extracts Resume Keywords & JD Keywords  
✅ Shows Matched and Missing Keywords  
✅ Suggests missing skills/keywords  
✅ Streamlit-based UI (easy to use)

---

## 🛠 Tech Stack
- **Python**
- **Streamlit**
- **PyMuPDF** (PDF text extraction)
- **Scikit-learn**
- **TF-IDF Vectorizer**
- **Cosine Similarity**

---

## 📂 Project Structure
```txt
ATS-Resume-Analyzer/
│── app.py
│── resume_parser.py
│── ats_scoring.py
│── keyword_matcher.py
│── requirements.txt
│── README.md
│── screenshots/
⚙️ How It Works
Extracts resume text from PDF

Converts resume and job description into TF-IDF vectors

Computes similarity score using cosine similarity

Converts similarity score into ATS Score

Extracts keywords from both resume and job description

Shows missing and matched keywords

▶️ How to Run Locally
1. Clone Repository
git clone https://github.com/iamshrihari/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer
2. Install Dependencies
pip install -r requirements.txt
3. Run Streamlit App
streamlit run app.py
🎯 Future Improvements
Skill extraction using predefined skill database

PDF report generation

Resume section detection (Education, Skills, Experience)

Deployment on Streamlit Cloud

BERT-based semantic matching for better scoring

👨‍💻 Author
Shrihari Padatare
GitHub: https://github.com/iamshrihari