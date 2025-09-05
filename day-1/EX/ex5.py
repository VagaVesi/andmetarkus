# FOR tsükkel Lahendused

girl_names = ["Jaanika", "Malle", "Kersti", "Ann", "Mari", "Kati"]

# Väljasta kõik tüdrukute nimed ükshaaval, kasutades for tsüklit
for name in girl_names:
    print(name)

# Väjasta esimesed 2 - lahendus 1

# lisatud reavahtusega
print("\nLahendus 1 \n")

for i in range(2):
    print(girl_names[i])

print("\nLahendus 2 \n")

# piirame järjendi pikkust kahe esimese elemendiga
for name in girl_names[:2]:
    print(name)