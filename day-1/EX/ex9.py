# Näidis newlist = [x for x in fruits if "a" in x]
girl_names = ["Jaanika", "Malle", "Kersti", "Ann",
              "Mari", "Kati", "Annika", "Aili", "Karmen"]

names_containing_a = [name for name in girl_names if "a" in name]

print(names_containing_a)  # ['Jaanika', 'Malle', 'Mari', 'Kati']

names_starting_with_A = [name for name in girl_names if name.startswith("A")]

print(names_starting_with_A)  # ['Ann', 'Annika', 'Aili']


# Nimed mis on lühemad kui 4 tähemärki
short_names = [name for name in girl_names if len(name) < 4]
print(short_names)  # ['Ann']
