import streamlit as st
import pandas as pd
import joblib

# Load saved demo model package
saved = joblib.load("permit_demo_model.pkl")
model = saved["model"]
permit_map = saved["permit_map"]
construction_map = saved["construction_map"]

# =========================
# PAGE TITLE
# =========================
st.title("Building Permit Value Predictor")

# =========================
# MODEL INFORMATION
# =========================
st.subheader("Model Information")
st.info(
    """
**Algorithm:** Random Forest Regressor  
**Target Variable:** acceptedvalue  
**Demo Features Used:** buildingpermittype, typesofconstructionactual, issueyear  
**Evaluation Type:** Simplified Streamlit demo model
"""
)

# =========================
# PERMIT OPTIONS
# =========================
permit_options = list(permit_map.keys())

# =========================
# HUMAN-FRIENDLY CONSTRUCTION LABELS
# =========================
construction_meanings = {
    "Unknown": "Unknown",
    "VN": "New Building Construction",
    "VB": "Wood Frame / Residential Building",
    "IA": "Interior Alteration",
    "I.F.R.": "Fire-Resistant Construction",
    "IIB": "Non-Combustible Building",
    "II N": "Non-Rated Commercial Building",
    "IB": "High-Rise Fire-Resistant Building",
    "IV": "Heavy Timber Construction",
    "IIIA": "Protected Combustible Construction",
    "IIA": "Fire-Resistant Light Construction",
    "VA": "Light Wood Construction",
    "IIIB": "Unprotected Combustible Construction",
    "IV H.T.": "Heavy Timber (Historic)"
}

# Only use codes that exist in trained model
valid_codes = list(construction_map.keys())

# Create display labels and reverse mapping
construction_display_options = []
display_to_code = {}

for code in valid_codes:
    meaning = construction_meanings.get(code, "Construction Type")
    label = f"{meaning} ({code})"   # 👈 USER FRIENDLY FORMAT
    construction_display_options.append(label)
    display_to_code[label] = code

# =========================
# INPUT SECTION
# =========================
st.subheader("Enter Permit Details")

# Permit dropdown
selected_permit = st.selectbox("Permit Type", permit_options)

# 👇 THIS IS WHERE THE CAPTION GOES
st.caption("Select the type of construction used for the building")

# Construction dropdown
selected_construction_display = st.selectbox(
    "Construction Type",
    construction_display_options
)

# Year input
issue_year = st.number_input("Issue Year", min_value=2000, max_value=2035, step=1)

# =========================
# PREDICTION
# =========================
if st.button("Predict Permit Value"):

    # Convert back to model codes
    selected_construction_code = display_to_code[selected_construction_display]

    permit_value = permit_map[selected_permit]
    construction_value = construction_map[selected_construction_code]

    # Create input dataframe
    input_data = pd.DataFrame(
        {
            "buildingpermittype": [permit_value],
            "typesofconstructionactual": [construction_value],
            "issueyear": [issue_year],
        }
    )

    # Predict
    prediction = model.predict(input_data)[0]

    # Display result
    st.success(f"Predicted Permit Value: ${prediction:,.2f}")