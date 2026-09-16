import random

def main() -> None:
    num: int = random.randint(1, 32)
    ans: int = 2**num

    print(f"What is 2 to the power of {num}?")
    input_ans = input("Your answer: ")
    check_answer(input_ans, ans)
    again: str = input("again? (y/n)")
    if again == "y":
        main()
    return

def check_answer(input_ans: str, ans: int) -> None:
    if input_ans.lower() == "s":
        print(f"The answer is: {ans}")
        return
    if input_ans.isdigit():
        if int(input_ans) == ans:
            print("Correct!")
        else:
            print(f"Incorrect. please try again\n")
            print("press s to show answer")
            check_answer(input("Your answer: "), ans)
    else:
        print("Please enter a valid number.")
        check_answer(input("Your answer: "), ans)

if __name__ == "__main__":
    main()