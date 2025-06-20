from flask import Flask, request, render_template
import pandas as pd
import json

app = Flask(__name__)

# Lade deine Autodaten
df = pd.read_csv("CarData40.csv")
df['Make_Model'] = df['Make'] + '_' + df['Model']

# Lade Fragen aus JSON
with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html", questions=questions)

@app.route('/predict', methods=['POST'])
def predict():
    answers = {}

    # Antworten sammeln
    for q in questions:
        feature = q["feature"]
        val = request.form.get(feature)
        
        if q["type"] == "range_choice":
            for choice in q["choices"]:
                if choice["label"] == val:
                    answers[feature] = tuple(choice["range"])
                    break
            else:
                answers[feature] = (None, None)
        else:
            if feature == "Seats":
                answers[feature] = int(val)
            else:
                answers[feature] = val

    def score_row(row):
        score = 0
        total = 0

        # Numerische Ranges
        for feature in ["Horsepower", "TopSpeed", "Acceleration", "Weight"]:
            val_range = answers.get(feature, (None, None))
            if None not in val_range:
                low, high = val_range
                total += 1
                if low <= row[feature] <= high:
                    score += 1
        
        # Kategoriale Features
        for feature in ["FuelType", "DriveType", "PriceCategory", "Seats"]:
            val = answers.get(feature)
            if val is not None and val != "":
                total += 1
                if row[feature] == val:
                    score += 1
        
        return score / total if total > 0 else 0

    # Score für alle Autos berechnen
    df['score'] = df.apply(score_row, axis=1)

    # Top 3 Autos nach Score, absteigend sortiert
    top_cars = df.sort_values(by='score', ascending=False).head(3)

    # Falls keine passenden Modelle gefunden wurden
    if top_cars['score'].max() == 0:
        results = ["Keine passenden Modelle gefunden."]
    else:
        results = [f"{row['Make']} {row['Model']} (Score: {row['score']:.2f})" for idx, row in top_cars.iterrows()]

    return render_template('result.html', results=results)


if __name__ == "__main__":
    app.run(debug=True)
