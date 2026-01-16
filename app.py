import pickle
import pandas as pd
import streamlit as st

#setup
st.set_page_config(page_icon="",page_title="House Price prediction",layout="wide")


#load RF model
with open("RF_model.pkl","rb") as file:
    model = pickle.load(file)

#load dataset
df = pd.read_csv("cleaned_df.csv")


with st.sidebar:
    st.title("House Price Prediction App")
    st.image("hose_logo.avif",width=300)

def get_encoded_loc(location):
    for loc,encoded in zip(df["location"],df["encoded_loc"]):
        if location==loc:
            return encoded

#input fields  --> location,sqft,bath,bhk
with st.container(border=True):
    col1,col2 = st.columns(2)
    with col1:
        location = st.selectbox("🗺️ Location: ",options=df["location"].unique())
        sqft = st.number_input("📐 Sqr.ft: ",min_value=300)
    with col2:
        bath = st.selectbox("🛁 No of bathrroms: ",options=sorted(df["bath"].unique()))
        bhk = st.selectbox("🏠 BHK: ",options=sorted(df["bhk"].unique()))

    encoded_loc = get_encoded_loc(location)

    c1,c2,c3 = st.columns([2.2,2,1])
    if c2.button("💲Predict"):
        #model prediction
        inp_data = [[sqft,bath,bhk,encoded_loc]]
        pred = model.predict(inp_data)
        pred = float(f"{pred[0]:.2f}")
        st.subheader(f"Predicted Price: Rs. {pred*100000}")