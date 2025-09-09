import requests
import pandas as pd

url = "https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php"

response = requests.get(url)
xml_content = response.content

# Proovi leida sobiv XPath, nt kõik <place> elemendid
df = pd.read_xml(xml_content, xpath=".//place")

min_temp_row = df[df['tempmin'] == df['tempmin'].min()]
max_temp_row = df[df['tempmin'] == df['tempmin'].max()]

# Rühmitame temperatuuriskaala järgi (nt tempmin)
# Näiteks: mitu linna igas tempmin väärtuses
grouped = df.groupby("tempmin").size().reset_index(name="count")

print(min_temp_row)
print(max_temp_row)
print(grouped)
