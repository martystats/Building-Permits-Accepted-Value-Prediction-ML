import streamlit as st
import pandas as pd
import joblib

# Load saved demo model and encoding maps
saved = joblib.load("permit_demo_model.pkl")
model = saved["model"]
permit_map = saved["permit_map"]
construction_map = saved["construction_map"]

st.set_page_config(page_title="Building Permit Value Predictor")

st.title("Building Permit Value Predictor")

st.subheader("Model Information")
st.info("""
Algorithm: Random Forest Regressor  
Target Variable: acceptedvalue  
Demo Features Used: buildingpermittype, typesofconstructionactual, issueyear  
Evaluation Type: Simplified Streamlit demo model
""")

st.subheader("Enter Permit Details")

permit_types = list(permit_map.keys())
construction_types = list(construction_map.keys())

selected_permit = st.selectbox("Permit Type", permit_types)
selected_construction = st.selectbox("Construction Type", construction_types)
issue_year = st.number_input("Issue Year", min_value=2000, max_value=2035, step=1)

if st.button("Predict Permit Value"):
    # convert selected categories to the numeric values used during training
    permit_value = float(permit_map[selected_permit])
    construction_value = float(construction_map[selected_construction])
    year_value = float(issue_year)

    input_data = pd.DataFrame(
        [[permit_value, construction_value, year_value]],
        columns=["buildingpermittype", "typesofconstructionactual", "issueyear"]
    )

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Permit Value: ${prediction:,.2f}")