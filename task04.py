def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    print("--- Baholash Tizimi ---")
    
    score_input = int(input("To'plangan ballni kiriting (0-100): "))
    
    if 0 <= score_input <= 100:
        grade = get_grade(score_input)
        print(f"Sizning bahongiz: {grade}")
    else:
        print("Xatolik! Ball 0 va 100 oralig'ida bo'lishi kerak.")

if __name__ == "__main__":
    main()