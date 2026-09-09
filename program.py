import random


def hex_to_bin(hex_number):
    try:
        return format(int(hex_number, 16), '04b')
    except ValueError:
        return "Error: not a valid hex number"


def binary_to_hex(binary_number):
    try:
        return format(int(binary_number, 2), 'X')
    except ValueError:
        return "Error: not a valid binary number"


def run_quiz(number_of_questions=5):
    score = 0

    print("Hexadecimal and Binary Quiz")
    print("Conversions are randomly chosen. Enter q to quit.\n")

    for question_number in range(1, number_of_questions + 1):
        conversion = random.choice(("hex_to_bin", "bin_to_hex"))

        if conversion == "hex_to_bin":
            question = random.choice("0123456789ABCDEF")
            correct_answer = hex_to_bin(question)
            prompt = f"What is hexadecimal {question} in binary? "
        else:
            question = format(random.randrange(16), '04b')
            correct_answer = binary_to_hex(question)
            prompt = f"What is binary {question} in hexadecimal? "

        while True:
            answer = input(
                f"Question {question_number}/{number_of_questions}: "
                f"{prompt}"
            ).strip().replace(" ", "").upper()

            if answer.lower() == "q":
                print(f"\nYou scored {score}/{question_number - 1}.")
                return

            if conversion == "hex_to_bin":
                valid_answer = len(answer) == 4 and set(answer) <= {"0", "1"}
                error_message = "Please enter exactly four binary digits, such as 0101."
            else:
                valid_answer = len(answer) == 1 and answer in "0123456789ABCDEF"
                error_message = "Please enter one hexadecimal digit, such as A."

            if valid_answer:
                break

            print(error_message)

        if answer == correct_answer:
            score += 1
            print("Correct!\n")
        else:
            print(f"Not quite. The correct answer is {correct_answer}.\n")

    print(f"Quiz complete! You scored {score}/{number_of_questions}.")


if __name__ == "__main__":
    run_quiz()