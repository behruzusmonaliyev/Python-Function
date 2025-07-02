def ask_question(question: str, correct_answer: str):
    user_answer = input(question + " ")
    return check_answer(user_answer, correct_answer)
def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.strip().lower() == correct_answer.strip().lower()
if ask_question("Ozbekiston Poytaxti nima?"  ", Toshkent"):
    print("Togri!")
else:
    print("Xato")