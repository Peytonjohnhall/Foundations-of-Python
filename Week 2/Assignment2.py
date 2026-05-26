"""
@Author: Peyton John Hall
A Python program that stores percentages in a list of scores, then performes
calculations; viz. it finds the mu, top score, bottom score, total above 
average (exclusive), and finds and removes the bottom two scores from the list.
"""

def get_input():
    score = [] # use singular rather than plural for readability
    while True:
        percentage = float(input("Enter exam scores one at a time. Once you"
                                 " are done, enter \"-1\": "))
        if percentage == -1:
            break
        elif 0 <= percentage <= 100:
            score.append(percentage) # append, viz. add
        else:
            print("Invalid input.")
    print("Scores entered:", "\n", score)
    return score

def calculate_mu(score):
    loop_iteration_range = len(score)
    the_sum = 0 # before counting, it is zero
    for next_percentage in range(loop_iteration_range):
        the_sum = the_sum + score[next_percentage]
    average = the_sum / len(score)
    average = round(average, 2) # round to two decimal points
    return average

def find_highest(score):
    loop_iteration_range = len(score)
    highest_hitherto = score[0] # tell computer to assume index 0 is highest
    # make the computer skeptical and check
    for next_percentage in range(loop_iteration_range):
        if score[next_percentage] > highest_hitherto:
            highest_hitherto = score[next_percentage]
    highest = highest_hitherto # updated English
    return highest

def find_lowest(score):
    loop_iteration_range = len(score)
    lowest_hitherto = score[0] # tell computer to assume index 0 is lowest
    # make the computer skeptical and check
    for next_percentage in range(loop_iteration_range):
        if score[next_percentage] < lowest_hitherto:
            lowest_hitherto = score[next_percentage]
    lowest = lowest_hitherto # updated English
    return lowest

def find_above_average(score, average):
    loop_iteration_range = len(score)
    total_above_average_hitherto = 0
    for next_percentage in range(loop_iteration_range):
        if score[next_percentage] > average:
            total_above_average_hitherto = total_above_average_hitherto + 1
    total_above_average_scores = total_above_average_hitherto # updated English
    return total_above_average_scores

def remove_lowest(score, lowest):
    score_list_copy = score[:]
    score_list_copy.remove(lowest) # if duplicates, only removes leftmost
    return score_list_copy

def new_mu(score_list_copy):
    new_average = calculate_mu(score_list_copy)
    return new_average

def main():
    score = get_input()
    if not score:
        print("The list is empty.")
    else:
        average = calculate_mu(score)
        highest = find_highest(score)
        lowest = find_lowest(score)
        total_above_average_scores = find_above_average(score, average)
        score_list_copy = remove_lowest(score, lowest)
        new_average = new_mu(score_list_copy)
        print("Average score:", "\n", "[", average, "]" "\n",
              "Highest score:", "\n", "[", highest, "]" "\n",
              "Lowest score:", "\n", "[", lowest, "]" "\n",
              "Scores above average:", "\n", 
              "[", total_above_average_scores, "]" "\n",
              "Scores after dropping lowest:", "\n", score_list_copy, "\n",
              "New average:", "\n", "[", new_average, "]" "\n")

if __name__ == "__main__":
    main()