def is_Even(number):
    if number % 2 == 0:
        return True
    else:
        return False

Starting = 0
while Starting < 100:
    if is_Even(Starting):
        print(f"{Starting} Number is Even")
    else:
        print(f"{Starting} Number is Odd")
    Starting = Starting + 1

print("Finish")

even_numbers = []
Starting = 0
user_Input = int(input("Limit: "))
while Starting <= user_Input:
    if is_Even(Starting):
        even_numbers.append(Starting)
    Starting = Starting + 1

print(f"Even Numbers: {even_numbers}")
print("Finish")