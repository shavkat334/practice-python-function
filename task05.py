def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To'g'ri topdingiz!")
    else:
        print("Xato, qaytadan urinib ko'ring.")

def main():
    secret = 7
    print("--- Sonni topish o'yini ---")
    
    guess = int(input("1 dan 10 gacha son kiriting: "))
    
    is_correct = check_guess(secret, guess)
    print_result(is_correct)

if __name__ == "__main__":
    main()