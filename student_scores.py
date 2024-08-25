"""
1. Calculate the average of each student
2. Find a student with the highest average
3. Return student dict in following format:
4.
{
    "Student_name" : "average"
    ...
    "top_student" : name
}
"""
from tkinter.font import names

students_scores = [
    {'name': 'Alice', 'math': 85, 'science': 92, 'english': 88, 'physics' : 83},
    {'name': 'Bob', 'math': 79, 'science': 85, 'english': 90},
    {'name': 'Charlie', 'math': 92, 'science': 87, 'english': 85}
]

averages = {}
top_student = ""
highest_average = 0

for student in students_scores:
    scores = []
    name = student['name']
    for key, score in student.items():
        if key != 'name':
            scores.append(score)
    average_score = round(sum(scores)/len(scores), 2)
    averages[name] = average_score

    if average_score > highest_average:
        highest_average = average_score
        top_student = name

averages['top_student'] = top_student

print(averages)

