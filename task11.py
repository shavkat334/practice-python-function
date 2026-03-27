def calculate_tax(salary):
    if salary > 5000000:
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    return salary - tax

def main():
    print("--- Soliq Hisoblagich ---")
    s = float(input("Maoshingizni kiriting: "))
    
    tax = calculate_tax(s)
    net = calculate_net_salary(s)
    
    print(f"Soliq: {tax} so'm")
    print(f"Qo'lga tegadigan maosh: {net} so'm")

if __name__ == "__main__":
    main()