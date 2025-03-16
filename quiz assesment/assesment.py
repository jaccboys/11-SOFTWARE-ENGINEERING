import sys
from time import sleep


from questions import questions 

def typewriter(words): #function to print out text in a typewriter fashion
    for char in words:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in ':.!, ?><':
            sleep(0.06)
    sys.stdout.write("\n\n")

def welcome(): #function to print out the welcome message
    typewriter("Welcome to my quiz game!")
    typewriter("You will be asked a series of extreamly difficult questions.")
    typewriter("You must answer them correctly to win.")
    typewriter("Good luck!")
    typewriter("First things first, please enter you name: \n")
    name = input('>>  ').upper().strip()
    print('WELCONE', name, 'TO MY QUIZ')


def filter_by_topic(questions): #function to filter the questions based on the player's choice
    typewriter('What topic would you like to be quizzed on?')
    typewriter("Enter your chosen topic from the following:\n Ninjago | Star wars") 
    
    player_choice = input().lower().strip()
    
    print('testing', player_choice) #testing
    #VERIFICATION FOR ANSWER
    
    while player_choice != 'ninjago' and player_choice != 'star wars':
        typewriter("Your input is invalid. \n please enter a valid input. (make sure your spelling is correct)") 
        player_choice = input().lower().strip()
    
    typewriter('You have chosen ' + player_choice + ' as your topic.')

    filtered_questions = []
    for i in questions:
        if i["topic"].lower() == player_choice.lower():
            filtered_questions.append(i)

    return filtered_questions


def game_loop(filtered_questions):
    score = 0
    typewriter("**Remember to spell your answers correctly please.**")
    typewriter('please type out one of each answer from the options given')
    for x in filtered_questions: 
        typewriter(x["qns"])
        typewriter(", ".join(x['options']))
        typewriter("Enter your answer below:")
        answer = input()
        if answer.lower() == x["Correct Ans"]: #check if the answer is correct
            typewriter("\nCorrect!") #print correct if the answer is correct
            score += 1 #increment the score by 1
        else:
            typewriter("\nWrong!")
    return score

def end_game(score, filtered_questions):
    typewriter(f"Your score is {score} out of {len(filtered_questions)} questions.")
    typewriter("Thank you for playing!")
    typewriter("Hope you had fun!")
    


def main(questions, score=0):
    #welcome()
    filtered_questions = filter_by_topic(questions)
    game_loop(filtered_questions)
    end_game(score, filtered_questions)
    
main(questions)