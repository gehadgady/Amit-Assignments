import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.title('Wind Turbine Power Prediction App')
st.write('This is a simple example of a Streamlit app that shows some data analysis on the Wind Turbine dataset.')

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("../wind_turbine_maintenance_data.csv")  # Change filename if needed

df = load_data()

# showing the head()
st.subheader("Dataset Preview")
st.write("Here are the first few rows of the dataset:")
st.dataframe(df.head()) 

# let user decide what number of rows to show
rows = st.slider("Select number of rows to display", 1, 20, 5)
st.dataframe(df.head(rows))
