from flask import Flask, request, render_template
import joblib
import pdfplumber

app = Flask(__name__)

model = joblib.load("resume_model.pkl")
vector = joblib.load("vector.pkl")

HTML = """
<h2>Resume Screening AI</h2>
<form method="post" enctype="multipart/form-data">
Upload Resume (PDF): <input type="file" name="resume"><br><br>
Job Description:<br>
<textarea name="job" rows="6" cols="50"></textarea><br><br>
<input type="submit">
</form>

{% if result %}
<h3>Result: {{result}}</h3>
<h3>Match: {{match}}%</h3>
{% endif %}
"""

def extract_text(file):
    text=""
    with pdfplumber.open(file) as pdf:
        for p in pdf.pages:
            text += p.extract_text()
    return text

@app.route("/", methods=["GET","POST"])
def home():
    result=None
    match=None

    if request.method=="POST":
        resume = request.files["resume"]
        job = request.form["job"]

        text = extract_text(resume)
        X = vector.transform([text])
        pred = model.predict(X)[0]

        result = "Selected" if pred==1 else "Rejected"

        words1 = set(text.lower().split())
        words2 = set(job.lower().split())
        match = round(len(words1 & words2) / len(words2) * 100,2)

    return render_template("index.html", result=result, match=match)

app.run(debug=True)
