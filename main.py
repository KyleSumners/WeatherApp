import streamlit as st


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
st.selectbox("Select data to view", options=("Temperature", "Sky"))

st.header(f"Temperature for the next {days} {"day" if days == 1 else "days"} "
          f" in {place}")
