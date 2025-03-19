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
    typewriter("Enter your chosen topic from the following:\n\n Ninjago | Star wars") 
    
    player_choice = input().lower().strip()
    
    while player_choice not in ['ninjago', 'star wars']: #checking if the input is one of the topics available
        typewriter("Your input is invalid. \n please enter a valid input. (make sure your spelling is correct)") 
        player_choice = input().lower().strip()
    
    typewriter(f'\nYou have chosen {player_choice} as your topic.')

    filtered_questions = []
    for i in questions: #filtering qns through player's topic choice
        if i["topic"].lower() == player_choice.lower():
            filtered_questions.append(i)

    return filtered_questions

def game_loop(filtered_questions):
    score = 0
    typewriter("**Remember to spell your answers correctly please.**")
    typewriter('please type out one of each answer from the options given')
    typewriter("If your having trouble, remember you can ask for a hint by typing 'hint'")
    typewriter("Beware, you only have 3")
    typewriter('Good luck!')

    for x in filtered_questions: 
        typewriter(x["qns"])
        typewriter(" | ".join(x['options']))
        typewriter("Enter your answer below:")
        answer = input().strip().lower()
        correct_answer = x["Correct Ans"].strip().lower()

        #HINTS
        hints = 3
        if answer == "hint":
            if hints == 0:
                typewriter("Sadly you have no hints left.")
                typewriter("I appologise but you have no hints left.")
            else:
                typewriter("Here is your hint,")
                typewriter(x["hint"])
                hints -= 1
                if hints == 0:
                    typewriter("You have no hints left.")
                else:
                    typewriter(f"remember though, you have {hints} hints left.")
        typewriter("Please re-enter your answer")
        answer = input().strip().lower()


        correct_answer = x["Correct Ans"].strip().lower()
        valid_answers = [option.strip().lower() for option in x['options']] #creating a seperate list of options that are lowercased and no trailing spaces
        while answer not in valid_answers: #checking that the answer is on of the options available
            typewriter("you input is invalid, please re-enter your answer")
            typewriter("remember to spell your answer correctly")
            answer = input().strip().lower()

        if answer == correct_answer:  # Ensure both are case-insensitive and trimmed
            typewriter("\nCorrect!")
            score += 1 #incrementing score by 1 when answer is correct
        else:
            typewriter("\nWrong!")
            typewriter(f"The correct answer is {x['Correct Ans']}")

    return score

def end_game(score, filtered_questions):
    typewriter(f"Your score is {score} out of {len(filtered_questions)} questions.")
    typewriter("Thank you for playing!")
    typewriter("Hope you had fun!")
    

def main(questions): #main function
    #welcome()
    filtered_questions = filter_by_topic(questions)
    score = game_loop(filtered_questions)
    end_game(score, filtered_questions)

main(questions)