import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Renewable Energy Monitoring Simulator")

# Load data
solar_df = pd.read_csv('reports/monthly_solar_report.csv')
wind_df = pd.read_csv('reports/monthly_wind_report.csv')

st.header("Solar Energy")
st.line_chart(solar_df.set_index('Day')['Solar_Energy(kWh)'])

st.header("Wind Energy")
st.line_chart(wind_df.set_index('Day')['Wind_Energy(kWh)'])

st.header("Download Reports")
st.download_button("Download Solar Report", data=solar_df.to_csv(index=False), file_name="monthly_solar_report.csv")
st.download_button("Download Wind Report", data=wind_df.to_csv(index=False), file_name="monthly_wind_report.csv")