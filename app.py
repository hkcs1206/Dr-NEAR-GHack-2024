import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from datetime import datetime
import streamlit.components.v1 as components

# Load the doctor dataset from CSV
doctors_df = pd.read_csv('updated_doctors.csv')

# Load the symptoms and specialist dataset from CSV
symptoms_specialist_df = pd.read_csv('symptoms_specialist.csv')

# Application Frontend
st.title('Doctor Near')

# Collect user symptoms
selected_symptoms = st.multiselect('Select your symptoms:', symptoms_specialist_df['symptoms'].unique())

# Calendar input for selecting the appointment date
selected_date = st.date_input("Select preferred date for the appointment:", min_value=datetime.today())

# Derive the day of the week from the selected date
selected_day = selected_date.strftime("%A")

# Dropdown for selecting location with an option for any location
location_options = ['Any Location'] + list(doctors_df['Location'].unique())
selected_location = st.selectbox('Select your location:', location_options)

# Filter specialist based on selected symptoms
filtered_specialist = symptoms_specialist_df[symptoms_specialist_df['symptoms'].isin(selected_symptoms)]

if filtered_specialist['specialist'].nunique() < 2:
    st.write('Insufficient data to make a recommendation.')
else:
    # Train the classifier
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(filtered_specialist['symptoms'])
    y = filtered_specialist['specialist']
    classifier = LinearSVC(dual=False)
    classifier.fit(X, y)

    # Predict specialist for the selected symptoms
    X_user = vectorizer.transform(selected_symptoms)
    predicted_specialist = classifier.predict(X_user)

    # Filter doctors based on predicted specialist, selected day, and selected location
    filtered_doctors = doctors_df[doctors_df['Specialty'].isin(predicted_specialist)]
    filtered_doctors = filtered_doctors.sort_values('User Rating', ascending=False)

    if selected_location != 'Any Location':
        filtered_doctors = filtered_doctors[filtered_doctors['Location'] == selected_location]

    filtered_doctors = filtered_doctors[filtered_doctors['Available Days'].apply(lambda days: selected_day in [day.strip() for day in days.split(',')])]

    # Display recommended doctors
    if not filtered_doctors.empty:
        st.subheader('Recommended Doctors:')
        for index, row in filtered_doctors.iterrows():
            st.write(
                f"""
                <div style='background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); color: black; display: flex; justify-content: space-between; align-items: center;'>
                    <div>
                        <h3 style='color: #FF6868;'>{row['Name']} - Rating: {row['User Rating']} &#9733;</h3>
                        <p><strong>Specialty:</strong> {row['Specialty']}</p>
                        <p><strong>Location:</strong> {row['Location']}</p>
                        <p><strong>Experience:</strong> {row['Experience']}</p>
                        <p><strong>Available:</strong> {row['Available Days']} - {row['Available Times']}</p>

                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("---")
    else:
        st.write('No doctors found for the selected symptoms, day, or location.')

# Add CSS for styling
components.html('''
<style>
h1, h2, h3, h4, h5, h6 {
    color: #303f9f !important;
    font-family: 'Arial', sans-serif;
}

body {
    padding: 20px;
}

.card {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
}

.card-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
}

.card-content {
    font-size: 16px;
    margin-bottom: 10px;
}

hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 20px 0;
}

</style>
''')
