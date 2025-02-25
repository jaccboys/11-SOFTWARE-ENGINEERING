def main():
    scores = []
    collect_scores(scores) # First funciton to run
    average = calculate_scores(scores)
    grade = determine_grade(average)
    display_results(grade)


def collect_scores(scores):
    for i in range(3):
        score = int(input("Enter score: "))
        scores.append(score)
        return scores #(return) doesnt delete the values, 
                      #it stores it deep down to be brought back later

def calculate_scores(scores):
    average = average(scores)
    return average

def determine_grade(average):
    if average >= 90:
        grade = "Band 6"
    elif average >= 80:
        grade = "Band 5"
    elif average >= 70:
        grade = 'Band 4'
    else:
        grade = 'Fail'
    display_you_suck()
    return grade

def display_results(average, grade):
    print(f"Average: {average}, Grade: {grade}")

def display_you_suck():
    print('You suck')