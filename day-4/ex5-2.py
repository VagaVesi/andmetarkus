# andmete töötlus sõnastikuga
import json

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

# Otsida välja kõik toidud, mille mineraalide hulgas on "Kaalium", ja väljasta nende nimed terminali.

# for tsükkel
for k, v in toidud.items():
    if "Kaalium" in v["mineraalid"]:
        print(k)
# Output: õun, banaan, kartul

# print  kasutades list comprehensionit
print([toit for toit in toidud if "Kaalium" in toidud[toit]["mineraalid"]])

# Kas toidu sees on mineraalid
# for toit in toidud:
#     if "mineraalid" in toidud[toit]:
#         print(toit + " On olemas")

# Lisada lisatunnus  "makro" väärtusega "süsivesikurohke", "rasvane" kui vastav osakaal
# makrotoitainetest on üle 50%. Muudel juhtudel lisa tekst "mitmekülgne"

for toidunimi, toiduomadus in toidud.items():
    kokku_g = toiduomadus["süsivesikud"] + \
        toiduomadus["rasv"] + toiduomadus["valk"]
    if toiduomadus["süsivesikud"] / kokku_g > 0.5:
        toiduomadus["makro"] = "süsivesikurohke"
    elif toiduomadus["rasv"] / kokku_g > 0.5:
        toiduomadus["makro"] = "rasvane"
    else:
        toiduomadus["makro"] = "mitmekülgne"

# print(toidud)

# Väljastab elemendi mille võti on õun
print("Väljastab elemendi mille võti on õun")
print(toidud["õun"])

# väljastab õuna mineraalid
print("väljastab õuna mineraalid")
print(toidud["õun"]['mineraalid'])

# väljastab esimesena leitud mineraali
print("väljastab esimesena leitud mineraali")
print(toidud["õun"]['mineraalid'][0])

# Salvestame tulemuse faili
with open("day-4/toidud.json", "w", encoding="utf-8") as f:
    json.dump(toidud, f, ensure_ascii=False, indent=2)


# Otsida välja kõik toidud, mille vitamiinide hulgas on vähemalt kaks B vitamiini ja lisa need uude sõnastikku "b_vitamini_rikkad"

vitamiinide_rikkad = []

for k, v in toidud.items():
    b_vitamiinide_arv = sum(
        1 for vit in v["vitamiinid"] if vit.startswith("B"))
    if b_vitamiinide_arv >= 2:
        vitamiinide_rikkad.append(k)

print("B vitamiini rikkad toidud:", vitamiinide_rikkad)

vitamiinide_rikkad_2 = []

for k, v in toidud.items():
    b_vitamiinide_arv = len(
        [vit for vit in v["vitamiinid"] if vit.startswith("B")])
    if b_vitamiinide_arv >= 2:
        vitamiinide_rikkad_2.append(k)

print("lahendus 2 B vitamiini rikkad toidud:", vitamiinide_rikkad_2)
