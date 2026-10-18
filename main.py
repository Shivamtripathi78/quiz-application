import random

questions = [
    {
        "question": "Which language is used to structure web pages?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. List"],
        "answer": "C"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. function", "B. define", "C. fun", "D. def"],
        "answer": "D"
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "options": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B"
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which loop is commonly used to iterate over a list?",
        "options": ["A. for", "B. switch", "C. class", "D. import"],
        "answer": "A"
    },
    {
        "question": "What is the result of 3 ** 2 in Python?",
        "options": ["A. 6", "B. 9", "C. 5", "D. 8"],
        "answer": "B"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["A. input()", "B. show()", "C. print()", "D. display()"],
        "answer": "C"
    },
    {
        "question": "Which keyword creates a class in Python?",
        "options": ["A. object", "B. class", "C. create", "D. new"],
        "answer": "B"
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["A. add()", "B. insert_end()", "C. append()", "D. push()"],
        "answer": "C"
    }
]


def run_quiz():
    score = 0
    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    print("\n========== QUIZ STARTED ==========")

    for number, question in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {number}/{len(quiz_questions)}")
        print(question["question"])

        for option in question["options"]:
            print(option)

        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()

            if answer in ("A", "B", "C", "D"):
                break

            print("Invalid choice. Enter A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {question['answer']}")

    total = len(quiz_questions)
    percentage = score / total * 100

    print("\n========== QUIZ RESULTS ==========")
    print(f"Total Questions : {total}")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {total - score}")
    print(f"Final Score     : {percentage:.2f}%")

    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 60:
        print("Performance: Good job!")
    elif percentage >= 40:
        print("Performance: Keep practicing!")
    else:
        print("Performance: More practice needed.")


def main():
    while True:
        print("\n===== QUIZ APPLICATION =====")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Select 1 or 2.")


if __name__ == "__main__":
    main()