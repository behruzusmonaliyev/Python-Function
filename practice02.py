def calculate_age(birth_year, current_year):
    return current_year - birth_year 
print("Yosh hisoblagich")
birth_year = int(input("Tugilgann yilingizni kiriting: "))
current_year = int(input("Hozirgi yilni kiriting"))
age = calculate_age(birth_year, current_year)
print("Sizning yoshingiz:", age)
if age >= 18:
    print("Siz balogatga yetgansiz.")
else:
    print("Siz hali balogat yoshiga yetmagansiz.")