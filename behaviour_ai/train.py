import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import time

df = pd.read_csv("data.csv")

map_ans = {'A': 0, 'B': 1, 'C': 2}
X = df[['Q1', 'Q2', 'Q3']].apply(lambda col: col.map(map_ans))

le = LabelEncoder()

y = le.fit_transform(df['Label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()

model.fit(X_train, y_train)

def predict_behavior(q1, q2, q3):
    data = pd.DataFrame([[q1, q2, q3]], columns=['Q1', 'Q2', 'Q3'])
    data = data.apply(lambda col: col.map(map_ans))
    pred = model.predict(data)[0]
    return le.inverse_transform([pred])[0]

print("Q1: How do you feel in crowds?")
print("A: Energized\nB: Neutral\nC: Drained")

a1=input('Q1 answer : ').upper()

print("Q2: Do you prefer working in groups or alone?")
print("A: Groups\nB: Depends\nC: Alone\n")

a2=input('Q2 answer : ').upper()

print("Q3: How do you make decisions?")
print("A: Logically\nB: Both logic and feeling\nC: Emotionally\n")

a3=input('Q3 answer : ').upper()

time.sleep(2)

print("Prediction:", predict_behavior(a1, a2, a3))
print(f"Accuracy: {model.score(X_test, y_test)*100:.2f}%")