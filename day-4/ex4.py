# Andmete töötlus

sonad = ["    õun", "banaan    ", "    pirn    ", "ploom", "    viinamari    "]

# variant 1: kasutades string meetodit strip()

puhastatud_sonad = []
for sona in sonad:
    puhastatud_sonad.append(sona.strip())

print(puhastatud_sonad)

# variant 2: kasutades listi comprehensions ja string replace() meetodit
puhastatud_sonad = [sona.replace(" ", "") for sona in sonad]
print(puhastatud_sonad)

# Summade teisendus
summad = ["1,234.56", "12,000.00", "5,678.90", "100.00", "23,456.78"]
