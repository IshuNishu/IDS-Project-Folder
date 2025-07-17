import streamlit as st
import pandas as pd
import joblib
import numpy as np

# The Initial Command Used in Streamlit 
st.set_page_config(page_title="IDS Dashboard", layout="wide")

# --- Load  the model and preprocessing  the tools ---
@st.cache_resource
def load_model_and_tools():
    model = joblib.load("model.pkl")
    label_encoders = joblib.load("label_encoders.pkl")
    feature_names = joblib.load("feature_names.pkl")
    return model, label_encoders, feature_names

model, label_encoders, expected_features = load_model_and_tools()

# The interactive front end of a Streamlit app
st.title(" Intrusion Detection System (IDS) Dashboard")
st.markdown("Upload a test CSV file (e.g., `KDDTest+.txt`) with the same format as training data.")

uploaded_file = st.file_uploader(" Upload a  file for IDS analysis", type=["csv", "txt"])

if uploaded_file is not None:
    try:
        # Load the  test data
        test_df = pd.read_csv(uploaded_file, header=None)

        # Load the field names
        field_names = pd.read_csv('Field Names.csv', header=None)[0].tolist()
        field_names.append('label')
        field_names.append('difficulty')
        test_df.columns = field_names

        # Drop 'difficulty' and 'label' columns (if you only want to predict them )
        test_df.drop(['difficulty', 'label'], axis=1, inplace=True, errors='ignore')

        # Encode categorical columns
        for col in label_encoders:
            if col in test_df.columns:
                le = label_encoders[col]
                test_df[col] = test_df[col].map(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

        # Ensure the feature alignment
        if list(test_df.columns) != expected_features:
            st.error(" Error: Uploaded file’s features don't match training features.")
            st.write("Expected features:", expected_features)
            st.write("Uploaded features:", test_df.columns.tolist())
        else:
            # Uses the trained model to generate predicted labels or values for the data test_df
            predictions = model.predict(test_df)

            # Show the results
            st.success(" Predictions completed!!")
            test_df['Prediction'] = predictions
            st.dataframe(test_df.head())

            # Give the summary too
            st.subheader(" Prediction Summary")
            st.bar_chart(test_df['Prediction'].value_counts())

    except Exception as e:
        st.error(f" An error occurred: {e}")
