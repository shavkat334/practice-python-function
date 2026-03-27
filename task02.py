def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    return age

def check_status(age):
    if age >= 18:
        print("Siz balog'atga yetgansiz")
    else:
        print("Siz balog'atga yetmagansiz")

def main():
    print("--- Yosh Hisoblagich ---")
    
    birth_year = int(input('Tug\'ilgan yilingizni kiriting: '))
    current_year = int(input('Hozirgi yilni kiriting: '))

    age = calculate_age(birth_year, current_year)
    print(f"Yoshingiz: {age}")
    
    check_status(age)

if __name__ == "__main__":
    main()