age = 20

if age >= 16:
    print("Võid hääletada KOV valmistel")
    if age >= 18:
        print("Võid hääletada Riigikogu valmistel")
else:
    print("Oota veel veidi, saad varsti hääletada")


#   Väärtuse kontroll
number_to_check = 150

if number_to_check < 100:
    print(f"Muutuja väärtus {number_to_check} on alla 100")
elif number_to_check == 100:
    print(f"Muutuja väärtus {number_to_check} on täpselt 100")
else:
    print(f"Muutuja väärtus {number_to_check} on üle 100")

# Kas täiskasvanud?

is_adult = age >= 18
print(f"Kas isik on täiskasvanud? {is_adult}")

if age >= 18:
    print("Isik on täiskasvanud")
else:
    print("Isik ei ole täiskasvanud")

print("Isik on täiskasvanud") if age >= 18 else print("Isik ei ole täiskasvanud")
