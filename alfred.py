questions = [
    "Have you ever coded before? (yes/no): ",
    "Would you recommend anyone to code? (yes/no): ",
    "Do you prefer online learning? (yes/no): ",
    "Do you like Python? (yes/no): "
]


num_students = int(input("How many students will take the survey? "))


all_answers = []


for student in range(num_students):
    print("\nStudent", student + 1)
    answers = []  
    for q in questions:
        reply = input(q).lower()
        while reply != "yes" and reply != "no":
            print("Kindly answer with 'yes' or 'no'.")
            reply = input(q).lower()
        answers.append(reply)
    all_answers.append(answers)


for i in range(len(questions)):
    yes_count = 0
    no_count = 0
    for student_answers in all_answers:
        if student_answers[i] == "yes":
            yes_count += 1
        else:
            no_count += 1

    print("\n" + questions[i])
    print("Yes:", yes_count)
    print("No:", no_count)
