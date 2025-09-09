
import pandas as pd

# Lae elektrihindade graafikud

source_data = pd.read_json('day-3/elektrihind/el_data_2024.json')
electricity_data = pd.json_normalize(source_data["data"])
print(electricity_data.head())

source_data_2 = pd.read_csv('day-3/tallinn_harku_2024.csv')
weather_data = pd.DataFrame(source_data_2)
print(weather_data.head())
