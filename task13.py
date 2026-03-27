def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def main():
    print("--- Palindrom Tekshiruvi ---")
    t = input("So'z yoki gap kiriting: ")
    
    if is_palindrome(t):
        print("Ha, bu palindrom.")
    else:
        print("Yo'q, bu palindrom emas.")

if __name__ == "__main__":
    main()