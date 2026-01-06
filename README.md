Project Title-Used Car Price Prediction (USA)

A machine learning web application that predicts the price of used cars in the USA based on features like manufacturing year, mileage, city, state, company (make), and model.  
The app uses Random Forest Regression, along with Target Encoding and Frequency Encoding for categorical feature handling.

Features

- Predict used car price using ML regression
- Dependent dropdown: only models of selected company are shown
- Efficient deployment without loading full dataset
- Encodings handled using pre-saved mapping dictionaries
- Built with interactive UI using Streamlit
- Supports large-scale real-world USA used car dataset

How it works:

Dataset split into `X` (features) and `y` (Price)
Categorical columns encoded using:
   - Target Encoding: `Make`, `Model`, `State`
   - Frequency Encoding: `City`
Company → Models mapping stored using:
company_models_map = train_df.groupby("Company")["Model"].unique().apply(list).to_dict()
Used RandomForestRegressor algorithm to train the model

Tech Stack

Python
scikit-learn (Random Forest Regressor)
Pandas, NumPy
Streamlit
Pickle (Model & encoders storage)
USA Used Cars Dataset (852,092 rows)

To run this in streamlit and enter this in terminal:
streamlit run app.py

