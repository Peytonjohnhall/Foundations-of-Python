"""

This is a functional python code file. You can copy this directly into an IDE and start working. 

 

Introduction to Python

Assignment 6: Working with Python Strings

Points: ______ / 5

Overview:
In this assignment you will build a student grade tracker using
Python strings. You will practice:

• Escape sequences
• String formatting (f-strings and format())
• Searching strings
• split() and join()
• Building multi-line reports
• String Builder equivalent using list + join()

⚠ IMPORTANT:
Your output must appear in EXACTLY the same order shown
in the Expected Output sections.
"""

# -----------------------------------------------
# Programmer : Your Name
# Date       : Today's Date
# Description: Student Grade Tracker using Strings
# -----------------------------------------------


# =====================================================
# Part 1: Creating Strings and Escape Sequences (1 pt)
# =====================================================

print("=== Part 1: Creating and Displaying Strings ===\n")

# 1. Create a string variable called course_title:
#    Introduction to Python Programming
course_title = "Introduction to Python Programming"

# 2. Create a multi-line string called welcome_message using escape sequences
#    It must print exactly:
#
#    Welcome to "Introduction to Python Programming"
#    This course will teach you:
#        - String manipulation
#        - Data formatting
#        - Searching text
welcome_message = f"Welcome to \"{course_title}\"\nThis course will teach you:\n\t- String manipulation\n\t- Data formatting\n\t- Searching text"

# 3. Print both variables
print(course_title + "\n" + welcome_message)
# 4. Print the length of course_title
print(len(course_title))
# 5. Print the data type of course_title
print(type(course_title))


# =====================================================
# Part 2: Splitting and Joining Strings (1 pt)
# =====================================================

print("\n=== Part 2: Splitting and Joining Strings ===\n")

# Use this string:
student_data = "Alice,88;Carlos,95;Julia,93;Diana,78"

# 1. Split student_data into student records
student_records = student_data.split(";")
# 2. Print the records list
print(student_records)
# 3. Split each record into name and grade
student_records = [record.split(",") for record in student_data.split(";")]
# 4. Store names in list called names
names = [record[0] for record in student_records]
# 5. Store grades in list called grades
grades = [record[1] for record in student_records]
# 6. Use join() to print names separated by " | "
print(" | ".join(names))
# 7. Use join() to print grades separated by ", "
print(", ".join(grades))


# =====================================================
# Part 3: Searching and Replacing (1 pt)
# =====================================================

print("\n=== Part 3: Searching and Replacing ===\n")

announcement = "The midterm exam is on Friday. The final exam is in December."

# 1. Check if "midterm" exists using in
print("midterm" in announcement)
# 2. Find index of first "exam"
print(announcement.index("exam"))
# 3. Count how many times "exam" appears
print(announcement.count("exam"))
# 4. Replace "Friday" with "Monday"
announcement = announcement.replace("Friday", "Monday")
# 5. Print all results
print(announcement) # see print statements in previous lines


# =====================================================
# Part 4: String Formatting (1 pt)
# =====================================================

print("\n=== Part 4: String Formatting ===\n")

name = "Carlos"
grade = 95
average = 89.4567

# 1. Print using f-string:
#    Carlos scored 95 on the exam.
print(f"{name} scored {grade} on the exam.")
# 2. Print using format()
print("{} scored {} on the exam.".format(name, grade))
# 3. Print average rounded to 2 decimal places
print(round(average, 2))
# 4. Print formatted table:
#
#    Name     | Grade
#    Carlos   | 95
print(f"{"Name":<8} | Grade")
print(f"{name:<8} | {grade}")


# =====================================================
# Part 5: String Builder Equivalent (0.5 pt)
# =====================================================

print("\n=== Part 5: String Builder Equivalent ===\n")

names = ["Alice", "Carlos", "Julia"]
grades = [88, 95, 93]

# 1. Create empty list report_lines
report_lines = []
# 2. Loop and append formatted strings like:
#       Alice - 88
for i in range(len(names)):
	report_lines.append(f"{names[i]} - {grades[i]}")
# 3. Use "\n".join(report_lines)
print("\n".join(report_lines))
# 4. Print final report
""" See print statement above and output """


# =====================================================
# Part 6: Multi-Line Grade Report (0.5 pt)
# =====================================================

print("\n=== Part 6: Building a Multi-Line Report ===\n")

# Build a final formatted report using:
# • join()
# • f-strings
# • newline escape sequences
# • header and footer lines
# • average calculation
#
# Format example:
#
# =================================
#         CLASS REPORT
# =================================
# Alice    : 88
# Carlos   : 95
# Julia    : 93
# ---------------------------------
# Average  : 92.00
# =================================


# =====================
# End of Assignment
# =====================
rows = [f"{names[i]:<8} : {grades[i]}" for i in range(len(names))]
average = sum(grades) / len(grades)
print("=================================" + "\n" + 
	  "\t" + "CLASS REPORT" + "\n" + 
	  "=================================" + "\n" +
	  "\n".join(rows) + "\n" +
	  "---------------------------------" + "\n" +
	  f"Average  : {average:.2f}" + "\n" +
	  "=================================" + "\n\n" +
	  "=====================" + "\n" +
	  "End of Assignment" + "\n" + 
	  "=====================")

