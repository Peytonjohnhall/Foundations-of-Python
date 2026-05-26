# -----------------------------------------------

# Programmer : Peyton Hall

# Date       : 02/27/2026

# Description: Student Grade Tracker using Lists

# -----------------------------------------------

print("\n")
""" Part 1 """
# Note: This code block defines two lists: one containing student names, another containing their grades.
#		It prints the lists as well as the length and data type of the names list.
student_names = ["Alice", "Bob", "Carlos", "Diana", "Ethan",
                  "Fiona", "George", "Hannah"]
student_grades = [88, 72, 95, 61, 84, 77, 90, 68]
print("=== Part 1: Creating and Displaying Lists ===", "\n",
	  "Student Names : ", student_names, "\n",
	  "Student Grades: ", student_grades, "\n",
	  "Total Students: ", len(student_names), "\n"
	  "Data Type: ", type(student_grades), "\n")

""" Part 2 """
# Note: This code block simply shows the first, last, first 3, and last 3 students with their corresponding grades.
#		It also shows the middle four names and grades along with every other name. Lastly, it reversed the order.
print("=== Part 2: Indexing and Slicing ===", "\n",
	  "First student : ", student_names[0], " | ", "Grade: ", student_grades[0], "\n",
	  "Last student  : ", student_names[-1], " | ", "Grade: ", student_grades[-1], "\n",
	  "First 3 names : ", student_names[:3], "\n", "First 3 grades: ", student_grades[:3], "\n",
	  "Last 3 names  : ", student_names[-3:], "\n", "Last 3 grades : ", student_grades[-3:], "\n",
	  "Middle names  : ", student_names[2:6], "\n", "Middle grades : ", student_grades[2:6], "\n",
	  "Every other   : ", student_names[0:8:2], "\n", "Reversed names: ", student_names[::-1], "\n")

""" Part 3 """
# Note: This code block adds Ivan and his grade to the end of each appropriate list, inserts Julia and her grade at
# 		index 3 of the appropriate list, removes Bob and his grade and returns the value of his grade, changes 
#		Diana's grade to a 78, and prints the updated lists.
student_names.append("Ivan")
student_grades.append(81)
student_names.insert(3, "Julia")
student_grades.insert(3, 93)
student_names.remove("Bob")
student_grades.pop(1)
student_grades[3] = 78
print("=== Part 3: Modifying Lists ===", "\n", 
	  "Updated Names : ", student_names, "\n",
	  "Updated Grades: ", student_grades, "\n")

""" Part 4 """
# Note: This code block computes the class average rounded to two decimal points, finds the index of the highest grade,
#		saves a variable that contains the value of sorted grades, and uses that information to firstly loop through the 
#		grades list to find how many are 80 or avove and secondly print relevant information.
class_average = round(sum(student_grades) / len(student_grades), 2)
highest_grade_index = student_grades.index(max(student_grades))
sorted_grades = sorted(student_grades)
list_length = len(student_grades)
eighty_or_higher_count = 0
for g in range(list_length):
	if student_grades[g] >= 80:
		eighty_or_higher_count = eighty_or_higher_count + 1
print("=== Part 4: List Methods and Analysis ===", "\n",
	  "Highest Grade : ", max(student_grades), "\n",
	  "Lowest Grade  : ", min(student_grades), "\n",
	  "Class Average : ", class_average, "\n",
	  "Top Student   : ", student_names[highest_grade_index], "\n",
	  "Sorted Grades : ", sorted_grades, "\n",
	  "Students >= 80: ", eighty_or_higher_count, "\n")

""" Part 5 """
# Note: This code block creates a new list, loops through the list x amount of times, where x is the length of both former lists, 
#		and adds students' names with their corresponding grades, which results in x nested lists, with length two, inside of the new list.
class_roster = []
for i in range(list_length):
	class_roster.append([student_names[i], student_grades[i]])
print("=== Part 5: Nested Lists ===", "\n",
	  "class_roster: ", class_roster, "\n", 
	  "Second student --> Name: ", class_roster[1][0], " | Grade: ", class_roster[1][1])
for i in range(list_length):
	print(" Student: ", class_roster[i][0], "   Grade: ", class_roster[i][1])
half_the_list_length = int(len(class_roster) / 2)
print(" First half of roster:", class_roster[:half_the_list_length], "\n")

""" Part 6 """
# Note: This code block defines which students passed by, looping through the newly created list, finding them based on inequality.
#		It also boosts the grades by five points, then, based on interval inequalities, determines the letter grade for each student.
#		Finally, of course, the relevant information gets printed to the terminal (if using command line interface).
passing_students = [class_roster[check_seventy_plus][0] for check_seventy_plus in range(len(class_roster)) if class_roster[check_seventy_plus][1] >= 70]
boosted_grades = [points + 5 for points in student_grades]
letter_grades = []
for percent in student_grades:
	if percent >= 90:
		letter_grades.append("A")
	if 89 >= percent >= 80:
		letter_grades.append("B")
	if 79 >= percent >= 70:
		letter_grades.append("C") 
	if 69 >= percent >= 60:
		letter_grades.append("D")
	if percent < 60:
		letter_grades.append("F")
print("=== Part 6: List Comprehensions ===", "\n", 
	  "Passing Students: ", passing_students, "\n",
	  "Boosted Grades  : ", boosted_grades, "\n",
	  "Letter Grades   : ", letter_grades, "\n")

""" Part 7 """
# Note: This code block defines a function and calls it at the end. The function requires two arguments, those are, a couple
#		of newly created lists, class_roster and letter_grades. Because the former list is nested, filtering inner items requites double 
#		indexing, and with the latter being a non-nested list of strings, double indexing is not needed. The function uses the information
#		in these lists to print, in the original order, students' names, percentage points, and letter grades. After the first 
#		print statement in the function, the class average is calculated, one for loop finds the maximum score and corresponding student name,
#		and another finds the minimum score and corresponding student name. The findings appear in the second print statement in 
#		the function, concluded, similarly to the first print statement, with a long line, upon which the third portion of this function 
#		begins. The third portion creates a new list, loops through class_roster, viz. the original nested list, and swaps the positionings of 
#		the two inner items; therefore, using the sort() method, the list is able to be sorted by percentages from low to high, with the highest 
#		three sliced. The double indicies, corresponding to each filtered value in the new list, top_three, are called to point to the variables 
#		whose values are, thirdly and finally, printed.
def print_report_card(class_roster, letter_grades):
	print("=== Part 7: Report Card Function ===", "\n", 
		  "=============================", "\n",
		  "      CLASS REPORT CARD", "\n",
		  "=============================", "\n",
		  "1. ", class_roster[0][0], " | Grade: ", class_roster[0][1], "Letter: ", letter_grades[0], "\n",
		  "2. ", class_roster[1][0], " | Grade: ", class_roster[1][1], "Letter: ", letter_grades[1], "\n",
		  "3. ", class_roster[2][0], " | Grade: ", class_roster[2][1], "Letter: ", letter_grades[2], "\n",
		  "4. ", class_roster[3][0], " | Grade: ", class_roster[3][1], "Letter: ", letter_grades[3], "\n",
		  "5. ", class_roster[4][0], " | Grade: ", class_roster[4][1], "Letter: ", letter_grades[4], "\n",
		  "6. ", class_roster[5][0], " | Grade: ", class_roster[5][1], "Letter: ", letter_grades[5], "\n",
		  "7. ", class_roster[6][0], " | Grade: ", class_roster[6][1], "Letter: ", letter_grades[6], "\n",
		  "8. ", class_roster[7][0], " | Grade: ", class_roster[7][1], "Letter: ", letter_grades[7], "\n",
		  "9. ", class_roster[8][0], " | Grade: ", class_roster[8][1], "Letter: ", letter_grades[8])
	avg = round(sum([student[1] for student in class_roster]) / len(class_roster), 2)
	max_score = class_roster[0][1] # tell the computer to assume conditional proof
	min_score = class_roster[0][1] # tell the computer to assume conditional proof
	max_name = class_roster[0][0] # tell the computer to assume conditional proof
	min_name = class_roster[0][0] # tell the computer to assume conditional proof
	# find true max
	for eachItem in class_roster:
		if eachItem[1] > max_score:
			max_score = eachItem[1]
			max_name = eachItem[0]
	# find true min
	for eachItem in class_roster:
		if eachItem[1] < min_score:
			min_score = eachItem[1]
			min_name = eachItem[0]
	print(" ----------------------------", "\n",
		  "Class Average : ", avg, "\n",
		  "Highest Score : ", max_score, "(", max_name, ")", "\n",
		  "Lowest Score  : ", min_score, "(", min_name, ")", "\n",
		  "----------------------------")
	# avoid sorting in alphabetical order
	percent_to_the_left = [] # initialize a copy to swap inner indicies
	for eachItem in class_roster:
		# percent must be appended first to sort by grades low to high
		percent_to_the_left.append([eachItem[1], eachItem[0]]) # add to the new list
	percent_to_the_left.sort() # percent low to high
	top_three = percent_to_the_left[-3:]
	first_place_percent, first_place_name = top_three[2][0], top_three[2][1]
	second_place_percent, second_place_name = top_three[1][0], top_three[1][1]
	third_place_percent, third_place_name = top_three[0][0], top_three[0][1]
	print(" *** HONOR ROLL (Top 3) ***", "\n",
		  first_place_name, " - ", first_place_percent, "\n",
		  second_place_name, " - ", second_place_percent, "\n",
		  third_place_name, " - ", third_place_percent, "\n")
	return
print_report_card(class_roster, letter_grades)