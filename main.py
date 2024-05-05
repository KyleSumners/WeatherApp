import streamlit as st
import plotly.express as px


def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 12, 15]
    temperatures = [i * days for i in temperatures]
    return dates, temperatures


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
st.selectbox("Select data to view", options=("Temperature", "Sky"))

st.header(f"Temperature for the next {days} {"day" if days == 1 else "days"} "
          f" in {place}")
d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure)
