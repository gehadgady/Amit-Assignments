import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io


st.title('Wind Turbine Power Prediction App')
st.write('This is a simple example of a Streamlit app that shows some data analysis on the Wind Turbine dataset.')

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("streamlet/data/wind_turbine_maintenance_data.csv")  # Change filename if needed

df = load_data()

# showing the head()
st.subheader("Dataset Preview")
st.write("Here are the first few rows of the dataset:")
st.dataframe(df.head()) 

# let user decide what number of rows to show
rows = st.slider("Select number of rows to display", 1, 20, 5)
st.dataframe(df.head(rows))



# Display dataset info
st.subheader("Dataset Info")
st.write("Here are some details about the dataset:")

buffer = io.StringIO()  # Create an in-memory buffer
df.info(buf=buffer)  # Write df.info() output to buffer
info_str = buffer.getvalue()  # Get the string output

st.text(info_str)  # Display the info as plain text



# Streamlit app
st.title("Histogram Plots 📊")

st.subheader("Select a column to visualize its distribution")
column = st.selectbox("Choose a numerical column:", df.select_dtypes(include=["int", "float"]).columns)

# Plot histogram
fig, ax = plt.subplots()
sns.histplot(df[column], kde=True, bins=30, ax=ax)
ax.set_title(f"Histogram of {column}")

# Display plot in Streamlit
st.pyplot(fig)
