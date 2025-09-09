import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Lae elektrihindade graafikud

df = pd.read_json('day-3/elektrihind/el_data_2025.json')
df_expanded = pd.json_normalize(df["data"])


# Joonista joonis price

plt.figure(figsize=(12, 6))
plt.plot(df_expanded["price"], label="Price")
plt.title("Electricity Price in 2025")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()


# Andmed päevade kaupa
df_expanded['date'] = pd.to_datetime(df_expanded['datetime']).dt.date
daily_avg = df_expanded.groupby('date')['price'].mean().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(daily_avg['date'], daily_avg['price'],
         marker='o', linestyle='-', label="Daily Average")

# Trendijoone lisamine
x = np.arange(len(daily_avg['date']))
z = np.polyfit(x, daily_avg['price'], 1)
p = np.poly1d(z)
plt.plot(daily_avg['date'], p(x), color='red',
         linestyle='--', label='Trendijoon')

plt.title("Daily Average Electricity Price in 2025")
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
