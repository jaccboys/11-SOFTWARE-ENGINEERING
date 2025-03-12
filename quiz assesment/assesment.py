import sys
from time import sleep


from questions import questions 

def typewriter(words): #function to print out text in a typewriter fashion
    for char in words:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in ':.!f, ':
            sleep(0.06)
    sys.stdout.write("\n\n")

def welcome(): #function to print out the welcome message
    typewriter("WELCOME TO THE QUIZ GAME.")
    typewriter("You will be asked a series of extreamly difficult questions.")
    typewriter("You must answer them correctly to win.")
    typewriter("Good luck!")
    typewriter("First things first, please enter you name: \n")
    name = input('>>  ').upper().strip()
    print('WELCONE', name, 'TO MY QUIZ')

def print_questions(questions): #function to print out the questions
    pass
    #typewriter("The questions are: ")
    #for i in questions:
    #    typewriter(f"{questions[i]["qns"]}")

def filter_by_topic(questions): #function to filter the questions based on the player's choice
    typewriter('What topic would you like to be quizzed on?')
    typewriter("Enter your chosen topic from the following: \n Ninjago | Star wars") 
    player_choice = input().lower().strip()
    print('testing', player_choice) #testing
    #VERIFICATION FOR ANSWER
    if player_choice != 'ninjago' and player_choice != 'star wars':
        typewriter("Your input is invalid. \n please enter a valid input. (make sure your spelling is correct)") 
        player_choice = input().lower().strip()

    filtered_questions = []
    for i in questions:
        if i["topic"] == player_choice:
            filtered_questions.append(i)
    print('testing', filtered_questions) #TESTING
    return filtered_questions

#def answer_qn(filtered_question):
    #typewriter("Enter your answer: ")
    #chosen_anser = input().lower().strip()

def game_loop(filtered_questions):
    score = 0
    for x in filtered_questions:
        typewriter(x["qns"])
        typewriter("Enter your answer: ")
        answer = input().lower().strip()
        if answer == x["Correct Ans"]:
            typewriter("Correct!")
            score += 1
        else:
            typewriter("Wrong!")
    return score

def main(questions):
    welcome()
    filter_by_topic(questions)
    filtered_questions = filter_by_topic(questions)
    
main(questions)