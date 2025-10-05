import random

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return f"{num1} {operator} {num2}", answer

def math_quiz():
    score = 0
    rounds = 10

    print("\n--- Selamat datang di game quiz matematika! ---")
    print("You will be presented with math problems, and you need to provide the correct answer.")

    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"\nQuestion {i + 1}: {question}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue  # Skip to the next question if input is invalid

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    # Print the result after all questions
    print("\n--- Game selesai! ---")
    print(f"Skor akhir Anda adalah: {score}/{rounds}")
    if score == rounds:
        print("Selamat! Anda berhasil menjawab semuanya dengan benar.")
    elif score >= rounds // 2:
        print("Bagus! Anda sudah mencoba.")
    else:
        print("Teruslah berlatih! You can do better next time.")

math_quiz()
