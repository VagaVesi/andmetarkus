# paigalda pip install tools.api_request

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# url = "https://demo-datahub.rik.ee/api/v1/meta/classifications"

url_riik = 'https://api.worldbank.org/v2/countries/EST/?format=json'
url_rahvastik_ = 'https://api.worldbank.org/v2/country/EST/indicator/SP.POP.TOTL?format=json'

response = requests.get(url_rahvastik_)
data = response.json()

# json dumps muudab väljundi terminalis loetavaks
# print(json.dumps(data, indent=2, ensure_ascii=False))

values = {'year': [], 'population': []}

for item in data[1]:
    values['year'].append(item['date'])
    values['population'].append(item['value'])

# print(json.dumps(values, indent=2, ensure_ascii=False))

df = pd.DataFrame(values)

df.plot(x='year', y='population', kind='line', marker='o',
        title='Eesti rahvaarv aastatel 1960-2021', xlabel='Aasta', ylabel='Inimeste arv')

plt.show()

print(df)

# response_df = pd.json_normalize(data)
# print(response_df)
