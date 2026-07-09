import random

secret_number = random.randint(1, 50)

print("===NUMBER GUESSING GAME===")
print("guess the number between 1 to 50")
print("you have five chances to guess the number\n")

for attempt in range(1, 6):
    print(f"---Attempt number {attempt}---")

    # 1. Yeh validation loop hai (Iske shuru mein spaces hona zaroori hain)
    while True:
        guess = int(input("enter your guess: "))

        if 1 <= guess <= 50:
            break  
        else:
            print("Invalid number! Please enter a number between 1 to 50. Try again.")
            continue

    # 2. MAIN LOGIC (Yeh 'while' ke barabar seedh mein hona chahiye)
    if guess == secret_number:
        print(f"Congratulations Manzar! you guessed the number in {attempt} attempts ")
        break
    elif guess < secret_number:
        print("Your guess is low! Try again: \n")
    else:
        print("Your guess is high! Try again: \n")

# 3. GAME OVER (Yeh 'for' loop ka else hai)
else:
    print("===GAME OVER===")
    print(f"Your five attempts are over! The secret number was {secret_number}. Best of luck for next time.")
