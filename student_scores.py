"""
1. Calculate the average of each student
2. Find a student with the highest average
3. Return student dict in following format:
4. New dict with student avg score, considering only subjects they have
5. A list of a class-wise averages, avg score of a subject for all students
3. student with lowers avg score
{
    "averages" {
        "student_name" : "average"
        ...
    },
    "subject_averages" : {
        "subject" : "average"
        ...
    }
    "top_student" : name
    "bottom_student" : name
}
"""

students_scores = [
    {'name': 'Alice', 'math': 85, 'science': 92, 'english': 88},
    {'name': 'Bob', 'math': 79, 'english': 90},
    {'name': 'Charlie', 'science': 87, 'english': 85},
    {'name': 'David', 'math': 92, 'science': 89, 'english': 93},
    {'name' : 'Jakob'}
]

subject_total = {}
subject_counts = {}
student_averages = {}
subject_averages = {}
top_student = ""
bottom_student = ""
highest_average = float(0)
lowest_average = float(0)

for student in students_scores:
    print(f"Student working on: {student}")
    scores = {}
    name = student['name']
    print(f"Student name working on is: {name}")
    print(f"{name} student items is {student.items()}")
    for key, score in student.items(): # Iteration over  dict_items([('name', 'Alice'), ('math', 85), ('science', 92), ('english', 88)])
        if key != 'name':
            scores[key] = score
    print(f"Scores for student {name} are {scores}")
    if scores:
        # scores are {'math': 85, 'science': 92, 'english': 88}
        average_score = round(sum(scores.values()) / len(scores), 2)
        print(f"Avarage score for {name} is {average_score}")
        student_averages[name] = average_score
        print(f"Student averages currently looks like: {student_averages}")

        if lowest_average == 0:
            lowest_average = average_score
            print(f"Doing initialization for lowest_average")
        if average_score > highest_average:
            highest_average = average_score
            top_student = name
            print(f"Student's {name} average score of {average_score} is bigger then current highest")
        if average_score < lowest_average:
            lowest_average = average_score
            bottom_student = name
            print(f"Student's {name} average score of {average_score} is lower then current lower")

        print(f"Currently scores looks like: {scores}")
        for subject, score in scores.items():
            print(f"Student: {name}, Subject: {subject}, Score: {score}")
            if subject in subject_total:
                subject_total[subject] += score
                subject_counts[subject] += 1
            else:
                subject_total[subject] = score
                subject_counts[subject] = 1
            print(f"subjects_total now is: {subject_total}")
            print(f"subject_count now is: {subject_counts}")

        print('------' * 10)
for subject in subject_total:
    subject_averages[subject] = round(subject_total[subject] / subject_counts[subject], 2)

final_dict = {
    'averages': student_averages,
    'subject_averages': subject_averages,
    'top_student': top_student,
    'bottom_student': bottom_student
}

print(final_dict)
