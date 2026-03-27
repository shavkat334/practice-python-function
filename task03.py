def check_even_odd(number):
    # Sonni 2 ga bo'lgandagi qoldig'ini tekshiramiz
    if number % 2 == 0:
        return "Juft son"
    else:
        return "Toq son"

def display_result(num, status):
    print(f"Kiritilgan son: {num}")
    print(f"Natija: Bu {status}")

def main():
    print("--- Juft yoki Toq sonni aniqlash ---")
    
    try:
       
        user_input = int(input("Biror son kiriting: "))
        
        
        result_status = check_even_odd(user_input)
        

        display_result(user_input, result_status)
        
    except ValueError:
        print("Xatolik! Iltimos, faqat butun son kiriting.")

if __name__ == "__main__":
    main()