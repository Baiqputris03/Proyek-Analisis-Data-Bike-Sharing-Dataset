import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Convert date column
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Select Year", day_df['dteday'].dt.year.unique())
selected_weather = st.sidebar.multiselect("Weather Condition", day_df['weathersit'].unique())

# Filter data
filtered_day_df = day_df[day_df['dteday'].dt.year == selected_year]
if selected_weather:
    filtered_day_df = filtered_day_df[filtered_day_df['weathersit'].isin(selected_weather)]

# Dashboard Title
st.title("Bike Sharing Dashboard")
st.markdown("### Overview of Bike Sharing Data")

# Display Data Summary
st.write("### Dataset Overview")
st.write(filtered_day_df.describe())

# Visualization 1: Rental Trends Over Time
st.write("### Rental Trends Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=filtered_day_df['dteday'], y=filtered_day_df['cnt'], ax=ax)
plt.xlabel("Date")
plt.ylabel("Total Rentals")
st.pyplot(fig)

# Visualization 2: Rentals by Season
st.write("### Rentals by Season")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x=filtered_day_df['season'], y=filtered_day_df['cnt'], ax=ax)
plt.xlabel("Season")
plt.ylabel("Total Rentals")
st.pyplot(fig)

# Visualization 3: Rentals by Weather Condition
st.write("### Rentals by Weather Condition")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x=filtered_day_df['weathersit'], y=filtered_day_df['cnt'], ax=ax)
plt.xlabel("Weather Condition")
plt.ylabel("Total Rentals")
st.pyplot(fig)

#ls untuk menjalankan perintah pada terminal mac
import streamlit as st

st.title("Bike Sharing Data Analysis 🚲")
st.write("Selamat datang di dashboard interaktif untuk analisis data Bike Sharing!")

pip install streamlit

# Run with: streamlit run dashboard.py