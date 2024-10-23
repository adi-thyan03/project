import pickle
import streamlit as st

# Load the trained machine learning model
with open('my_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title for the web app
st.title("Property Price Prediction App")

# Add inputs to the form
st.header("Enter Property Details")
total_area = st.number_input("Total Area (in sqft)", min_value=0.0, step=1.0)
price_per_sqft = st.number_input("Price per SQFT", min_value=0.0, step=1.0)
baths = st.number_input("Number of Baths", min_value=1, step=1)

# Add a button to submit the form
if st.button("Predict Price"):
    try:
        # Prepare input data for the model (assuming the same format used during training)
        input_data = [[total_area, price_per_sqft, baths]]
        
        # Use the model to make a prediction
        prediction = model.predict(input_data)[0]
        
        # Display the prediction
        st.success(f"The predicted property price is: {prediction}")
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")




