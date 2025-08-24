UserName =input("Enter your Name: ")
QuizData = [
    {
        "question": "Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? ",
        "options": ["a.Delete the message and try to forget about it", "b.Keep the text and show an adult you trust", "c.Text the person back saying something mean to them"],
        "answer": "b"
    },
    {
        "question": "You find out that someone has posted an embarrassing picture of you online. What should you do? ",
        "options": ["a.Tweet that they are an idiot and a loser", "b.Ask your friends to give the person a hard time", "c.Tell an adult you trust "],
        "answer": "c"
    },
    {
        "question": "You want to join an online gaming site. Which of the following information is okay for you to post on the site. ",
        "options": ["a.A nickname", "b.Your name", "c.Your email address"],
        "answer": "a"
    },
    {
        "question": "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment? ",
        "options": ["a.Your video is rubbish!", "b.Man, this is awful! Stick to playing sport or something.", "c.Congrats on your first video! Let me know if you’d like any help editing for your next video."],
        "answer": "c"
    },
    {
        "question": "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply? ",
        "options": ["a.“We shouldn’t be mean to them just because they’re mean to us.”", "b.“Yeah, totally. They’re evil and deserve it!”", "c.“Yes, I think that is a great idea. Maybe they will understand what it feels like, and stop bullying us!”"],
        "answer": "c"
    }
]
score = 0
for QuestData in QuizData:
        print(QuestData["question"])
        for option in QuestData["options"]:
            print(option)

        UserAns = input("Enter your answer: ")

        if UserAns == QuestData["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {QuestData['answer']}.")
        print("-" * 20) 
    
        print(f"You scored {score} out of {len(QuizData)}. Well done " + (UserName))