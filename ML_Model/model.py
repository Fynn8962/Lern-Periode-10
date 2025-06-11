import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# region Training
# Daten einlesen
df = pd.read_csv("dataCar.csv")

# Zielspalte: Model
y = df['Model']

# Features auswählen (alle außer Make und Model)
X = df.drop(columns=['Make', 'Model'])

# LabelEncoder für jede kategoriale Spalte vorbereiten
label_encoders = {}
for col in X.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    label_encoders[col] = le

# Zielspalte ebenfalls kodieren
model_encoder = LabelEncoder()
y = model_encoder.fit_transform(y)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelltraining
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluation (optional)
y_pred = clf.predict(X_test)
print("Modell-Evaluation:\n")
print(classification_report(y_test, y_pred))
# endregion

# region Interkation
import json

with open("questions.json", "r") as file:
    questions = json.load(file)

def ask_user(questions):
    answers = {}
    for q in questions:
        feature = q["feature"]
        print("\n" + q["question"])
        
        if q["type"] == "choice":
            for i, choice in enumerate(q["choices"]):
                print(f"{i+1}: {choice}")
            index = int(input("Deine Wahl (Nummer): ")) - 1
            answers[feature] = q["choices"][index]
        
        elif q["type"] == "range_choice":
            for i, choice in enumerate(q["choices"]):
                print(f"{i+1}: {choice['label']}")
            index = int(input("Deine Wahl (Nummer): ")) - 1
            choice = q["choices"][index]
            if feature == "Engine HP":
                answers[feature] = (choice["range"][0] + choice["range"][1]) // 2
            elif feature == "highway MPG":
                answers[feature] = choice["min_highway_mpg"]
    return answers


def build_feature(answers, df_columns, label_encoders):
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

# endregion


# region Vorhersage
user_answers = ask_user(questions["questions"])
user_input = build_feature(user_answers, X.columns, label_encoders)
predicted_label = clf.predict(user_input)[0]
predicted_model = model_encoder.inverse_transform([predicted_label])[0]

# Marke zum Modell heraussuchen
predicted_make = df[df["Model"] == predicted_model]["Make"].mode()[0]

print(f"\n Das empfohlene Auto ist: **{predicted_make} {predicted_model}**")

# endregion