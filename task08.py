def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("--- Haroratni o'zgartirgich ---")
    
    c = float(input("Selsiy (C) darajasini kiriting: "))
    f_result = c_to_f(c)
    print(f"{c} C = {f_result} F")
    
    f = float(input("\nFarengeyt (F) darajasini kiriting: "))
    c_result = f_to_c(f)
    print(f"{f} F = {c_result} C")

if __name__ == "__main__":
    main()