import sys
"""
The plant employs 3 mechanics, each working 8 hours a day.
The user specifies the number of cars to be serviced, then for each car he gives the number of hours needed to complete the mechanic's work.
We assign individual services to mechanics by selecting the mechanic with the lowest number of working hours at the moment.
If the number is the same, we choose the mechanic with the lower number. Working hours cannot be divided into mechanics.
The program should return the number of days needed to dismiss any mechanic and the number of days needed for all mechanics to complete the jobs
"""
car_count = int(input())
workload1 = 0
workload2 = 0
workload3 = 0

def select_mechanic(job_hours, workload1, workload2, workload3):
    if workload3 < workload1 and workload3 < workload2:
        workload3 += job_hours
        print("Mechanic 3 will do take the job.")
    elif workload2 < workload1:
        workload2 += job_hours
        print("Mechanic 2 will do take the job.")
    else:
        workload1 += job_hours
        print("Mechanic 1 will do take the job.")
    return workload1, workload2, workload3


for car in range(car_count):
    while True:
        print("Enter a number of working hours for the car: ")
        job_hours = int(input())
        if job_hours <= 0:
            print("Error: Invalid number of hours")
        else:
            break
    workload1, workload2, workload3 = select_mechanic(job_hours, workload1, workload2, workload3)

print(f"The nearest mechanic will be free within {int((min(workload1, workload2, workload3) + 7)/8)} days")
print(f"All mechanics will be free within {int((max(workload1, workload2, workload3) + 7)/8)} days")

# Works on car 8 hours = 1 day.
# Work on car 9 hours = Number of work on car / number of working hours = 9/8 = 1.125 = 2 days
# int((work + 7)/8). 1 + 7 / 8 = day
# min, max.