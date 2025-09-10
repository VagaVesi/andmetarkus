# regex
import re

text_to_analyze = "Minu kontonumber on 345678, aga vana konto oli 312345. Mõned näited, mida ei tohiks leida: 234567, 34567, 33445566, 39876, 399999, 3123457, 31234. Samuti on olemas 398765 ja 300001."
# regex täpselt 6-kohalistele numbritele, mis algavad 3-ga
pattern = r'\b3\d{5}\b'

matches = re.findall(pattern, text_to_analyze)
print(matches)

tekst2 = """See on esimene rida.
See on teine rida.
Kolmas rida on siin.
Neljandal real on samuti tekst."""

pattern2 = r'\n'

# Variant 1
tekst2_ilma_reavahetuseta = re.sub(pattern2, '', tekst2)
print(tekst2_ilma_reavahetuseta)

# Variant 2 ilma regexita
tekst2_ilma_reavahetuseta = tekst2.replace('\n', '')
print(tekst2_ilma_reavahetuseta)
