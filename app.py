import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np

with open('car_price.pkl','rb') as obj1:
        data=pkl.load(obj1)
target_maps = data["target_maps"]
city_freq = data["city_freq"]
feature_columns = data["feature_columns"]
model = data["model"]

def set_bg(image_url):
    bg_css = f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Call function with your image link
set_bg('https://wallpapercave.com/wp/wp5857069.jpg')

st.title("Used Car Price Prediction")

Company = st.selectbox("Select Company",sorted(target_maps["Company"].index.tolist()))

filtered_models = data["company_models_map"].get(Company, [])

Model = st.selectbox("Select Model",sorted(filtered_models))

State = st.selectbox("Select State",sorted(target_maps["State"].index.tolist()))

City = st.selectbox("Select City",sorted(city_freq.index.tolist()))

Year = st.number_input ("Year", min_value=1997, max_value=2018, step=1)
Km_driven = st.slider("Kilometers Driven",min_value=0,max_value=800000,step=1000)

button=st.button('Predict')
if button:
    Company_te = target_maps["Company"].get(
    Company, target_maps["Company"].mean())

    Model_te = target_maps["Model"].get(
    Model, target_maps["Model"].mean())

    State_te = target_maps["State"].get(
    State, target_maps["State"].mean())

    City_fe = city_freq.get(City, 0)
    Km_driven_log = np.log1p(Km_driven)
    input_data = {
    "Year": Year,
    "Km_driven_log": Km_driven_log,
    "Company_te": Company_te,
    "Model_te": Model_te,
    "State_te": State_te,
    "City_fe": City_fe
     }

    input_df = pd.DataFrame([input_data])
    input_df = input_df[feature_columns]

    result=model.predict(input_df)[0]
    st.success(f"The price of the car is ${round(result)}")
