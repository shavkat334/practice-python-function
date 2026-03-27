def ask_question(question, correct_answer):
    user_answer = input(f"{question}: ")
    return check_answer(user_answer, correct_answer)

def check_answer(user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        return True
    else:
        return False

def main():
    print("--- Mini Test ---")
    
    question = "O'zbekiston poytaxti qaysi shahar?"
    answer = "Toshkent"
    
    is_correct = ask_question(question, answer)
    
    if is_correct:
        print("To'g'ri!")
    else:
        print(f"Xato! To'g'ri javob: {answer}")

if __name__ == "__main__":
    main()