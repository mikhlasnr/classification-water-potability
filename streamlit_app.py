import streamlit as st
import pickle

# Load the saved model from disk
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Hey there! Welcome to our Potability Water Web App! Give it a try!')

# Create 9 input fields for user to enter numbers
input1 = st.number_input('ph:', format='%.7f')
input2 = st.number_input('Hardness', format='%.7f')
input3 = st.number_input('Solids', format='%.7f')
input4 = st.number_input('Chloramines', format='%.7f')
input5 = st.number_input('Sulfate:', format='%.7f')
input6 = st.number_input('Conductivity', format='%.7f')
input7 = st.number_input('Organic_carbon:', format='%.7f')
input8 = st.number_input('Trihalomethanes:', format='%.7f')
input9 = st.number_input('Turbidity:', format='%.7f')

# Create a button to make the prediction
if st.button('Predict'):
    # Use the loaded model to make a prediction
    prediction = model.predict(
        [[input1, input2, input3, input4, input5, input6, input7, input8, input9]])

    # Display the prediction result
    if(prediction[0] == 1):
        result_predict_message = """Air Dapat Diminum"""
        st.success(result_predict_message)
    else:
        result_predict_message = """Air Tidak Dapat Diminum"""
        st.error(result_predict_message)
