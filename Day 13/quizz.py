import random 
score=0
questions = [
    {"question": "What is the capital of France?", "options": ["A) Paris", "B) London", "C) Rome", "D) Madrid"], "answer": "A"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"], "answer": "B"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway", "D) Mark Twain"], "answer": "A"},
    {"question": "What is the chemical symbol for gold?", "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"], "answer": "A"},
    {"question": "What is the largest mammal in the world?", "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"], "answer": "B"},
    {"question": "Which element has the atomic number 1?", "options": ["A) Helium", "B) Oxygen", "C) Hydrogen", "D) Carbon"], "answer": "C"},
    {"question": "What year did the Titanic sink?", "options": ["A) 1912", "B) 1915", "C) 1905", "D) 1920"], "answer": "A"},
    {"question": "Who painted the Mona Lisa?", "options": ["A) Vincent Van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"], "answer": "C"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["A) Gold", "B) Diamond", "C) Platinum", "D) Iron"], "answer": "B"},
    {"question": "In which country would you find the Great Wall?", "options": ["A) Japan", "B) China", "C) India", "D) Korea"], "answer": "B"},
    {"question": "What is the smallest unit of life?", "options": ["A) Organism", "B) Tissue", "C) Cell", "D) Atom"], "answer": "C"},
    {"question": "Which famous scientist developed the theory of relativity?", "options": ["A) Isaac Newton", "B) Albert Einstein", "C) Nikola Tesla", "D) Galileo Galilei"], "answer": "B"},
    {"question": "What is the capital of Japan?", "options": ["A) Tokyo", "B) Seoul", "C) Beijing", "D) Bangkok"], "answer": "A"},
    {"question": "What is the largest ocean on Earth?", "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"], "answer": "D"},
    {"question": "Which language is primarily spoken in Brazil?", "options": ["A) Spanish", "B) Portuguese", "C) English", "D) French"], "answer": "B"},
    {"question": "What is the name of the galaxy that contains our Solar System?", "options": ["A) Andromeda Galaxy", "B) Milky Way Galaxy", "C) Triangulum Galaxy", "D) Messier 87"], "answer": "B"},
    {"question": "Who is known as the father of modern physics?", "options": ["A) Galileo Galilei", "B) Isaac Newton", "C) Albert Einstein", "D) Richard Feynman"], "answer": "B"},
    {"question": "What is the largest desert in the world?", "options": ["A) Sahara Desert", "B) Arabian Desert", "C) Gobi Desert", "D) Antarctic Desert"], "answer": "D"},
    {"question": "What is the main ingredient in guacamole?", "options": ["A) Tomato", "B) Avocado", "C) Onion", "D) Pepper"], "answer": "B"},
    {"question": "What is the boiling point of water in Celsius?", "options": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"], "answer": "B"}
]


print("WElcome to the quizz game!!!!")
print("10 questions will be asked \nChoose the correct option \nLets start")

selected_ques=random.sample(questions,10)
for index,i in enumerate(selected_ques,start=1):
    print(f"{index}.{i['question']}")
    for option in i['options']:
        print(f"{option}")
    user_ans=input("Enter the correct option: ").strip().upper()
    if user_ans==i['answer']:
        print("Correct answer")
        score+=1
    else:
        print(f"The correct answer was {i['answer']}")

print(f"You have succesfully completed your game \nYou have {score} correct answers.")
        
                                          