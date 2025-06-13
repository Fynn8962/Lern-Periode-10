from flask import Flask, request, render_template
import pandas as pd
import joblib
import json

app = Flask(__name__)

# Modelle und Objekte laden
clf = joblib.load('model.pkl')
label_encoders = joblib.load('label_encoders.pkl')
model_encoder = joblib.load('model_encoder.pkl')
df_columns = joblib.load('columns.pkl')
df = pd.read_csv("dataCar.csv")

with open("questions.json", "r", encoding='utf-8') as f:
    questions = json.load(f)["questions"]


def build_feature(answers):
    input_vector = pd.DataFrame(columns=df_columns)
    row = []
    for col in df_columns:
        val = answers.get(col, None)
        if col in label_encoders:
            val = label_encoders[col].transform([val])[0] if val is not None else 0
        elif val is None:
            val = 0
        row.append(val)
    input_vector.loc[0] = row
    return input_vector


@app.route('/', methods=['GET'])
def form():
    return render_template('form.html', questions=questions)


@app.route('/predict', methods=['POST'])
def predict():
    answers = {}
    for q in questions:
        feature = q["feature"]
        val = request.form.get(feature)
        if q["type"] == "range_choice":
            val = int(val)
        answers[feature] = val

    user_input = build_feature(answers)
    pred_label = clf.predict(user_input)[0]
    model_name = model_encoder.inverse_transform([pred_label])[0]
    make_name = df[df["Model"] == model_name]["Make"].mode()[0]

    return render_template('result.html', result=f"{make_name} {model_name}")


if __name__ == '__main__':
    app.run(debug=True)
