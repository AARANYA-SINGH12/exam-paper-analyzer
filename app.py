from flask import Flask, render_template, request
import os
from analyzer.pdf_parser import extract_text_from_pdf      
from analyzer.question_extractor import extract_questions
from analyzer.topic_clusterer import cluster_topics
from analyzer.pattern_engine import analyze_patterns

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])   
def analyze():
    subject = request.form.get("subject")
    num_topics = int(request.form.get("num_topics", 8))
    files = request.files.getlist("papers")

    all_questions = []
    years = []

    for i, file in enumerate(files):
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)

        text = extract_text_from_pdf(filepath)
        questions = extract_questions(text, year = 2024 - i)

        all_questions.extend(questions)
        years.append(2024 - i)

        # deleting the file after processing 
        os.remove(filepath)

    clustered = cluster_topics(all_questions, num_topics=num_topics)
    results = analyze_patterns(clustered, years=years)

    return render_template("results.html", results=results, subject=subject)

if __name__ == "__main__":                 
    app.run(debug=True)