import numpy as np
import pandas as pd

ilmaandmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "temperatuur": [18.5, 19.2, 17.8, 16.4, 15.9],
    "niiskus": [65, 60, 70, 68, 75],
    "tuul": [4.2, 3.8, 5.0, 4.5, 6.1]
}

linnad_andmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "elanike_arv": [440000, 95000, 51000, 57000, None],
    "pindala": [159.2, 38.8, 32.2, 84.5, 15.0]  # km²
}

ilma_df = pd.DataFrame(ilmaandmed)
linnad_df = pd.DataFrame(linnad_andmed)

# Ühenda andmed linnade alusel
koond_df = pd.merge(ilma_df, linnad_df, on="linn")

# Paranda Nan kui linna väärtus on kuressaare
koond_df.loc[koond_df['linn'] == 'Kuressaare', 'elanike_arv'] = 13000


# Leia, millises linnas on kõrgeim temperatuur.

max_temp = koond_df['temperatuur'].max()
linna_nimi = koond_df.loc[koond_df['temperatuur']
                          == max_temp, 'linn'].values[0]
print(f"Kõrgeim temperatuur on {max_temp}°C linnas {linna_nimi}")

# Leia, millises linnas on kõrgeim temperatuur.
max_temp_row = koond_df[koond_df['temperatuur']
                        == koond_df['temperatuur'].max()]
print(max_temp_row)

# Arvuta iga linna rahvastikutihedus (elanike arv / pindala). Lisaveeruna

koond_df['rahvastikutihedus'] = (
    koond_df['elanike_arv'] / koond_df['pindala']).round(1)


# Filtreeri välja linnad, kus niiskus on üle 70%.
niisked_linnad = koond_df[koond_df['niiskus'] > 70]

# Sorteeri andmed tuule kiiruse järgi kasvavalt.
koond_df = koond_df.sort_values(by='tuul', ascending=True)

# Lisa uus veerg, mis näitab kas temperatuur on üle keskmise ("üle keskmise" / "alla keskmise").

keskmine_temp = koond_df['temperatuur'].mean()

koond_df["temp_kategooria"] = np.where(
    koond_df["temperatuur"] > keskmine_temp,
    "üle keskmise",
    "alla keskmise"
)

# Asenda kõik linnanimed suurte tähtedega.
koond_df['linn'] = koond_df['linn'].str.upper()

# salvestame tulemuse faili
koond_df.to_csv("day-4/koond_andmed.csv", index=False)

print(koond_df)
