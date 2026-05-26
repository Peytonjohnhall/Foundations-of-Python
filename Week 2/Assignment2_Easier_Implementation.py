"""
@Author: Peyton John Hall
A Python program that stores percentages in a list of scores, then performes
calculations; viz. it finds the mu, top score, bottom score, total above 
average (exclusive), and finds and removes the bottom two scores from the list.
"""

"""
This is the easier implementation because it uses slicing.
"""

"""
Began typing this program after finishing Assignment2.py implementation.
Began typing program: 02/18/2026 at 9:46p.m.
"""

score = []
print("Enter exam scores one at a time. Once you are done, enter \"-1\"")
while True:
    percentage = float(input())

    if percentage == -1:
        break
    elif 0 <= percentage <= 100:
        score.append(percentage) # append, viz. add
    else:
        print("Invalid input.")
print("Scores entered:", "\n", score)

# find average
average = sum(score) / len(score)
average = round(average, 2) # round to two decimal points
print("Average score:", "\n", average)

score.sort()

# find highest (copied and pasted from Assignment2.py)
loop_iteration_range = len(score)
highest_hitherto = score[0] # tell computer to assume index 0 is highest
# make the computer skeptical and check
for next_percentage in range(loop_iteration_range):
    if score[next_percentage] > highest_hitherto:
        highest_hitherto = score[next_percentage]
highest = highest_hitherto # updated English
print("Highest score:", "\n", highest)

# find lowest (copied and pasted from Assignment2.py)
loop_iteration_range = len(score)
lowest_hitherto = score[0] # tell computer to assume index 0 is lowest
# make the computer skeptical and check
for next_percentage in range(loop_iteration_range):
    if score[next_percentage] < lowest_hitherto:
        lowest_hitherto = score[next_percentage]
lowest = lowest_hitherto # updated English
print("Lowest score:", "\n", lowest)

# count scores above average (copied and pasted from Assignment2.py)
total_above_average_hitherto = 0
for next_percentage in range(loop_iteration_range):
    if score[next_percentage] > average:
        total_above_average_hitherto = total_above_average_hitherto + 1
total_above_average_scores = total_above_average_hitherto # updated English
print("Scores above average:", "\n", total_above_average_scores)

# remove lowest score from the list
score = score[1:]
print("Scores after dropping lowest:", "\n", score)

# find new average
# simply copy and paste from above
average = sum(score) / len(score)
average = round(average, 2) # round to two decimal points
print("New average:", "\n", average)

"""
Finished implememtation at 10:18p.m.
"""


