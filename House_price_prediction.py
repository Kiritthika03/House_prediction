import numpy as np
import streamlit as st
import pickle

# Safely load the model
model_path = r'C:\Users\LENOVO\Documents\Project\academic project\Price prediction\rf_model.pkl'
with open(model_path, 'rb') as file:
    loaded_model = pickle.load(file)

# Prediction function
def house_price_prediction(input_data):
    input_data_as_numpy = np.array(input_data, dtype=float)  # Ensure all inputs are float
    input_data_reshaped = input_data_as_numpy.reshape(1, -1)  # Reshape for prediction
    prediction = loaded_model.predict(input_data_reshaped)
    return f"The predicted price of the house is: ${prediction[0]:,.2f}"

# Streamlit UI
def main():
    st.title('House Price Prediction App')

    # Input fields
    try:
        Area = float(st.text_input('Area (SqFt):'))
        Bedrooms = int(st.text_input('Number of Bedrooms:'))
        Bathroom = int(st.text_input('Number of Bathrooms:'))
        Floors = int(st.text_input('Number of Floors:'))
        YearBuilt = int(st.text_input('Year Built:'))
        Location = int(st.text_input('Location (Downtown: 0, Suburban: 2, Urban: 3, Rural: 1):'))
        Condition = int(st.text_input('Condition (Excellent: 0, Good: 2, Fair: 1, Poor: 3):'))
        Garage = int(st.text_input('Garage (Yes: 1, No: 0):'))
        PropertyAge = int(st.text_input('Property Age (Years):'))
        PricePerSqFt = float(st.text_input('Price Per SqFt:'))
    except ValueError:
        st.warning("Please ensure all inputs are valid numbers.")
        return

    # Prediction button
    if st.button('Predict Price'):
        Price = house_price_prediction([Area, Bedrooms, Bathroom, Floors, YearBuilt, Location, Condition, Garage, PropertyAge, PricePerSqFt])
        st.success(Price)

# Run the app
if __name__ == '__main__':
    main()
