""" boys_names = ["Ain", "Peeter", "Kusti", "Karl"]
boys_names.append("Valdek")
print(boys_names)
girls_names = ["Jaanika", "Malle", "Kersti", "Ann"]
names = []
print(names)
names = boys_names + girls_names
print("names: " + str(names))

# järjendi pikkus
print(len(names))

# sorteeritud nimekiri
sorted_names = sorted(names)
print("sorted names: " + str(sorted_names))

print(min(names))

print(max(names))
boys_names.sort()
sorted2 = sorted(girls_names)
print(boys_names)


transaction_customer_id = [1, 2, 5, 2, 4, 8]
print(transaction_customer_id)
unique_customer_id = set(transaction_customer_id)
print(unique_customer_id)
all_customers = set(range(1, 11))
print(all_customers)

passive_customers = all_customers - unique_customer_id
print(passive_customers)
 """

my_company_data = {"id": 12345678
                   , "name": "My Company OÜ"
                   , "year_sales": {2023: 10000, 2024: 20000, 2025: 30000}
                   , "activity": "IT services"}
print(my_company_data)

my_company_data["name"] = "UUS NIMI"
print(my_company_data)

my_company_data.update({"address": "Tartu mnt 1, Tallinn"})
print(my_company_data)

my_company_data["year_sales"][2025] = 40000
print(my_company_data)
my_company_data["year_sales"].update({2026: 50000})
print(my_company_data)

# Tuple

popular_boys_names = ("Peeter", "Karl")
print(popular_boys_names)
random_data = (1, "tere", 1.75, True, None, [1, 2, 3], (4, 5) )
print(random_data)