quiz_data = [
    {
        "question": "Who sung the song Bad guy? ",
        "options": ["Olivia Rodrigo", "Billie Eilish", "Taylor Swift"],
        "answer": "Billie Eilish"
    },
    {
        "question": "Who sung the song Good 4 You? ",
        "options": ["Louis Armstrong", "Ella Fitzerald", "Olivia Rodrigo"],
        "answer": "Olivia Rodrigo"
    },
    {
        "question": "Who sung the song Without You? ",
        "options": ["The Kid Laroi", "Twenty One Pilots", "Billie Eilish"],
        "answer": "The Kid Laroi"
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