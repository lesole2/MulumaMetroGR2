questions = [
    "Have you ever coded before? (yes/no): ",
    "Would you recommend anyone to code? (yes/no): ",
    "Do you prefer online learning? (yes/no): ",
    "Do you like Python? (yes/no): "
]

num_students = int(input("How many students will take the survey? "))

all_answers = []
overall_tally = {"yes": 0, "no": 0}  

for student in range(num_students):
    print("\nStudent", student + 1)
    answers = []
    for q in questions:
        reply = input(q).lower()
        while reply != "yes" and reply != "no":
            #
            reply = input(q).lower()

        answers.append(reply)
        overall_tally[reply] += 1
    all_answers.append(answers)
      
for i in range(len(questions)):
    question_text = questions[i]
    tally = {"yes": 0, "no": 0}
    
    for student_answers in all_answers:
        if student_answers[i] == "yes":
            tally["yes"] += 1
        else:
            tally["no"] += 1

    print(f"\n{question_text.strip()}")
    print(tally)

print("\n--- Overall Tally ---")
print(overall_tally)