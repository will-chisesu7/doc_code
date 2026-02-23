import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "What is 12 x 12?",
        "options": ["A. 124", "B. 144", "C. 132", "D. 148"],
        "answer": "B"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["A. Venus", "B. Earth", "C. Mars", "D. Mercury"],
        "answer": "D"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    },
    {
        "question": "Who wrote Romeo and Juliet?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. O2", "B. CO2", "C. H2O", "D. HO"],
        "answer": "C"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 7"],
        "answer": "D"
    },
    {
        "question": "What is the fastest land animal?",
        "options": ["A. Lion", "B. Cheetah", "C. Horse", "D. Leopard"],
        "answer": "B"
    },
    {
        "question": "Which country invented the internet?",
        "options": ["A. Japan", "B. UK", "C. USA", "D. Germany"],
        "answer": "C"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 9", "C. 7", "D. 8"],
        "answer": "D"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Quartz"],
        "answer": "C"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A. 5", "B. 7", "C. 8", "D. 6"],
        "answer": "D"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"],
        "answer": "C"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "How many bones are in the adult human body?",
        "options": ["A. 206", "B. 180", "C. 250", "D. 198"],
        "answer": "A"
    },
    {
        "question": "Which country is the largest in the world by area?",
        "options": ["A. China", "B. USA", "C. Canada", "D. Russia"],
        "answer": "D"
    },
    {
        "question": "What is the currency of the United Kingdom?",
        "options": ["A. Euro", "B. Dollar", "C. Pound", "D. Franc"],
        "answer": "C"
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["A. Jupiter", "B. Mars", "C. Saturn", "D. Neptune"],
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Michelangelo", "B. Picasso", "C. Van Gogh", "D. Leonardo da Vinci"],
        "answer": "D"
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["A. Amazon", "B. Yangtze", "C. Nile", "D. Mississippi"],
        "answer": "C"
    },
    {
        "question": "How many players are on a football (soccer) team?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 9"],
        "answer": "B"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["A. Monaco", "B. San Marino", "C. Liechtenstein", "D. Vatican City"],
        "answer": "D"
    },
    {
        "question": "Which element has the atomic number 1?",
        "options": ["A. Helium", "B. Oxygen", "C. Hydrogen", "D. Carbon"],
        "answer": "C"
    },
    {
        "question": "What year did World War II end?",
        "options": ["A. 1943", "B. 1944", "C. 1945", "D. 1946"],
        "answer": "C"
    },
    {
        "question": "Which programming language is known as the language of the web?",
        "options": ["A. Python", "B. Java", "C. C++", "D. JavaScript"],
        "answer": "D"
    },
]


def play_quiz():
    print("=" * 50)
    print("           WELCOME TO THE QUIZ GAME")
    print("=" * 50)
    print("Answer each question by typing A, B, C, or D.\n")

    score = 0
    selected = random.sample(questions, len(questions))

    for i, q in enumerate(selected, start=1):
        print(f"Question {i}/{len(selected)}: {q['question']}")
        for option in q["options"]:
            print(f"  {option}")

        while True:
            answer = input("Your answer: ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("  Correct!\n")
            score += 1
        else:
            correct_option = next(o for o in q["options"] if o.startswith(q["answer"]))
            print(f"  Wrong! The correct answer was {correct_option}\n")

    print("=" * 50)
    print(f"  GAME OVER! You scored {score}/{len(selected)}")

    if score == len(selected):
        print("  Perfect score! Outstanding!")
    elif score >= len(selected) * 0.8:
        print("  Excellent work!")
    elif score >= len(selected) * 0.5:
        print("  Good effort, keep practicing!")
    else:
        print("  Better luck next time!")

    print("=" * 50)


def main():
    while True:
        play_quiz()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
