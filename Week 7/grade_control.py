# -----------------------------------------------
# Programmer : Peyton John Hall
# Date : 03/25/2026
# Description: Student Grade Tracker — Control Flow,
# Loops, Break/Continue, List Comprehensions
# -----------------------------------------------

# Part 1: Creates two lists, defines criteria for letter and status
student_names = ["Alice", "Bob", "Carlos", "Diana", "Ethan",
"Fiona", "George", "Hannah", "Ivan", "Julia"]
student_grades = [88, 72, 95, 61, 84, 55, 90, 68, 81, 93]
print("=== Part 1: Conditional Statements ===")
name = student_names[0]
grade = student_grades[0]
if grade >= 90:
	letter = "A"
	status = "Excellent"
elif grade >= 80:
	letter = "B"
	status = "Good"
elif grade >= 70:
	letter = "C"
	status = "Satisfactory"
elif grade >= 60:
	letter = "D"
	status = "Needs Improvement"
else:
	letter = "F"
	status = "Failing"
print(f"Student: {name}  |  Grade: {grade}  |  Letter: {letter}  |  Status: {status}", "\n\n"
	  f"Full Class Classification:", sep = "")
for i in range(len(student_names)):
	name = student_names[i]
	grade = student_grades[i]
	if grade >= 90:
		letter = "A"
		status = "Excellent"
	elif grade >= 80:
		letter = "B"
		status = "Good"
	elif grade >= 70:
		letter = "C"
		status = "Satisfactory"
	elif grade >= 60:
		letter = "D"
		status = "Needs Improvement"
	else:
		letter = "F"
		status = "Failing"
	print(f"  {name:<8}: {grade}  {letter}  {status}")
# loops through student_names and student_grades using indices, and prints each student's status
print("\n", "Honor Roll Check:", sep = "")
for i in range(len(student_names)):
	name = student_names[i]
	grade = student_grades[i]
	if grade >= 90:
		print(f"  {name} -- HONOR ROLL")
	elif grade >= 60:
		print(f"  {name} -- Passing")
	else:
		print(f"  {name} -- FAILING -- needs immediate attention")
# find how many people got each grade and prints it
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0
for grade in student_grades:
	if grade >= 90:
		a_count += 1
	elif grade >= 80:
		b_count += 1
	elif grade >= 70:
		c_count += 1
	elif grade >= 60:
		d_count += 1
	else:
		f_count += 1
print("\n", "Grade Band Counts:", "\n",
	  f"  {'A (90-100)':<11}: {a_count} student(s)", "\n",
	  f"  {'B (80-89)':<11}: {b_count} student(s)", "\n",
	  f"  {'C (70-79)':<11}: {c_count} student(s)", "\n",
	  f"  {'D (60-69)':<11}: {d_count} student(s)", "\n",
	  f"  {'F (0-59)':<11}: {f_count} student(s)", sep = "")

# Part 2: Loops through the list(s) and prints information
print("\n", "=== Part 2: for Loops and Built-in Functions ===", "\n", 
	  "Roster (for loop with range):", sep = "")
for i in range(len(student_names)):
	print(f"{i + 1:>4}. {student_names[i]}")
print("\n", "Roster (enumerate):", sep = "")
# enumarate() adds an index to each item in an iterable
for i, name in enumerate(student_names, start = 1):
	print(f"{i:>4}. {name}")
print("\n", "Name + Grade (zip):", sep = "")
# zip() combines multiple iterable elements into one iterable element
for name, grade in zip(student_names, student_grades):
	print(f"  {name:<8}: {grade}")
print("\n", "Total Points : ", sum(student_grades), sep = "")
total = 0
for grade in student_grades:
	total += grade
average = round(total / len(student_grades), 2)
print("Class Average:", average)
print("\n", "Every-other student (step=2):", sep = "")
for i in range(0, len(student_names), 2): # starting at index 0, going every other
	print(f"  {student_names[i]:<7} : {student_grades[i]}")

# Part 3: Uses while loops to test criteria under conditional logic
print("\n", "=== Part 3: while Loops ===", "\n",
	  "Roster (while loop):", sep = "")
i = 0
while i < len(student_names):
	print(f"  {student_names[i]:<7} : {student_grades[i]}")
	i += 1
print("\n", "Searching for first student above 90:", sep = "")
i = 0
found = False
while i < len(student_grades) and not found:
	if student_grades[i] > 90:
		print(f"  Found: {student_names[i]} with grade {student_grades[i]}")
		found = True
	i += 1
print("\n", "Countdown:", sep = "")
n = 5
while n > 0:
	print(f"  {n}...")
	n -= 1
print("  Grades submitted!", "\n\n",
	  "Running total (stop when total > 400):", sep = "")
i = 0
running_total = 0
while i < len(student_grades) and running_total <= 400:
	running_total += student_grades[i]
	print(f"  Added {student_names[i]} ({student_grades[i]}) --> Running total: {running_total}")
	i += 1
print(f"  Stopped after {i} students. Total = {running_total}")

# Part 4: Demonstrates break (exiting loop) and continue (restarting loop)
print("\n", "=== Part 4: break and continue ===", "\n",
	  "Search for first FAILING student (break):", sep = "")
for name, grade in zip(student_names, student_grades):
	if grade < 60:
		print(f"  First failing student: {name} with grade {grade}")
		break # exit loop
print("\n", "Passing students only (continue):", sep = "")
for name, grade in zip(student_names, student_grades):
	if grade < 60:
		continue # don't print. go back to for
	print(f"  {name:<7} : {grade}")
print("\n", "Skip grades divisible by 10 (continue):", sep = "")
for name, grade in zip(student_names, student_grades):
	if grade % 10 == 0:
		print(f"  Skipping {name} (grade {grade} is divisible by 10)")
		continue # go back to for
	print(f"  {name:<7} : {grade}")
print("\n", "First 3 Honor Roll students (break after 3):", sep = "")
count = 0
for name, grade in zip(student_names, student_grades):
	if grade >= 85:
		print(f"  {name}: {grade}")
		count += 1
		if count == 3:
			print("  (Stopping after 3 results)")
			break # exit loop
print("\n", "  for/else demonstration (looking for a grade of exactly 100):", sep = "")
for name, grade in zip(student_names, student_grades):
	if grade == 100:
		print(f"  Found perfect score: {name}")
		break # exit loop
else:
	print("    No perfect score in the class.")

# Part 5: Demonstrates that for loops can exist inside for loops
print("\n", "=== Part 5: Nested Loops ===", "\n",
	  "Grade Comparison (who outscored whom):", sep = "")
for i in range(len(student_grades)):
	count = 0
	for j in range(len(student_grades)):
		if student_grades[i] > student_grades[j]:
			count += 1
	print(f"  {student_names[i]:<8} outscored {count} other student(s)")
print("\n", "Grade Pyramid (top 4 students):", sep = "")
top_names = ["Carlos", "Julia", "George", "Alice"]
top_grades = [95, 93, 90, 88]
for i in range(len(top_names)):
	stars = "*" * (top_grades[i] // 10)
	print(f"  {top_names[i]:<8} ({top_grades[i]}) {stars}")
print("\n", "Grade scan (inner break on first failing grade per row) :", sep = "")
categories = ["Midterm", "Final", "Project"]
scores_matrix = [
	[85, 90, 88], # Alice
	[70, 68, 74], # Bob
	[95, 97, 93], # Carlos
	[60, 55, 65], # Diana
	[80, 84, 82], # Ethan
]
sub_names = ["Alice", "Bob", "Carlos", "Diana", "Ethan"]
for i in range(len(scores_matrix)):
	print(f"  {sub_names[i]}:", end = "  ")
	for j in range(len(scores_matrix[i])):
		score = scores_matrix[i][j]
		print(f"{categories[j]}={score}", end = "  ")
		if score < 60:
			print("[FAILED - stopping]")
			break
	else:
		print()

# Part 6: Uses list comprehensions with for, if, and else to create new lists
print("\n", "=== Part 6: List Comprehensions ===", sep = "")
boosted = [grade + 5 for grade in student_grades]
passing = [name for name, grade in zip(student_names, student_grades) if grade >= 60]
letters = ["A" if grade >= 90 else
		   "B" if grade >= 80 else
		   "C" if grade >= 70 else
		   "D" if grade >= 60 else
		   "F" for grade in student_grades]
records = [f"{name}: {grade}" for name, grade in zip(student_names, student_grades)]
mult_table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
ranked = [f"#{i} {name} ({grade})"
		  for i, (name, grade) in enumerate(sorted(zip(student_names, student_grades), key = lambda x: x[1], reverse = True), start = 1)]
print("Boosted Grades    : ", boosted, "\n",
	  "Passing Students  : ", passing, "\n",
	  "Letter Grades     : ", letters, "\n",
	  "Name-Grade Records: ", records, "\n",
	  "3x3 Mult Table    : ", mult_table, "\n",
	  "Ranked Students   : ", ranked, sep = "")

# Part 7: A function, using loops, conditionals, and list comprehensions, that generates a report
def generate_report(student_names, student_grades):
	print("\n", "=== Part 7: Combined Challenge — Grade Report Function ===", "\n",
		  "=" * 36, "\n",
		  " " * 7, "STUDENT GRADE REPORT", "\n",
		  "=" * 36, "\n",
		  "(Failing students marked with  ***)",
		  sep = "")
	letters = ["A" if g >= 90 else
			   "B" if g >= 80 else
			   "C" if g >= 70 else
			   "D" if g >= 60 else
			   "F" for g in student_grades]
	for name, grade, letter in zip(student_names, student_grades, letters):
		if grade < 60:
			print(f"  *** {name:<8} | {grade:<2} | {letter}  -- FAILING")
			continue
		print(f"      {name:<8} | {grade:<2} | {letter}")
	print("-" * 36)
	total = sum(student_grades)
	avg = round(total / len(student_grades), 1)
	high = max(student_grades)
	low = min(student_grades)
	print("  Class Average : ", avg, "\n",
		  "  Highest Score : ", high, f"  ({student_names[student_grades.index(high)]})", "\n",
		  "  Lowest Score  : ", low, f"  ({student_names[student_grades.index(low)]})", sep = "")
	print("-" * 36, "\n", "  Grade Distribution:", sep = "")
	dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
	for l in letters: # iterate through letter grades
		dist[l] += 1
	for i in ["A", "B", "C", "D", "F"]:
		print(f"    {i}: {'█' * dist[i]} ({dist[i]})")
	print("-" * 36, "\n", 
		  " " * 2, "*** HONOR ROLL (Top 3) ***", sep = "")
	top3 = sorted(zip(student_names, student_grades), key = lambda x: x[1], reverse = True)[:3]
	for name, grade in top3:
		print(" " * 4, f"{name:<8} - {grade}", sep = "")
	print("-" * 36, "\n", 
		  " " * 2, "At-Risk Students:", sep = "")
	i = 0
	found = False
	while i < len(student_grades):
		if student_grades[i] < 60:
			print(" " * 3, f"{student_names[i]} ({student_grades[i]}) -- needs intervention")
			found = True
		i += 1
	if not found:
		print("None")
	print("=" * 36)
generate_report(student_names, student_grades)