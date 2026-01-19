Project Title-Used Car Price Prediction (USA)

A machine learning web application that predicts the price of used cars in the USA based on features like manufacturing year, mileage, city, state, company (make), and model.  
I downloaded the dataset from kaggle.
Link- https://www.kaggle.com/datasets/harikrishnareddyb/used-car-price-predictions

Uses CatBoost Regression for training the model and i don't use any encoder to encode the categorical features ,CatBoost regressor itself encodes it .

Features

- Predict used car price using ML regression
- Dependent dropdown: only models of selected company are shown
- Efficient deployment without loading full dataset
- Encodings handled using pre-saved mapping dictionaries
- Built with interactive UI using Streamlit
- Supports large-scale real-world USA used car dataset

How it works:

After the converting the csv dataset into dataframe, cleaned the dataset.
Dataset split into `X` (features) and `y` (Price)
Again x and y is splitted for training and testing .
Used CatBoostRegressor algorithm to train the model and the algorithm itself encode the categorical features.

Tech Stack:

Python
scikit-learn
Pandas, NumPy
Matplotlib
Streamlit
Pickle (contains model ,columns list, dataframe ,etc..)
USA Used Cars Dataset (852,092 rows)

To run this in streamlit and enter this in terminal:
streamlit run app.py

