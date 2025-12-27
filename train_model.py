import pandas as pd
from sklearn.tree import DecisionTreeClassifier # <--- CHANGED THIS
import pickle

print("1. Loading the data... ⏳")
data = pd.read_csv('fraud_data.csv')

# Map Account Types
data['account_type'] = data['account_type'].map({
    'Student': 0,
    'Corporate': 1
})

# Map Locations
data['location'] = data['location'].map({
    'Lagos': 0, 'Abuja': 1, 'Kano': 2, 'Ibadan': 3, 
    'Russia': 4, 'China': 5, 'USA': 6,
    'Forest': 7, 'Remote': 8
})

X = data[['amount', 'location', 'account_type', 'time']]
y = data['is_fraud']

print("2. Training the Decision Tree... 🌳")
# We switched from LogisticRegression to DecisionTreeClassifier
model = DecisionTreeClassifier() 
model.fit(X, y)

with open('fraud_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("3. Success! 🎓 The Decision Tree model has been saved.")