# -----------------------------------------------
# Programmer : Peyton John Hall
# Date : 03/24/2026
# Description: Student Grade Tracker using Dictionaries
# -----------------------------------------------

# Part 1: Creates a dictionary and prints basic information
student_grades = {
	"Alice": 88, "Bob": 72, "Carlos": 95, "Diana": 61,
	"Ethan": 84, "Fiona": 77, "George": 90, "Hannah": 68
}
print(f"=== Part 1: Creating and Displaying a Dictionary ===", "\n",
	  f"student_grades: {student_grades}", "\n",
	  f"Total Students: {len(student_grades)}", "\n",
	  f"Data Type     : {type(student_grades)}", "\n", sep = "") # left shift

# Part 2: Demonstrates use of .get(), .keys(), .values(), and .items() functions
print(f"=== Part 2: Accessing Dictionary Data ===", "\n",
	  f"Alice's grade    : ", student_grades["Alice"], "\n",
	  f"Carlos's grade   : ", student_grades.get("Carlos"), "\n",
	  f"Zara's grade     : ", student_grades.get("Zara", "Not Found"), "\n",
	  f"Is Diana enrolled: ", "Diana" in student_grades, "\n",
	  f"Is Zara enrolled : ", "Zara" in student_grades, "\n",
	  f"All student names: ", student_grades.keys(), "\n",
	  f"All grades       : ", student_grades.values(), "\n",
	  f"All records: ", sep = "") # left shift
for key, value in student_grades.items():
    print(f"{key:<16} : {value}")
print("\n")

# Part 3: Demonstrates use of .update() and .pop() functions
student_grades.update({"Ivan": 81, "Julia": 93})
student_grades["Diana"] = 78
removed_grade = student_grades.pop("Bob")
student_grades.update({"Ethan": 87, "Karen": 79})
print(f"=== Part 3: Modifying a Dictionary ===", "\n",
	  f"Removed student: Bob  |  Grade: {removed_grade}", "\n",
	  f"Updated Grades : {student_grades}", "\n",
	  f"Total Students : {len(student_grades)}", "\n", sep = "") # left shift

# Part 4: Demonstrates use of max(), min(), list(), and sorted() functions
top_student = max(student_grades, key = student_grades.get)
top_grade = student_grades[top_student]
bottom_student = min(student_grades, key = student_grades.get)
bottom_grade = student_grades[bottom_student]
values = list(student_grades.values()) # convert only the values to a list
average = round(sum(values) / len(values), 2)
sorted_names = sorted(student_grades.keys())
print(f"=== Part 4: Dictionary Methods and Analysis ===", "\n",
	  f"Highest Grade : {top_grade}  ( {top_student} )", "\n",
	  f"Lowest Grade  : {bottom_grade}  ( {bottom_student} )", "\n", 
	  f"Class Average : {average}", "\n",
	  f"Sorted by Name: {sorted_names}", sep = "") # left shift
""" key = lambda item: item[1] means each (name, grade) pair from .items() is passed 
in as 'item', and it sorts using item[1] according to the index of the grade, i.e. 1 """
sorted_by_grade = sorted(student_grades.items(), key = lambda item: item[1], reverse = True)
print("Top Scorers (sorted high to low):")
for name, grade in sorted_by_grade:
	print(f"  {name:<7} : {grade}")
count = 0
for i in student_grades.values(): # remember: keys() vs values()
	if i >= 80:
		count += 1
print(f"Students >= 80: {count}", "\n")

# Part 5: Builds nested dict, assigns grade/letter/status, adds rank, prints Honor Roll
print("=== Part 5: Nested Dictionaries ===", "\n",
	  "student_info:", sep = "")  # left shift
student_info = {}
for name, grade in student_grades.items():
	if grade >= 90:
		letter = "A"
		status = "Honor Roll"
	elif grade >= 80:
		letter = "B"
		status = "Good Standing"
	elif grade >= 70:
		letter = "C"
		status = "Satisfactory"
	elif grade >= 60:
		letter = "D"
		status = "Needs Improvement"
	else:
		letter = "F"
		status = "At Risk"
	student_info[name] = {"grade": grade, "letter": letter, "status": status}
for name, nested_dictionary in student_info.items():
	print(f"  {name:<8}: {nested_dictionary}")
print(f"Carlos's full record: {student_info["Carlos"]}", "\n",
	  f"Carlos's letter grade: {student_info["Carlos"]["letter"]}", sep = "") # left shift
rank = 1
for name, grade in sorted_by_grade:
	# adds a key, i.e. rank, and value, i.e. rank number, to the nested dictionaries
	student_info[name]["rank"] = rank
	rank += 1
print("Honor Roll students:")
for name, nested_dictionary in student_info.items():
	if nested_dictionary["letter"] == "A": # viz. ["key"] == "value"
		print(f"  {name:<7} - {nested_dictionary["grade"]} - {nested_dictionary["letter"]}")
print("\n")

# Part 6: Uses dictionary comprehensions to filter and transform data
passing_students = {name: grade for name, grade in student_grades.items() if grade >= 70}
boosted_grades = {name: grade + 5 for name, grade in student_grades.items()}
letter_grades = {name: ("A" if grade >= 90 else
						"B" if grade >= 80 else
						"C" if grade >= 70 else
						"D" if grade >= 60 else
						"F") 
						for name, grade in student_grades.items()}
status_dict = {name: ("Honor Roll" if grade >= 90 else
					  "Good Standing" if grade >= 80 else
					  "Satisfactory" if grade >= 70 else
					  "Needs Improvement" if grade >= 60 else
					  "At Risk")
					  for name, grade in student_grades.items()}
print("=== Part 6: Dictionary Comprehensions ===", "\n",
	  f"Passing Students: {passing_students}", "\n",
	  f"Boosted Grades  : {boosted_grades}", "\n",
	  f"Letter Grades   : {letter_grades}", "\n",
	  f"Status Dict     : {status_dict}", "\n", sep = "") # left shift

# Part 7: Prints formatted report card using built-in functions, sorting, and slicing
def print_report_card(student_grades, letter_grades):
	"""
	could also pass the following 5 variables into the function
	but retyped for visual convenience and all came from part 4:
	"""
	values = list(student_grades.values())
	average = round(sum(values) / len(values), 2)
	top_student = max(student_grades, key = student_grades.get)
	bottom_student = min(student_grades, key = student_grades.get)
	sorted_by_grade = sorted(student_grades.items(), key = lambda item: item[1], reverse = True)
	print("=== Part 7: Report Card Function ===", "\n",
		  "=============================", "\n",
		  "      CLASS REPORT CARD      ", "\n",
		  "=============================", sep = "") # left shift
	i = 1
	# .items() returns a view of (key, value) pairs as tuples
	for name, grade in student_grades.items():
		print(f"{i}. {name:<8} | Grade: {grade} | Letter: {letter_grades[name]}")
		i += 1
	print("-----------------------------", "\n",
		 f"Class Average : {average}", "\n",
		 f"Highest Score : {student_grades[top_student]}  ( {top_student} )", "\n",
		 f"Lowest Score  : {student_grades[bottom_student]}  ( {bottom_student} )", "\n",
		 "-----------------------------", "\n",
		 "  *** HONOR ROLL (Top 3) ***", sep = "") # left shift
	for name, grade in sorted_by_grade[:3]:
		print(f"  {name} - {grade}") # print key - value
print_report_card(student_grades, letter_grades)