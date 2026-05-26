# -----------------------------------------------

# Programmer : Peyton John Hall

# Date       : 03/11/2026

# Description: Student Grade Tracker using Tuples

# -----------------------------------------------

print("\n")
"""
Part 1 creates two tuples and prints them as well as the length and type of student_names.
It could have printed the length and type of student_grades, and that would return the same 
result. If the line that is commented out is uncommented out, it returns a TypeError because 
tuples are immutable types, meaning their structure can not be changed. However, if the objects
inside of the tuple are mutable types, meaning data types whose contents are able to be changed, 
then parts of the internal parts of the tuple can be changed.
"""
student_names = ("Alice", "Carlos", "Julia", "Diana", 
				 "Ethan", "Fiona", "George", "Hannah", "Ivan")
student_grades = (88, 95, 93, 78, 84, 77, 90, 68, 81)
print("=== Part 1: Creating and Displaying Tuples ===", "\n",
	  "Student Names               : ", student_names, "\n", 
	  "Student Grades              : ", student_grades, "\n",
	  "Total Students              : ", len(student_names), "\n",
	  "Data Type                   : ", type(student_names), "\n",
	  "# student_grades[0] = 99 -->  TypeError: 'tuple' object does not support item assignment", "\n")
# student_grades[0] = 99 # returns an error

"""
Part 2 uses indexing and slicing to find information in the tuples. 
It goes to show that tuples can be sliced.
"""
print("=== Part 2: Indexing and Slicing ===", "\n",
	  "First student               : ", student_names[0], "  |  Grade: ", student_grades[0], "\n",
	  "Last student                : ", student_names[-1], "  |  Grade: ", student_grades[-1], "\n",
	  "First 4 names               : ", student_names[:4], "\n", 
	  "First 4 grades              : ", student_grades[:4], "\n", 
	  "Last 3 names                : ", student_names[-3:], "\n",
	  "Last 3 grades               : ", student_grades[-3:], "\n",
	  "Middle names                : ", student_names[2:7], "\n",
	  "Middle grades               : ", student_grades[2:7], "\n",
	  "Every 3rd name              : ", student_names[0::3], "\n",
	  "Reversed grades             : ", student_grades[::-1], "\n")

"""
Part 3 demonstrates that tuples are compatible with the built-in functions max, min, sum, len, 
round, sorted, and type, and that tuples support the count and index methods.
"""
sorted_scores = sorted(student_grades)
sorted_desc = sorted(student_grades, reverse = True)
print("=== Part 3: Tuple Methods ===", "\n",
	  "Highest Score               : ", max(student_grades), "\n",
	  "Lowest Score                : ", min(student_grades), "\n",
	  "Average Score               : ", round(sum(student_grades) / len(student_grades), 2), "\n",
	  "Count of 90                 : ", student_grades.count(90), "\n",
	  "Count of 78                 : ", student_grades.count(78), "\n",
	  "First index of 95           : ", student_grades.index(95), "\n",
	  "Sorted (low-high)           : ", sorted_scores, "\n",
	  "Type of sorted_scores       : ", type(sorted_scores), "\n",
	  "Sorted (high-low)           : ", sorted_desc, "\n")

"""
Part 4 creates and unpacks four new tuples, uses *rest to capture intermediate 
elements, and prints the values stored in each variable. It then swaps the 
values of two variables, which, as a result, swaps the memory storage location
the two variables point to without deleting the memory.
"""
top_student   = ("Carlos", 95, "A", "Honor Roll")
bottom_record = ("Hannah", 68, "D", "Needs Improvement")
name, grade, letter, status = top_student
name2, grade2, letter2, status2 = bottom_record
score_range = (68, 95)
low, high = score_range
full_record = ("Alice", 88, "B", "Honor Roll", "Semester 1")
first_name, *rest, last_item = full_record
print("=== Part 4: Tuple Unpacking ===", "\n",
	  "Top Student: ",  "\n", 
	  "Name                        : ", name, "\n", 
	  "Grade                       : ", grade, "\n", 
	  "Letter                      : ", letter, "\n",
	  "Status                      : ", status, "\n",
	  "Bottom Record: ", "\n",
	  "Name                        : ", name2, "\n", 
	  "Grade                       : ", grade2, "\n", 
	  "Letter                      : ", letter2, "\n",
	  "Status                      : ", status2, "\n",
	  "Grade Range                 :  Low = ", low, "  |  High = ", high, "\n",
	  "First name                  : ", first_name, "\n", 
	  "Rest                        : ", *rest, "\n", 
	  "Last item                   : ", last_item)
x = 100
y = 200
print(" Before swap                 :  x = ", x, " y = ", y)
x, y = y, x
print(" After swap                  :  x = ", x, " y = ", y, "\n")

"""
Part 5 contains a series of for loops that loop through the first two tuples 
defined in the program, finds how many students scored 80 or above, uses 
index, value pairs to print a numbered roster, a grade report, and students
with low scores.
"""
eighty_plus = 0
for percent in student_grades:
	if percent >= 80:
		eighty_plus = eighty_plus + 1
print("=== Part 5: Iterating and enumerate() ===", "\n",
	  "Students scoring 80 or above: ", eighty_plus, "\n",
	  "Numbered roster: ")
for eachIndex, eachName in enumerate(student_names, start = 1):
	print(f" {eachIndex}. {eachName}")
print(" Grade Report: ")
for eachIndex, eachName in enumerate(student_names):
	# forces a fixed six characters before the printed colon
	print(f" {eachName:<6}: {student_grades[eachIndex]}")
print(" Needs Review:")
for eachIndex, eachName in enumerate(student_names):
	if student_grades[eachIndex] < 80:
		print(f" {eachName} - {student_grades[eachIndex]} - Needs Review")
print("\n")

"""
Part 6 converts the original two tuples to lists, which allows modification of
the structure of the series of elements, then converts the lists back to tuples.
It prints the updated tuples. This creates a new ovject in a new memory storage 
location and cuts access to the original objects created earlier in the program.
It then creates an empty list, adds tuples inside the list, and converts that
list to a tuple to cut off mutability. Using double indexing, slicing, and 
a for loop consisting of tuple unpacking, it prints relevant information.
"""
student_grades = list(student_grades)
student_grades.append(74)
student_grades = tuple(student_grades)
student_names = list(student_names)
student_names.append("Jasmine")
student_names = tuple(student_names)
print("=== Part 6: Converting and Nested Tuples ===", "\n", 
	  "Updated Names               : ", student_names, "\n", 
	  "Updated Grades              : ", student_grades)
class_roster = []
for eachItem in range(len(student_names)):
	class_roster.append((student_names[eachItem], student_grades[eachItem]))
class_roster = tuple(class_roster)
print(" class_roster: ", class_roster)
print(f" Third student --> Name: {class_roster[2][0]}  |  Grade: {class_roster[2][1]}")
print(f" Last 4 records: {class_roster[-4:]}")
print(" Formatted Roster:")
for name, grade in class_roster:
	print(f" Student: {name}     Grade: {grade}")
print("\n")

"""
Part 7 defines two functions. The first sets criteria for letter grades and status.
It adds the names and grades from the class roster tuple as well as the newly defined 
values stored in the variables letter grade and status to the report list and converts
the report to a tuple. The second function passes report as an argument to loop through
its contents and print them using the enumerate function to change the starting index
from zero to one. It then prints an honor roll by using a for loop consisting of tuple
unpacking.
"""
def build_report(class_roster):
	report = []
	for name, grade in class_roster:
		if grade >= 90:
			letter_grade = "A"
			status = "Honor Roll"
		elif grade >= 80:
			letter_grade = "B"
			status = "Good Standing"
		elif grade >= 70:
			letter_grade = "C"
			status = "Satisfactory"
		elif grade >= 60:
			letter_grade = "D"
			status = "Needs Improvement"
		elif grade < 60:
			letter_grade = "F"
			status = "At Risk"
		report.append((name, grade, letter_grade, status))
	return tuple(report)
report = build_report(class_roster)

def print_report(report):
	print("=== Bonus: Immutable Report Card ===", "\n",
		  "======================================", "\n",
		  "\t", "FULL CLASS REPORT CARD", "\n",
		  "======================================")
	# enumerate() saves you from tracking the index manually
	for eachItem, (name, grade, letter_grade, status) in enumerate(report, start = 1):
		print(f" {eachItem}. {name} | {grade} | {letter_grade} | {status}")
	print(" ------------------------------------", "\n", 
		  "*** HONOR ROLL ***")
	for name, grade, letter_grade, status in report:
		if grade >= 90:
			print(f" {name} - {grade} - {letter_grade}")
print_report(report)
print("\n")




