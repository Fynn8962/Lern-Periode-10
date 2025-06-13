import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("dataCar.csv")
y = df['Model']
X = df.drop(columns=['Make', 'Model'])

label_encoders = {}
for col in X.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    label_encoders[col] = le

model_encoder = LabelEncoder()
y = model_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

joblib.dump(clf, 'model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')
joblib.dump(model_encoder, 'model_encoder.pkl')
joblib.dump(X.columns.tolist(), 'columns.pkl')
