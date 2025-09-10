# import re

text = "Tere!   (Kas sa tuled?)  Ma ei tea...võib-olla,   aga -- vaatame!  Õhtul, kell 18:00, \"Kohvikus\"."

# Eemalda liigsed tühikud (asenda mitu tühikut ühega)
# text = re.sub(r'\s+', ' ', text).strip()

# alternatiivne viis tühikute eemaldamiseks kasutades string meetodit
text = text.replace("  ", " ")

# Eemalda kõik sulud ja nende sees olev tekst
# text = text.replace("(", "").replace(")", "").replace(
#    "\"", "").replace("...", ", ").replace("--", ", ").replace("  ", " ").replace(" ,", ",")

text = text.replace("\\", "")
print(text)
