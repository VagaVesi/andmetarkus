import pandas as pd
# Lae elektrihindade graafikud

df = pd.read_json('day-3/elektrihind/el_data_2025.json')
df_expanded = pd.json_normalize(df["data"])
print(df_expanded)
