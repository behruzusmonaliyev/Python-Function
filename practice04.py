def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
         return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"
    print ("Baxolash tizimi")
    score = int(input("Baliingizni kiriting (0-10): "))
    grade = get_grade(score)
    print(f"Sizning baxoyingiz: {grade}")