import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load  the field names
field_names = pd.read_csv('Field Names.csv', header=None)
columns = field_names[0].tolist()
columns.append('label')  # Add target column too
columns.append('difficulty')  # Last column in NSL-KDD dataset

# Load the training data
df = pd.read_csv('KDDTrain+.txt', names=columns)

# Drop 'difficulty' column (not used for training)
df.drop('difficulty', axis=1, inplace=True)

# Encode categorical columns
categorical_cols = ['protocol_type', 'service', 'flag']
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Define  the features and  the target
X = df.drop('label', axis=1)
y = df['label']

# Train  the model finally using(RFC)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model, feature names, and encoders for final usage 
joblib.dump(model, 'model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')
joblib.dump(X.columns.tolist(), 'feature_names.pkl')

print(" Model, encoders, and feature names saved successfully.")
