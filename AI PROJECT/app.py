import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('seattle_weather_best_model.pkl','rb'))

st.title("Seattle Rain Prediction App")

precip = st.number_input("Precipitation")
tmax = st.number_input("Max Temperature")
tmin = st.number_input("Min Temperature")
wind = st.number_input("Wind Speed")

if st.button("Predict"):
    result = model.predict([[precip, tmax, tmin, wind]])
    if result[0] == 1:
        st.success("🌧️ Rain Expected")
    else:
        st.success("☀️ No Rain")
