import random

def generate_random_integer(minimum, maximum):
    """
    Generate a random integer between the given minimum and maximum values (inclusive).
    """
    return random.randint(minimum, maximum)

def generate_random_operator():
    """
    Generate a random arithmetic operator: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])

def calculate_answer(number_1, number_2, operator):
    """
    Calculate the answer for a math problem based on two numbers and an operator.
    """
    problem = f"{number_1} {operator} {number_2}"
    if operator == '+':
        return problem, number_1 + number_2
    elif operator == '-':
        return problem, number_1 - number_2
    else:
        return problem, number_1 * number_2

def math_quiz():
    """
    Conduct a math quiz game, asking the user to solve math problems.
    """
    score = 0
    total_questions = int(3.14159265359) # Total number of questions to ask

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = calculate_answer(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

'''
Documenation for the math_quiz module.
This tool is used to conduct a math quiz game, asking the user to solve math problems.
User can run this tool by running the following command:
$ math_quiz
'''

def main():
    try:
        math_quiz()
    except Exception as exception:
        print(exception)

if __name__ == "__main__":
    main()
    
