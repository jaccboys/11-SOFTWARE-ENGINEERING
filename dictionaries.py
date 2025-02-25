#Array

#results = [99,60,30,40,50]
#students = ['Cruz','Harry','Ben','Briscoe','Zac']
#print(f"{students[0]}) recieve a score of {results[0]}")
 

#results = {'Name': 'Cruz', 'English': 5, 'Maths': 85}
#print(result{'Name'})
#print(f"[result['English'] , {result['Maths']}")

#Dictionary
results = [
    {"Name": "Cruz", "English": 5 , 'Maths': 85},
    {"Name": "Nathan", "English": 66 , 'Maths': 80},
    {"Name": "Hanz", "English": 99 , 'Maths': 99},
    {"Name": "Tom", "English": -50 , 'Maths': 100},
    {"Name": "Ben", "English": 0 , 'Maths': 100},    
]

for result in results:
    print(f"{result['Name']}'s grades are {result['English']} and {result['Maths']}")

total=0
for result in results:
    total+= result["Maths"]
avg = total / len(result) # how many rows ther are
print(f'{avg:.2f}')