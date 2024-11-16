
questions = [
    {
        "prompt": "How man dots appear on a pair of dice?",
        "options": ["A. 42", "B. 6", "C. 40", "D. 36"],
        "answer": "A"
        },
    {
        "prompt": "Which day of the week does the jewish sabbath begin?",
        "options": ["A. Monday", "B. Sunday", "C. Saturday", "D. Friday"],
        "answer": "D"
        },
    {
        "prompt": "In which country would yyou find Mount Kilimanjaro?",
        "options": ["A. Sudan", "B. Sahara desert", "C. Tanzania", "D. Zimbabwe"],
        "answer": "C"
        },
    {
        "prompt": "What are the colours on the Nigerian Flag?",
        "options": ["A. Green, White", "B. Blue, White", "C. Yellow, Black, Red", "D. Red, Blue"],
        "answer": "A"
        },
    {
        "prompt": "Who discovered the earth revolves around the sun?",
        "options": ["A. Napoleon Bonaparte", "B. Nicolas Copernicus", "C. Nathaniel Bassey", "D. Nicholas Venus"],
        "answer": "B"
        },
    {
        "prompt": "What is the process by which plants convert sunlight to energy?",
        "options": ["A. Photosynthesis", "B. Sublimation", "C. Evaporation", "D. Chemosynthesis"],
        "answer": "A"
        },
    {
        "prompt": "Where is the srongest human muscle located?",
        "options": ["A. Thighs", "B. Arms", "C. Jaw", "D. Fists"],
        "answer": "C"
        }
    ]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer=input("Enter an answer from the options  (A, B, C, or D): ")
        if answer == question["answer"]:
            print("Correct, good job!\n")
            score += 1
        else:
            print("Wrong, better luck next time. Correct answer is:", question["answer"],"\n")

    print("You got", {score}, "out of", {len(questions)}, "questions correct.")

run_quiz(questions)

echo "# python-projects" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:Steph100005/python-projects.git
git push -u origin main
