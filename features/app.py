from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = "supermegagheim"
with open('questions.json') as f:
    questions = json.load(f)

@app.route("/")
def index():
    session["answers"] = {}
    return redirect(url_for("question", qid=0))

@app.route("/question/<int:qid>", methods=["GET", "POST"])
def question(qid):
    if request.method == "POST":
        answer = request.form.get("answer")
        answers = session.get("answers", {})
        answers[str(qid)] = answer
        session["answers"] = answers
        next_qid = qid + 1
        if next_qid < len(questions):
            return redirect(url_for("question", qid=next_qid))
        else:
            return redirect(url_for("result"))

    question = questions[qid]
    return render_template("question.html", question=question, qid=qid)

@app.route('/result')
def result():
    answers = session.get("answers", {})
    return render_template("result.html", answers=answers)

if __name__ == "__main__":
    app.run(debug=True)