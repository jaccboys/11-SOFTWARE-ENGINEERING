import sys
from time import sleep
from questions import questions 

def typewriter(words): #function to print out text in a typewriter fashion
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in ':.!, ?><':
            sleep(0.03)
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
    typewriter("Enter your chosen topic from the following:\n\nRetro Gaming | Kendrick Lamar | Aphex Twin") 
    
    player_choice = input().lower().strip()
    
    while player_choice not in ['retro gaming', 'kendrick lamar', 'aphex twin']: #checking if the input is one of the topics available
        typewriter("Your input is invalid. \nPlease enter a valid input. (make sure your spelling is correct)") 
        player_choice = input().lower().strip()
    
    typewriter(f'\nYou have chosen {player_choice} as your topic.')

    filtered_questions = []
    for i in questions: #filtering qns through player's topic choice
        if i["topic"].lower() == player_choice.lower():
            filtered_questions.append(i)

    return filtered_questions

def game_loop(filtered_questions):
    valid_answers = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D', '1', '2', '3', '4', 'hint', 'HINT'] #valid answers for the quiz
    score = 0
    hints = 3
    typewriter('please answer the question by entering the letter of the correct answer or the letter that corresponds to the correct answer')
    typewriter("If your having trouble, remember you can ask for a hint by typing 'hint'")
    typewriter("Beware, you only have 3")
    typewriter('Good luck!')

    for x in filtered_questions: 

        typewriter(x["qns"])
        typewriter(" | ".join(x['options']))
        typewriter("Enter your answer below:")
        answer = input().lower().strip()
        
        while answer not in valid_answers:#checking that the answer is on of the options available
            typewriter("Your input is invalid, please re-enter your answer.")
            typewriter("remember to spell your answer correctly")
            answer = input().strip().lower()

        #FOR WHEN I RETURN TO THIS CODE I AM MAKEING IT SO THAT THE USER CANT ASK FOR A HINT TWICE IN THE SAME QUESTION#####################################################################
        #HINTS
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
                    typewriter(f"remember, you have {hints} hints left.")
                    typewriter("Use them carefully.")
                typewriter("Please re-enter your answer")
                answer = input().strip().lower()     
        
        if answer == 'a' or answer  == '1': #converting answer to a number to use in the dictionary
            pick1234 = 1
        elif answer == 'b' or answer == '2':
            pick1234 = 2
        elif answer == 'c' or answer == '3':
            pick1234 = 3
        elif answer == 'd' or answer == '4':
            pick1234 = 4
        elif answer == 'hint' and hints != 0:
            typewriter("You silly billy, WRONG!")
            pick1234 = 'hint'

        correct_answer = x["Correct Ans"] #getting the correct answer from the dictionary

        if pick1234 == correct_answer:  # Ensure both are case-insensitive and trimmed
            typewriter("\nCorrect!")
            score += 1 #incrementing score by 1 when answer is correct
        elif pick1234 != correct_answer and answer != 'hint':
            typewriter("\nWrong!")
            typewriter(f"The correct answer is {x['options'][correct_answer - 1]}") #displaying the correct answer when the player gets it wrong
    return score

def end_game(score, filtered_questions):
    typewriter(f"Your score is {score} out of {len(filtered_questions)} questions.")
    typewriter("Would you like to play again? (y/n)")
    play_again = input().lower().strip()
    if play_again == 'y':
        main_without_welcome_page(questions)
    else:
        typewriter("\nThank you for playing!")
        typewriter("Hope you had fun!")
        

def main(questions): #main function
    #welcome() #remeber to remove the comment to enable the welcome message
    filtered_questions = filter_by_topic(questions)
    score = game_loop(filtered_questions)
    end_game(score, filtered_questions)

def main_without_welcome_page(questions): #main function but doesnt include the welcome message for a player that wants to play the game multiple times
    filtered_questions = filter_by_topic(questions)
    score = game_loop(filtered_questions)
    end_game(score, filtered_questions)

main(questions)