import sys
from time import sleep


from questions import questions 
from questions import valid_answers

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
        typewriter("Your input is invalid. \nPlease enter a valid input. (make sure your spelling is correct)") 
        player_choice = input().lower().strip()
    
    typewriter(f'\nYou have chosen {player_choice} as your topic.')

    filtered_questions = []
    for i in questions: #filtering qns through player's topic choice
        if i["topic"].lower() == player_choice.lower():
            filtered_questions.append(i)

    return filtered_questions

def game_loop(filtered_questions):
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
        
        while answer not in valid_answers: #checking that the answer is on of the options available
            # if hint_used_this_question == True:
            #     typewriter("You cant use hints again for this question.")
            #     typewriter("Please re-enter your answer")
            #     answer = input().strip().lower()
            # elif hint_used_this_question == False:
            #     pass
            # else:
            typewriter("Your input is invalid, please re-enter your answer.")
            typewriter("remember to spell your answer correctly")
            answer = input().strip().lower()

        # hint_used_this_question = False
        
        if answer == 'a' or answer  == '1':
            pick1234 = 1
        elif answer == 'b' or answer == '2':
            pick1234 = 2
        elif answer == 'c' or answer == '3':
            pick1234 = 3
        elif answer == 'd' or answer == '4':
            pick1234 = 4
        
        correct_answer = x["Correct Ans"]
# #FOR WHEN I RETURN TO THIS CODE I AM MAKEING IT SO THAT THE USER CANT ASK FOR A HINT TWICE IN THE SAME QUESTION#####################################################################
#         #HINTS
#         if answer == "hint":
#             if hints == 0:
#                 typewriter("Sadly you have no hints left.")
#                 typewriter("I appologise but you have no hints left.")
#             else:
#                 typewriter("Here is your hint,")
#                 typewriter(x["hint"])
#                 hints -= 1
#                 if hints == 0:
#                     typewriter("You have no hints left.")
#                 else:
#                     typewriter(f"remember though, you have {hints} hints left.")
#         typewriter("Please re-enter your answer")
#         hint_used_this_question = True
#         answer = input().strip().lower()
#

        

        if pick1234 == correct_answer:  # Ensure both are case-insensitive and trimmed
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