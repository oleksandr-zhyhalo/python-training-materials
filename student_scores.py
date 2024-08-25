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

def get_info_about_students_scores(students_scores: list) -> dict:
    subject_total = {}
    subject_counts = {}
    student_averages = {}
    subject_averages = {}
    top_student = ""
    bottom_student = ""
    highest_average = float(0)
    lowest_average = float(0)

    for student in students_scores:
        scores = {}
        name = student['name']
        for key, score in student.items():
            if key != 'name':
                scores[key] = score
        if scores:
            average_score = round(sum(scores.values()) / len(scores), 2)
            student_averages[name] = average_score

            if lowest_average == 0:
                lowest_average = average_score
            if average_score > highest_average:
                highest_average = average_score
                top_student = name
            if average_score < lowest_average:
                lowest_average = average_score
                bottom_student = name

            for subject, score in scores.items():
                if subject in subject_total:
                    subject_total[subject] += score
                    subject_counts[subject] += 1
                else:
                    subject_total[subject] = score
                    subject_counts[subject] = 1

    for subject in subject_total:
        subject_averages[subject] = round(subject_total[subject] / subject_counts[subject], 2)

    return {
        'Student Average Scores': student_averages,
        'Average Scores by Subject': subject_averages,
        'Best Student': top_student,
        'Worst Student': bottom_student
    }


scores_semester_1 = [
    {'name': 'Alice', 'math': 85, 'science': 92, 'english': 88},
    {'name': 'Bob', 'math': 79, 'english': 90},
    {'name': 'Charlie', 'science': 87, 'english': 85},
    {'name': 'David', 'math': 92, 'science': 89, 'english': 93},
    {'name': 'Jakob', 'math' : 32}
]

scores_semester_2 = [
    {'name': 'Alice', 'math': 56, 'science': 91, 'english': 88},
    {'name': 'Bob', 'math': 79, 'english': 67},
    {'name': 'Charlie', 'science': 87, 'english': 66},
    {'name': 'David', 'math': 81, 'science': 74, 'english': 99},
]

sem_1_info = get_info_about_students_scores(scores_semester_1)
sem_2_info = get_info_about_students_scores(scores_semester_2)

print(sem_1_info)