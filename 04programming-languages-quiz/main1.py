"""
What to do:
1. Read the initial comment and delete it.  Run the code again.
2. welcome_message is a multiline string.  Change it to a string "Welcome!".
3. Learn the data type `dictionaries`.
    Replace questions_and_answers by QandA.
4. Put `print(QandA.items())` after the for-loop.
5. Learn the for-loop including the if-else structure.
6. Learn the if-elif-else structure.
7. Change `==` to `>=` in the elif line.
8. Change the comments to Japanese.
"""



welcome_message = "クイズの世界にようこそ!"
QandA = {"質問１の答えは？":"A1", "質問２の答えは？":"A2", "質問３の答えは？":"A3"}
questions_and_answers = {
    "What programming language took 10 days to develop? ": "JavaScript",
    "What programming language is named after a popular British comedy troupe? ": "Python",
    "What is the primary programming language for writing Roblox games? ": "Lua",
    "What programming language is Minecraft written in? ": "Java",
    "What programming language is primarily used for writing game engines? ": "C++",
    "What is the native programming language in web browsers? ": "JavaScript",
    "What programming language is the foundation of most operating systems? ": "C",
    "What programming language has new version releases every year on Christmas day? ": "Ruby",
}

correct_answers = 0
#num_questions = len(questions_and_answers)
num_questions = len(QandA)
print("len=",num_questions)
print(welcome_message)


for question, answer in QandA.items():
    print(QandA.items())
    user_guess = input(question)
    if user_guess == answer:
        print("そのとおりでございます。")
        correct_answers += 1
    else:
        print("残念ながら、それは違います...")

    print(f"正答数は、 {correct_answers} でした。")


if correct_answers == num_questions:
    print("おめでとうございます、すべてが正解です。")
elif correct_answers >= num_questions - 2:
    print("その調子です、いくつか間違えただけです。")
else:
    print("もっと時間をかけて勉強すべきです。")
