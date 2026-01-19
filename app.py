import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np

with open('car_price.pkl','rb') as obj1:
        data=pkl.load(obj1)
feature_columns = data["feature_columns"]
model = data["model"]
df=data['df']

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

Company = st.selectbox("Select Company",sorted(df["Company"].unique().tolist()))

filtered_models = data["company_models_map"].get(Company, [])

Model = st.selectbox("Select Model",sorted(filtered_models))

State = st.selectbox("Select State",sorted(df["State"].unique().tolist()))

filtered_city=data['state_city_map'].get(State,[])

City = st.selectbox("Select City",sorted(filtered_city))

Year = st.number_input ("Year", min_value=1997, max_value=2018, step=1)

Km_driven = st.slider("Kilometers Driven",min_value=0,max_value=100000,step=1000)

button=st.button('Predict')
if button:
   
    Km_driven_log = np.log1p(Km_driven)
    
    input_data = {
    "Year": Year,
    "Km_driven": Km_driven_log,
    "Company": Company,
    "Model": Model,
    "State": State,
    "City": City
     }

    input_df = pd.DataFrame([input_data])
    input_df = input_df[feature_columns]

    result=model.predict(input_df)[0]
    st.success(f"The price of the car is ${round(result)}")
