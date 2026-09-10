import random

Num_Of_Question = 7


def hex_to_bin(hex_number, num_bits=4):
    try:
        return format(int(hex_number, 16), f'0{num_bits}b')
    except ValueError:
        return "Error: not a valid hex number"


def binary_to_hex(binary_number, hex_digits=1):
    try:
        return format(int(binary_number, 2), f'0{hex_digits}X')
    except ValueError:
        return "Error: not a valid binary number"


def get_num_bits():
    while True:
        choice = input("Enter number of bits (multiples of 4, e.g. 4, 8, 12, 16) [default: 4]: ").strip()
        if not choice:
            return 4
        if choice.isdigit():
            bits = int(choice)
            if bits > 0 and bits % 4 == 0:
                return bits
        print("Please enter a positive multiple of 4 (e.g. 4, 8, 12, 16).")


def run_quiz(number_of_questions=5):
    score = 0
    print("---------------------------")
    print("Hexadecimal and Binary Quiz")
    print("---------------------------")

    num_bits = get_num_bits()
    hex_digits = num_bits // 4
    max_value = 1 << num_bits

    print(f"\nQuiz set to {num_bits} bits ({hex_digits} hex digit{'s' if hex_digits > 1 else ''}).")
    print("Conversions are randomly chosen. Enter q to quit.\n")

    for question_number in range(1, number_of_questions + 1):
        conversion = random.choice(("hex_to_bin", "bin_to_hex"))
        val = random.randrange(max_value)

        if conversion == "hex_to_bin":
            question = format(val, f'0{hex_digits}X')
            correct_answer = hex_to_bin(question, num_bits)
            prompt = f"What is hexadecimal {question} in binary? "
        else:
            question = format(val, f'0{num_bits}b')
            correct_answer = binary_to_hex(question, hex_digits)
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
                valid_answer = len(answer) == num_bits and set(answer) <= {"0", "1"}
                error_message = f"Please enter exactly {num_bits} binary digits (0s and 1s)."
            else:
                valid_answer = len(answer) == hex_digits and all(c in "0123456789ABCDEF" for c in answer)
                error_message = f"Please enter exactly {hex_digits} hexadecimal digit{'s' if hex_digits > 1 else ''} (0-9, A-F)."

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
    run_quiz(Num_Of_Question)
