your_marks = int(input("Enter your marks in programming: "))

def show_Grade(grade):
    print(f"You got: {grade}")

if your_marks >= 80:
    show_Grade("A+")
elif your_marks >= 70 and your_marks < 80:
    show_Grade("A")
elif your_marks >= 60 and your_marks < 70:
    show_Grade("A-")
elif your_marks >= 50 and your_marks < 60:
    show_Grade("B")
elif your_marks >= 40 and your_marks < 50:
    show_Grade("C")
elif your_marks >= 33 and your_marks < 40:
    show_Grade("D")
else:
    show_Grade("F")

print("Finished")