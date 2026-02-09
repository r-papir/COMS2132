print(" ")
print("Welcome to the GPA Calculator.")
print("Please enter all letter grades you received, one per line.")
print("Using the space bar, enter a blank line to designate the end.")
print(" ")

points= {'A+':4.33,
         'A':4.0,
         'A-':3.67,
         'B+':3.33,
         'B':3.0,
         'B-':2.67,
         'C+':2.33,
         'C':2.0,
         'C-':1.67,
         'D':1.0,
         'F':0.0}

num_courses = 0
total_points = 0
finished = False

while not finished:
    grade = input()
    if grade == " ":
        finished = True
    elif grade not in points:
        print("Error: Unknown grade '{0}' disregarded.".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses>0:
    print("Your GPA is {0:.3}".format(total_points / num_courses))
