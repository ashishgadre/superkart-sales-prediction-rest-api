import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = "http://backend:7860"

# Set the title of the Streamlit app
st.title("SuperKart Sales Prediction Platform")

# Section for online prediction
st.subheader("Online Prediction")

# Collect user input for property features

Product_Weight = st.number_input(
    "Product Weight",
    min_value=0.0,
    value=12.66,
    help="Weight of the product (numerical value)",
)

Product_Sugar_Content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

Product_Allocated_Area = st.number_input(
    "Product Allocated Area",
    min_value=0.0,
    value=0.068,
    help="Ratio of the allocated display area of each product to the total display area of all the products in a store",
)

Product_MRP = st.number_input(
    "Product MRP",
    min_value=0.0,
    value=116.7,
    help="Maximum retail price of each product (numerical value)",
)

Store_Size = st.selectbox(
    "Store Size",
    [ "Small", "Medium", "High"],
)
Store_Location_City_Type = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

Store_Type = st.selectbox(
    "Store Type",
    ["Supermarket Type1", "Supermarket Type2", "Departmental Store", "Food Mart"]
)

Store_Age_Years = st.number_input(
    "Store Age (Years)",
    min_value=0,
    value=17,
    help="Age of the store")

Product_Type_Category = st.selectbox(
    "Product Type Category",
    ["Perishables", "Non Perishables"]
)

Product_Id_char = st.selectbox(
    "Product Id Char",
    ["FD", "NC", "DR"]
)


# Convert user input into a DataFrame
input_data = pd.DataFrame([{
      "Product_Weight": Product_Weight,
      "Product_Sugar_Content": Product_Sugar_Content,
      "Product_Allocated_Area": Product_Allocated_Area,
      "Product_MRP": Product_MRP,
      "Store_Size": Store_Size,
      "Store_Location_City_Type": Store_Location_City_Type,
      "Store_Type": Store_Type,
      "Store_Age_Years": Store_Age_Years,
      "Product_Type_Category": Product_Type_Category,
      "Product_Id_char": Product_Id_char
}])

# Make prediction when the "Predict" button is clicked
if st.button("Run Prediction", type="primary"):
    response = requests.post(f"{BACKEND_URL}/v1/predictsales", json=input_data.to_dict(orient='records')[0])  # Send data to Flask API
    if response.status_code == 200:
        prediction = response.json()['Predicted Sales (in dollars)']
        st.success(f"Predicted Sales Price (in dollars): {prediction}")
    else:
        st.error("Unable to connect to the prediction API.")
