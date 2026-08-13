def is_Even(number):
    if number % 2 == 0:
        return True
    else:
        return False

Starting = 0
even_numbers = []
user_Input = int(input("Limit: "))
for every_value in range(0, user_Input + 1):
    if is_Even(every_value):
            even_numbers.append(every_value)

print(f"Even Numbers: {even_numbers}")
print("Finish")





grocery = ["rice", "water", "tomato", "Onion", "Ginger"]

for item in grocery:
    if item == "water":
        continue
    print(item)
print("\n")

for i in range(0, len(grocery)):
    print(grocery[i])
print("\n")

for i in range(0, 10, 2):
    print(i)