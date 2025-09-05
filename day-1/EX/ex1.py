text = "Python töötab"

"Python töötab"
# -*- coding: utf-8 -*-
# x = txt.encode("utf-8")
print("Python t\u00F6\u00F6tab")


# NAME EXERCISE
first_name = "Kaido"
surname = "Vetevoog"
full_name = first_name + " " + surname
print(full_name)
full_name_search = full_name.upper()
print(full_name_search)


# NUMBERS EXERCISE  
age = 150
height = 1.75
print(f"Mu vanus on {age} ja pikkus on {height}.")

# Mida väljastab järgmine koodirida?
print(age * first_name)

# Hashed name
hashed_name = surname[0] + (len(surname)-1)*surname[0].lower()
print(hashed_name)

# Initials
initials = first_name[:2] + surname[:2]
print(initials)

