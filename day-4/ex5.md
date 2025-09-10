# Kordamine

## For-tsükkel Pythonis

```python
nimed = ["Mari", "Jüri", "Kati"]
for nimi in nimed:
    print("Tere,", nimi + "!")
```

Väljund:
```
Tere, Mari!
Tere, Jüri!
Tere, Kati!
```

## Ülesanne 1 (järjend)

 Kirjuta for-tsükliga programm, mis leiab ja väljastab salvestab teise järjendisse kõik riigid, mis algavad kas E või A tähega. Väljasta järjendi sisu terminali.

**Näide loendist:**
```python
riigid = ["Eesti", "Austria", "Belgia", "Andorra", "Hispaania", "Soome", "Albaania", "Itaalia"]
```

## Näited sõnastiku kohta

### Näide: sõnastiku võtmete ja väärtuste väljastamine for-tsükliga

    key = riik, value = linn
    for k, v in dictionary.items


```python
pealinnad = {
    "Eesti": "Tallinn",
    "Soome": "Helsingi",
    "Rootsi": "Stockholm"
}

for riik, linn in pealinnad.items():
    print(f"{riik} pealinn on {linn}")
```

Väljund:
```
Eesti pealinn on Tallinn
Soome pealinn on Helsingi
Rootsi pealinn on Stockholm
```

## Ülesanne 2 (sõnastik)

**Näidisandmed:**
```python
toidud = {
    "õun": {
        "kalorsus": 52,
        "vitamiinid": ["C", "K", "B6"],
        "mineraalid": ["Kaalium", "Magneesium"],
        "süsivesikud": 14,
        "rasv": 0.2,
        "valk": 0.3
    },
    "banaan": {
        "kalorsus": 89,
        "vitamiinid": ["C", "B6"],
        "mineraalid": ["Kaalium", "Magneesium"],
        "süsivesikud": 23,
        "rasv": 0.3,
        "valk": 1.1
    },
    "kanafilee": {
        "kalorsus": 165,
        "vitamiinid": ["B3", "B6", "B12"],
        "mineraalid": ["Fosfor", "Seleen"],
        "süsivesikud": 0,
        "rasv": 3.6,
        "valk": 31.0
    },
    "kartul": {
        "kalorsus": 77,
        "vitamiinid": ["C", "B6"],
        "mineraalid": ["Kaalium", "Raud"],
        "süsivesikud": 17,
        "rasv": 0.1,
        "valk": 2.0
    },
    "lõhe": {
        "kalorsus": 208,
        "vitamiinid": ["D", "B12", "B6"],
        "mineraalid": ["Seleen", "Fosfor"],
        "süsivesikud": 0,
        "rasv": 13.0,
        "valk": 20.0
    },
    "riis": {
        "kalorsus": 130,
        "vitamiinid": ["B1", "B3", "B6"],
        "mineraalid": ["Magneesium", "Fosfor"],
        "süsivesikud": 28,
        "rasv": 0.3,
        "valk": 2.7
    }
}
```

**Mida sõnastikuga on vaja teha:**
- [ ] Otsida välja kõik toidud, mille mineraalide hulgas on "Kaalium", ja väljasta nende nimed terminali.
- [ ] Lisada lisatunnus  "makro" väärtusega "süsivesikurohke", "rasvane" kui vastav osakaal makrotoitainetest on üle 50%. Muudel juhtudel lisa tekst "mitmekülgne"
- [ ] Otsida välja kõik toidud, mille vitamiinide hulgas on vähemalt kaks B vitamiini ja lisa need uude sõnastikku "b_vitamini_rikkad"



