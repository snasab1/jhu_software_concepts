from flask import Flask, render_template
from query_data import * # Import SQL query functions

app = Flask(__name__)

@app.route("/")
def index():
    questions_and_answers = [
        {"question": "How many total applicants were there for Fall 2024?", "answer": total_applicants_fall_2024()},
        {"question": "What percentage of applicants are international students?", "answer": percent_international()},
        {"question": "What are the average GPA and GRE scores of applicants who submitted them?", "answer": average_gpa_and_gre()},
        {"question": "What is the average GPA of American applicants for Fall 2024?", "answer": average_gpa_american_fall_2024()},
        {"question": "What percentage of Fall 2024 entries are Acceptances?", "answer": acceptance_percentage_fall_2024()},
        {"question": "What is the average GPA of Accepted applicants for Fall 2024?", "answer": average_gpa_accepted_fall_2024()},
        {"question": "How many JHU applicants were there for a Master's in Computer Science?", "answer": jhu_applicants_masters_cs()},
    ]
    return render_template("index.html", questions_and_answers=questions_and_answers)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)