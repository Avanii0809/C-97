import random
num = random.randint(1, 9)
print(num)
for i in range(0, 5):
    xyz = int(input("Enter your guess: "))
    if num == xyz:
        print("Congrats! You got that right.")
        break
    else:
        print("Oops, try again.")