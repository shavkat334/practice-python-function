def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Overweight"

def main():
    print("--- BMI (Tana vazni indeksi) ---")
    w = float(input("Og'irlik (kg): "))
    h = float(input("Bo'y (metr, masalan 1.75): "))
    
    bmi = calculate_bmi(w, h)
    status = bmi_status(bmi)
    
    print(f"Sizning BMI ko'rsatkichingiz: {bmi:.2f}")
    print(f"Holati: {status}")

if __name__ == "__main__":
    main()