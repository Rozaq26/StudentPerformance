import streamlit as st
import joblib
import numpy as np

# Load the trained model
# Ensure the model and scaler files are in the 'model' directory
# or update the path accordingly.
try:
    model = joblib.load('model/model.joblib')
    scaler = joblib.load('model/scaler.pkl')
except FileNotFoundError:
    st.error("Model or scaler file not found. Please make sure 'model/model.joblib' and 'model/scaler.pkl' exist.")
    st.stop() # Stop execution if files are not found

st.sidebar.title("Student Dropout Model Prediction")
st.sidebar.write("""
     **Nama:** Rozaq Leksono \n

    **Email:** rozaql47@gmail.com

""")

# Function to make predictions
def predict_status(inputs):
    # Convert inputs to numpy array and reshape
    input_array = np.array(inputs).reshape(1, -1)
    # Apply the scaler
    input_array_scaled = scaler.transform(input_array)
    # Make prediction
    prediction = model.predict(input_array_scaled)
    return prediction

# Streamlit UI
st.title('Student Dropout Prediction')

# --- Input fields arranged in columns ---
st.subheader("Academic Information (1st Semester)")
col1, col2 = st.columns(2)
with col1:
    curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Sem Enrolled', min_value=0, max_value=30, value=20, key='c1_enrolled')
    curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Sem Approved', min_value=0, max_value=30, value=15, key='c1_approved')
with col2:
    curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Sem Grade', min_value=0.0, max_value=20.0, value=15.0, step=0.1, key='c1_grade')
    admission_grade = st.slider('Admission Grade', min_value=0.0, max_value=200.0, value=120.0, step=0.1, key='admission')


st.subheader("Academic Information (2nd Semester)")
col3, col4 = st.columns(2)
with col3:
    curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Sem Enrolled', min_value=0, max_value=30, value=20, key='c2_enrolled')
    curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Sem Approved', min_value=0, max_value=30, value=15, key='c2_approved')
with col4:
    curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Sem Grade', min_value=0.0, max_value=20.0, value=15.0, step=0.1, key='c2_grade')


st.subheader("Financial and Other Information")
col5, col6, col7 = st.columns(3) # Using three columns for these select boxes
with col5:
    tuition_fees_up_to_date = st.selectbox('Tuition Fees Up to Date', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No', key='tuition')
with col6:
    scholarship_holder = st.selectbox('Scholarship Holder', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No', key='scholarship')
with col7:
    displaced = st.selectbox('Displaced', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No', key='displaced')


# Map the inputs to the format expected by the model
# IMPORTANT: Ensure the order of features here EXACTLY matches the order
# your model was trained on.
# Based on the original code, the order was:
# 1. curricular_units_2nd_sem_approved
# 2. curricular_units_2nd_sem_grade
# 3. curricular_units_1st_sem_approved
# 4. curricular_units_1st_sem_grade
# 5. tuition_fees_up_to_date
# 6. scholarship_holder
# 7. curricular_units_2nd_sem_enrolled
# 8. curricular_units_1st_sem_enrolled
# 9. admission_grade
# 10. displaced
# I will maintain this order.

input_data = [
    curricular_units_2nd_sem_approved,
    curricular_units_2nd_sem_grade,
    curricular_units_1st_sem_approved,
    curricular_units_1st_sem_grade,
    tuition_fees_up_to_date,
    scholarship_holder,
    curricular_units_2nd_sem_enrolled,
    curricular_units_1st_sem_enrolled,
    admission_grade,
    displaced
]

# Button for prediction
if st.button('Predict Status'):
    prediction_result = predict_status(input_data)

    # The prediction_result might be probabilities or a single class index
    # If it's probabilities (e.g., from predict_proba), we need argmax.
    # If it's already a class index, argmax might not be needed or might need adjustment.
    # Assuming model.predict() for classifiers like SVC, LogisticRegression, RandomForestClassifier (when not using predict_proba)
    # often returns the class index directly.
    # If your model.predict() returns a 1D array with the class index:
    # predicted_status_index = prediction_result[0]

    # If your model.predict() returns a 2D array (e.g. for some Keras models or if using predict_proba inadvertently)
    # then the original np.argmax(prediction_result, axis=1)[0] is correct.
    # Let's assume model.predict() returns the class index directly for now,
    # as is common for many scikit-learn classifiers.
    # If you get an error or unexpected behavior, this is a key area to check.

    status_dict = {
        0: 'Dropout',
        1: 'Enrolled',
        2: 'Graduate'
    }

    # Check the shape of prediction_result to handle it correctly
    if isinstance(prediction_result, np.ndarray) and prediction_result.ndim > 1:
        # If it's a 2D array (like from predict_proba)
        predicted_status_index = np.argmax(prediction_result, axis=1)[0]
    elif isinstance(prediction_result, np.ndarray) and prediction_result.ndim == 1:
        # If it's a 1D array with the class index
        predicted_status_index = prediction_result[0]
    else:
        # Fallback or error handling if the format is unexpected
        st.error("Unexpected prediction format. Please check the model output.")
        st.stop()


    if predicted_status_index in status_dict:
        predicted_status = status_dict[predicted_status_index]
        
        # Displaying the prediction with enhanced styling
        if predicted_status == 'Dropout':
            st.error(f"Predicted Status: **{predicted_status}**")
        elif predicted_status == 'Graduate':
            st.success(f"Predicted Status: **{predicted_status}**")
        else: # Enrolled
            st.info(f"Predicted Status: **{predicted_status}**")
    else:
        st.warning(f"Predicted status index ({predicted_status_index}) not in status dictionary. Raw prediction: {prediction_result}")

