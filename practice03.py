def is_even(number): 
    return number % 2 == 0
def print_even_massage(number):
    if is_even(number):
        print(f"{number} - juft son.")
    else:
        print(f"{number} - toq son")
        print("Juft yoki Toq son aniqlovchi dastur")
        number = int(input("Istalgan butun sonni kiriting: "))
        print_even_massage(number)