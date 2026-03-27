def is_strong_password(password):
    if len(password) >= 8 and not password.isspace():
        return True
    else:
        return False

def main():
    print("--- Parol tekshiruvi ---")
    
    p = input("Yangi parolni kiriting: ")
    
    if is_strong_password(p):
        print("Parol mustahkam!")
    else:
        print("Xatolik! Parol kamida 8 ta belgidan iborat bo'lishi kerak.")

if __name__ == "__main__":
    main()