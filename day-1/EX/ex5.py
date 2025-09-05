# FOR tsükkel Lahendused

girl_names = ["Jaanika", "Malle", "Kersti", "Ann", "Mari", "Kati"]

""" # Väljasta kõik tüdrukute nimed ükshaaval, kasutades for tsüklit
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

print("\nLahendus teine neljas \n")
# teine kuni neljas
for name in girl_names[1:4]:
    print(name, end=" ")

print("\nLahendus elemendid tagurpidi \n")

for name in reversed(girl_names):
    print(name, end=" ")

print("\nLahendus paaris indeksiga elemendid \n")

# Alustab teisest nimest kuna algus on 1
for i in range(1, len(girl_names), 2):
    print(girl_names[i])

# Väljastame nimed mis algavad "K" tähega
print("\nLahendus nimed mis algavad K tähega \n")
for name in girl_names:
    if name.startswith("K"):
        print(name)

# lahendus 2

for name in girl_names:
    if name[0] == "K":
        print(name) """


# Moodustada sõnastik, mis sisaldab M tähega algavaid nimesid

sorted_names = {}

for name in girl_names:
    first_letter = name[0]
    # print("Esimene täht:", first_letter)
    if first_letter not in sorted_names:
        # print("Esimene kord, kui täht esineb:", first_letter)
        sorted_names[first_letter] = []
    if name.startswith(first_letter):
        # print(f"Nimi {name} lisatakse tähtede alla {first_letter}")
        sorted_names[first_letter].append(name)

print("\nSõnastik algustähtede järgi sorduna nimedega:\n", sorted_names)
print("\nNimed mis algavad M tähega:\n", sorted_names["M"])
