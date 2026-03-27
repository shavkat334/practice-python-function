def is_valid_phone_number(phone):
    if len(phone) == 9 and phone.isdigit():
        return True
    else:
        return False

def main():
    print("--- Telefon raqami tekshiruvi ---")
    
    number = input("9 xonali telefon raqamingizni kiriting: ")
    
    if is_valid_phone_number(number):
        print("Raqam to'g'ri kiritildi.")
    else:
        print("Xatolik! Raqam faqat raqamlardan iborat va 9 ta bo'lishi kerak.")

if __name__ == "__main__":
    main()