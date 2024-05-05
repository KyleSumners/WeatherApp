import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
option = st.selectbox("Select data to view", options=("Temperature", "Sky"))

st.header(f"Temperature for the next {"day" if days == 1 else f"{days} days"} "
          f" in {place}")

if place:
    try:
        # Get the temperature or sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Dates", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        else:
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=100)
    except KeyError:
        st.text(f"{place} does not exist")