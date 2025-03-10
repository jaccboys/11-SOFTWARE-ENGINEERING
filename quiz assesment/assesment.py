import sys
from time import sleep

from questions import questions

def typewriter(words):
    for char in words:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in '.!f, ':
            sleep(0.05)
    sys.stdout.write("\n\n")

def print_questions(questions):
    typewriter("The questions are: ")
    i = 0
    for qns in questions:
        typewriter(f"{questions[i]["qns"]}")
        i+=1

#print_questions(questions):
#    typewriter("The questions are: ")
#    i = 0
#    for qns in questions:
#        typewriter(f"{questions[i]["qns"]}")
#        i+=1

def main():
    print_questions(questions)

main()