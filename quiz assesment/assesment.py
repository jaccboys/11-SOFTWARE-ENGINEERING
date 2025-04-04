import sys
from time import sleep
from questions import questions 
import random

def typewriter(words, colour_code=""): #function to print out text in a typewriter fashion
    if colour_code:
        words = f"{colour_code}{words}\033[0m" #adding colour code to the text
    for char in words:
        sleep(0.01) #0.02 #time delay between each character
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in ':.|!, ?><\n': #increased time delay between punctuation
            sleep(0.01) #0.04
    sys.stdout.write("\n\n")

def welcome(): #function to print out the welcome message
    typewriter("Welcome to my quiz game!")
    typewriter("You will be asked a series of extreamly difficult questions.")
    typewriter("You must answer them correctly to win.")
    typewriter("Good luck!")
    typewriter("First things first, please enter you name: \n")
    name = input('>>  ').upper().strip()
    if name is None or name == "":
        name = "Player 1"
    typewriter('\n')
    typewriter(f"\033[46;30m{'-' * 53 + '-' * (2 * len(name) + 1)}\033[0m")
    typewriter(f"\033[46;30m----- W E L C O M E   T O   T H E   Q U I Z   {' '.join(name).upper()}! -------\033[0m")
    typewriter(f"\033[46;30m{'-' * 53 + '-' * (2 * len(name) + 1)}\033[0m")
    return name

def filter_by_topic(questions): #function to filter the questions based on the player's choice
    typewriter('\n\nWhat topic would you like to be quizzed on?')
    typewriter("Enter your chosen topic from the following:\n\nArt history | Music and Bands | Batman: Arkham") 
    
    topic_choice = input().lower().strip()
    
    while topic_choice not in ['art history', 'music and bands', 'batman: arkham']: #checking if the input is one of the topics available
        typewriter("\nYour input is invalid. \nPlease enter a valid input. (make sure your spelling is correct)") 
        topic_choice = input().lower().strip()
    
    typewriter(f'\nYou have chosen {topic_choice.upper()} as your topic.')

    filtered_questions = []
    for i in questions: #filtering qns through player's topic choice
        if i["topic"].lower() == topic_choice.lower():
            filtered_questions.append(i)
    return filtered_questions

def game_loop(filtered_questions):
    valid_answers = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D', '1', '2', '3', '4', 'hint', 'HINT'] #valid answers for the quiz
    score = 0
    hints = 3
    typewriter("please enter your answers in the following format:")
    typewriter("a, b, c, d, 1, 2, 3, or 4")
    typewriter("If your having trouble, remember you can ask for a hint by typing 'hint'")
    typewriter("Beware, you only have 3")
    typewriter('Good luck!')

    random.shuffle(filtered_questions) #Randomising the questions

    for x in filtered_questions:  #looping through the questions
        typewriter(x["qns"], colour_code="\033[46;30m") #adding colour code to the question
        typewriter(" | ".join(x['options']))
        typewriter("Enter your answer below:")
        answer = input().lower().strip()
        
        while answer not in valid_answers:#checking that the answer is on of the options available
            typewriter("\nYour input is invalid, please re-enter your answer.")
            typewriter("remember to spell your answer correctly")
            answer = input().strip().lower()

        if answer == "hint": #checking if the player has asked for a hint
            if hints == 0:
                typewriter("Sadly you have no hints left.")
                typewriter("Please re-enter your answer")
                answer = input().strip().lower()
                while answer not in valid_answers:
                    typewriter("\nYour input is invalid, please re-enter your answer.")
                    typewriter("remember to spell your answer correctly")
                    answer = input().strip().lower()
            else:
                typewriter("\nHere is your hint,")
                typewriter(x["hint"])
                hints -= 1
                if hints == 0:
                    typewriter("You have no hints left.")
                else:
                    typewriter(f"remember, you have {hints} hints left.")
                    typewriter("Use them carefully.")
                typewriter("Please re-enter your answer")
                answer = input().strip().lower()
                while answer not in valid_answers:
                    typewriter("\nYour input is invalid, please re-enter your answer.")
                    typewriter("remember to spell your answer correctly")
                    answer = input().strip().lower()
        
        correct_answer = x["Correct Ans"] #getting the correct answer from the dictionary
        
        if answer == 'a' or answer  == '1': #converting answer to a number to use in the dictionary
            pick1234 = 1
        elif answer == 'b' or answer == '2':
            pick1234 = 2
        elif answer == 'c' or answer == '3':
            pick1234 = 3
        elif answer == 'd' or answer == '4':
            pick1234 = 4
        elif answer == 'hint':
            typewriter("\nYou silly billy, WRONG!")
            typewriter(f"The correct answer is {x['options'][correct_answer - 1]}")
            typewriter("You have no hints left.")
            pick1234 = 'hint'

        if pick1234 == correct_answer: # Ensure both are case-insensitive and trimmed
            typewriter("\nCorrect!")
            score += 1 #incrementing score by 1 when answer is correct
        elif pick1234 != correct_answer and answer != 'hint':
            typewriter("\nWrong!")
            typewriter(f"The correct answer is {x['options'][correct_answer - 1]}") #displaying the correct answer when the player gets it wrong
    return score, hints

def end_game(score, filtered_questions, name, hints, questions): #function to display the end game message
    typewriter(f"Your score is {score} out of {len(filtered_questions)} questions.")
    typewriter(f"Thats {score/len(filtered_questions) * 100:.2f}%!")
    typewriter(f"You used {3 - hints} hint(s) throughout the quiz.")
    typewriter("Would you like to play again? (y/n)")
    play_again = input().lower().strip()
    while play_again not in ['y', 'n', 'yes', 'no']: #checking if the input is valid
        typewriter("Invalid input.")
        typewriter("Re-enter")
        play_again = input().lower().strip()
    if play_again in ['y', 'yes']:
        main(questions)  # Ensure questions is passed correctly
    elif play_again in ['n', 'no']:
        typewriter(f"\nThank you for playing {name}!")  # Correctly format name
        typewriter("Hope to see you soon!")  # Add proper punctuation        
            
def main(questions): # main function to run the game
    name = welcome()
    filtered_questions = filter_by_topic(questions)
    score, hints = game_loop(filtered_questions)  # Capture both score and hints
    end_game(score, filtered_questions, name, hints, questions)  # Pass hints to end_game

main(questions)