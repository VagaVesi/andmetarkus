riigid = ["Eesti", "Austria", "Belgia", "Andorra",
          "Hispaania", "Soome", "Albaania", "Itaalia"]

# Leia ja salvesta eraldi järjendisse kõik riigid, mis algavad A ja E tähega. Prindi uus nimek terminali.

# list comprehension
riigid_ae = [riik for riik in riigid if riik.startswith(("A", "E"))]

# for tsükkel
riigid_ae2 = []
for riik in riigid:
    if riik[0] in ("A", "E"):
        riigid_ae2.append(riik)


# for tsükkel
riigid_ae3 = []
for riik in riigid:
    if riik.startswith("A") or riik.startswith("E"):
        riigid_ae3.append(riik)

# testime lahendusi
print(riigid_ae)
print(riigid_ae2)
print(riigid_ae3)
# Output: ['Eesti', 'Austria', 'Andorra', 'Albaania']
