import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ===============================
# PAGE SETTINGS
# ===============================
st.set_page_config(
    page_title="Telecom Churn Prediction",
    page_icon="📡",
    layout="centered"
)

# ===============================
# TECH BACKGROUND STYLE
# ===============================
st.markdown("""
<style>

.stApp{
background: radial-gradient(circle at top,#02111b,#061f3a,#000814);
color:white;
overflow:hidden;
}

/* floating bubbles */
.bubble{
position:fixed;
bottom:-100px;
width:40px;
height:40px;
background:rgba(0,229,255,0.15);
border-radius:50%;
animation:rise 15s infinite ease-in;
}

@keyframes rise{
0%{
transform:translateY(0);
opacity:0.4;
}
50%{
opacity:0.8;
}
100%{
transform:translateY(-120vh);
opacity:0;
}
}

h1{
text-align:center;
color:#00E5FF;
font-weight:700;
}

.stButton>button{
background-color:#00E5FF;
color:black;
font-size:18px;
border-radius:10px;
padding:10px 25px;
}

.stButton>button:hover{
background-color:#00bcd4;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# BUBBLE ANIMATION
# ===============================
st.markdown("""
<div class="bubble" style="left:10%; animation-delay:0s"></div>
<div class="bubble" style="left:25%; animation-delay:2s"></div>
<div class="bubble" style="left:40%; animation-delay:4s"></div>
<div class="bubble" style="left:55%; animation-delay:1s"></div>
<div class="bubble" style="left:70%; animation-delay:3s"></div>
<div class="bubble" style="left:85%; animation-delay:5s"></div>
""", unsafe_allow_html=True)

# ===============================
# LOAD MODEL
# ===============================
model = pickle.load(open("model.pkl", "rb"))

# ===============================
# TITLE
# ===============================
st.markdown(
"""
<h1>📡 Telecom Customer Churn Prediction</h1>
<p style='text-align:center;color:#B0BEC5;font-size:18px;'>
Predict whether a telecom customer is likely to leave the service.
</p>
""",
unsafe_allow_html=True
)

# ===============================
# INPUT LAYOUT
# ===============================
col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Customer Tenure (months)", min_value=0.0)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0)

with col2:
    total_charges = st.number_input("Total Charges", min_value=0.0)

    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

st.write("")

# ===============================
# PREDICT BUTTON
# ===============================
if st.button("🔍 Predict Churn"):

    # convert categories to numbers
    if contract == "Month-to-month":
        contract = 0
    elif contract == "One year":
        contract = 1
    else:
        contract = 2

    if internet_service == "DSL":
        internet_service = 0
    elif internet_service == "Fiber optic":
        internet_service = 1
    else:
        internet_service = 2

    # create input array
    input_data = np.array([[tenure, monthly_charges, total_charges]])

    prediction = model.predict(input_data)

    st.write("Prediction value:", prediction[0])

    if prediction[0] == "Yes":
        st.error("⚠️ Customer will Churn")
    else:
        st.success("✅ Customer will NOT Churn")