import csv

# Open and read the CSV file
with open("students.csv", newline="") as file:
    reader = csv.reader(file)
    # next(reader)  # Skip the header row
    for row in reader:
        name, silly_word = row
        print(f"Name: {name}, Silly Word: {silly_word}")