import os
import requests


def get_data(place, forecast_days=None):
    url = "http://api.openweathermap.org/data/2.5/forecast?appid="
    url = url + os.getenv("WEATHER_API_KEY")
    url = url + f"&q={place}"

    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    d = get_data("San Antonio", forecast_days=3)
    print(d)
