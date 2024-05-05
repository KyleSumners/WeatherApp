import os
import requests


def get_data(place, forecast_days=None, option=None):
    url = os.getenv("WEATHER_API_KEY")
    url = url + f"&q={place}"

    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if option == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    else:
        filtered_data = [dict["weather"][0]["temp"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    d = get_data("San Antonio", forecast_days=3, option="Temperature")
    print(len(d))
