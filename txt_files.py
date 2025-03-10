# Open and read the text file
with open("files/students.txt", "r") as file:
    #      ^^^^^^^^^^^^^^^^^^ sets the parameter as the file chosen
    # the 'r' means READ ONLY (security measure)(ensures the file cannot be changed by this code)
    # for instance if you use another thing like 'w' write.

    for line in file:
        print(line)

        name, secret_word = line.strip().split(", ")
        print(f"Name: {name}, Silly Word: {secret_word}")
        print('hello')