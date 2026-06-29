import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="Walmart Supply Chain Panel", layout="wide")
st.title("📊 Walmart Predictive Supply Chain Engine")

# Explicit error check to show on the webpage if files are missing
missing_files = []
if not os.path.exists('walmart_model.pkl'): missing_files.append('walmart_model.pkl')
if not os.path.exists('model_columns.pkl'): missing_files.append('model_columns.pkl')

if missing_files:
    st.error(f"❌ Cannot load dashboard elements! The following files are missing from your Colab files panel: {missing_files}")
    st.info("💡 Fix: Please scroll up to your Machine Learning code cell block and run it again to generate these files.")
else:
    # Safely load assets since they are verified to exist
    model = joblib.load('walmart_model.pkl')
    model_columns = joblib.load('model_columns.pkl')
    
    st.success("✅ Model assets loaded perfectly!")
    
    # 🎛️ App layout columns
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔮 Input Store Configurations")
        store_id = st.number_input("Select Store Location ID", min_value=1, max_value=45, value=1)
        is_holiday = st.selectbox("Is this a holiday week?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        temperature = st.slider("Predicted Temperature (°F)", min_value=0.0, max_value=100.0, value=55.0)
        fuel_price = st.number_input("Regional Fuel Price ($/Gallon)", min_value=1.0, max_value=5.0, value=3.25)
        cpi = st.number_input("Consumer Price Index (CPI)", min_value=100.0, max_value=250.0, value=211.0)
        unemployment = st.slider("Unemployment Rate (%)", min_value=2.0, max_value=15.0, value=7.5)
        week_of_year = st.slider("Week of the Year", min_value=1, max_value=52, value=25)
        year_focus = st.selectbox("Target Year", options=[2024, 2025, 2026])
        
    with col2:
        st.subheader("🎯 Optimization Output")
        if st.button("Generate Replenishment Prediction Orders", type="primary"):
            input_data = pd.DataFrame(columns=model_columns)
            input_data.loc[0] = 0.0
            
            input_data['IsHoliday'] = int(is_holiday)
            input_data['Temperature'] = temperature
            input_data['Fuel_Price'] = fuel_price
            input_data['CPI'] = cpi
            input_data['Unemployment'] = unemployment
            input_data['Week_of_Year'] = week_of_year
            input_data['Year'] = year_focus
            
            target_store_col = f"Store_{store_id}"
            if target_store_col in input_data.columns:
                input_data[target_store_col] = 1.0
                
            predicted_sales = model.predict(input_data)[0]
            st.metric(label="Predicted Required Stock Demand Volume", value=f"${predicted_sales:,.2f}")
