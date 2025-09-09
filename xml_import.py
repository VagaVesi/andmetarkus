import requests
import pandas as pd

url = "https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php"

response = requests.get(url)
xml_content = response.content

# Proovi leida sobiv XPath, nt kõik <place> elemendid
df = pd.read_xml(xml_content, xpath=".//place")

print(df.head())
