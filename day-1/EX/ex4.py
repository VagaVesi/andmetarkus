def is_adult(age: int) -> bool:
    """Check if the given age represents an adult (18 or older)."""
    if not isinstance(age, int) or age < 0:
        return False
    elif age >= 18:
        return True
    else:
        return False 

# lühendatud versioon
    #return age >= 18  
# see tagastab juba ise True või False

""" # Test cases
print(is_adult(20))  # True
print(is_adult("Mari"))  # "Andmed vigased"
print(is_adult(16))  # False
print(is_adult(-1))  # "Andmed vigased"

age = 15
if is_adult(age):
    print("Võib Valida")
else:
    print("Ei või Valida") """

## Kas riik on Põhjamaade hulgas

eu_northen_country_codes = ["DK", "EE", "FI", "IS", "LT", "LV", "NO", "SE"]

def is_northen_country(country_code: str):
    """Check if the given country code is in the list of northern European countries."""
    if not isinstance(country_code, str) or len(country_code) != 2:
        return False
    return country_code in eu_northen_country_codes

print("Väärtus EE " + str(is_northen_country("EE")))  # True
print(is_northen_country("US"))  # False
print(is_northen_country("Est"))  # False
print(is_northen_country(123))  # False