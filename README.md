# Resume Screening AI

A web-based AI application that automatically analyzes resumes and matches them with job descriptions using Machine Learning and NLP techniques.

Live Demo: https://resume-screening-ai-3spo.onrender.com/


## Features
- Upload resume in PDF format
- Paste job description
- AI model calculates resume match percentage
- Graphical result (pie chart + score)
- Simple and clean UI
- Deployed live on Render

## Tech Stack
- Python
- Flask
- Machine Learning (Scikit-learn)
- NLP (TF-IDF Vectorizer)
- HTML, CSS, JavaScript
- Chart.js
- Render (Deployment)

## How It Works
1. User uploads resume (PDF)
2. Resume text is extracted using pdfplumber
3. Job description is converted to vector
4. AI model compares resume & JD
5. Match score is displayed in graph
