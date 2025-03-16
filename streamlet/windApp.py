import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io

import joblib
from huggingface_hub import hf_hub_download


st.title('Wind Turbine Power Prediction App')
st.write('This is a simple example of a Streamlit app that shows some data analysis on the Wind Turbine dataset.')

# Load dataset
@st.cache_data
def load_data():
    # D:\Materials\ML and AI Diploma\THE PROJECT\Wind Turbine Predictive Maintenance\wind-turbine-predictive-maintenance\streamlet\streamlet\data\wind_turbine_maintenance_data.csv
    return pd.read_csv("./data/wind_turbine_maintenance_data.csv")  # Change filename if needed

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


# getting data from the user to use the model to predict

# Download the model from Hugging Face
model_path = hf_hub_download(repo_id="gehadgady/wind_turbine_model", filename="wind_turbine_model.pkl")

# Load the model
model = joblib.load(model_path)


st.title("Wind Turbine Maintenance Prediction ⚙️💨")

st.subheader("Enter Sensor Data:")
rotor_speed = st.number_input("Rotor Speed (RPM)", min_value=10.0, step=0.1)
wind_speed = st.number_input("Wind Speed (mps)", min_value=5.0, step=0.1)
power_output = st.number_input("Power Output (kW)", min_value=1000.0, step=0.1)
gearbox_temp = st.number_input("Gearbox Oil Temp (°C)", min_value=50.0, step=0.1)
generator_temp = st.number_input("Generator Bearing Temp (°C)", min_value=50.0, step=0.1)
vibration = st.number_input("Vibration Level (mm/s)", min_value=1.0, step=0.1)
ambient_temp = st.number_input("Ambient Temp (°C)", min_value=10.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=50.0, step=1.0)


if st.button("Predict Maintenance Status"):
    # input_data = np.array([[rotor_speed, wind_speed, power_output, gearbox_temp, 
    #                         generator_temp, vibration, ambient_temp, humidity]])
    input_data = pd.DataFrame([[rotor_speed, wind_speed, power_output, gearbox_temp, 
                            generator_temp, vibration, ambient_temp, humidity]], 
                        columns=['Rotor_Speed_RPM', 'Wind_Speed_mps', 'Power_Output_kW', 
                                'Gearbox_Oil_Temp_C', 'Generator_Bearing_Temp_C', 'Vibration_Level_mmps', 
                                'Ambient_Temp_C', 'Humidity_pct'])

    print(input_data)
    prediction = model.predict(input_data)[0]  # Get the predicted class

    if prediction == 0:
        st.success("✅ No Fix Needed")
    elif prediction == 1:
        st.warning("⚠️ Check-up Required")
    else:
        st.error("🚨 Immediate Fix Needed!")
