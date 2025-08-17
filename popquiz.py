quiz_data = [
    {
        "question": "Who sung the song Bad guy? ",
        "options": ["a.Olivia Rodrigo", "b.Billie Eilish", "c.Taylor Swift"],
        "answer": "b"
    },
    {
        "question": "Who sung the song Good 4 You? ",
        "options": ["a.Louis Armstrong", "b.Ella Fitzerald", "c.Olivia Rodrigo"],
        "answer": "c"
    },
    {
        "question": "Who sung the song Without You? ",
        "options": ["a.The Kid Laroi", "b.Twenty One Pilots", "c.Billie Eilish"],
        "answer": "a"
    }
]
score = 0
for question_data in quiz_data:
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)

        user_answer = input("Enter your answer: ")

        if user_answer == question_data["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question_data['answer']}.")
        print("-" * 20) 
    
        print(f"You scored {score} out of {len(quiz_data)}.")