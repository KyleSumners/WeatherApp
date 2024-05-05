import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
option = st.selectbox("Select data to view", options=("Temperature", "Sky"))

st.header(f"Temperature for the next {days} {"day" if days == 1 else "days"} "
          f" in {place}")

data = get_data(place, days, option)

figure = px.line(labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure)
