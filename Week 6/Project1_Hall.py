# -----------------------------------------------

# Programmer : Peyton John Hall

# Date       : 03/20/2026

# Description: Project 1 - BMI Calculator

# -----------------------------------------------

def validate_input():
	print("\n")
	while True:
		try:
			inputted_height = float(input("Enter your height in meters or inches: "))
			break
		except ValueError:
			print("Invalid input. Enter a number.")
	while True:
		height_type = input("Is this value in meters or inches? ").lower()
		if (height_type in ["meters", "m", "meter"]):
			height_type = "meters"
			break
		elif (height_type in ["inches", "in", "inch"]):
			height_type = "inches"
			break
		else:
			print("Invalid input. Enter something recognizable.")
	while True:
		try:
			inputted_weight = float(input("Enter your weight in kilograms or pounds: "))
			break
		except ValueError:
			print("Invalid input. Enter a number.")
	while True:
		weight_type = input("Is this value in kilograms or pounds? ").lower()
		if (weight_type in ["kilograms", "kg", "kgs" "kilos", "kilogram", "kilo"]):
			weight_type = "kilograms"
			break
		elif (weight_type in ["pounds", "lbs", "lb", "pound"]):
			weight_type = "pounds"
			break
		else:
			print("Invalid input. Enter something recognizable.")
	return inputted_height, inputted_weight, height_type, weight_type

def convert_to_inches_and_pounds(inputted_height, inputted_weight, height_type, weight_type):
	height = inputted_height
	weight = inputted_weight
	if (height_type == "meters"):
		# inches = meters * 39.3701
		height = height * 39.3701 # convert it to inches
	if (weight_type == "kilograms"):
		# pounds = kilograms * 2.20462
		weight = weight * 2.20462 # convert it to pounds
	return height, weight # inches, pounds

def calculateBMI(height: float, weight: float):
	if (not isinstance(height, float)) | (not isinstance(weight, float)):
		raise TypeError("height and weight variables not of type float")
	# print(height)
	# print(weight)

	# if input goes against laws of physics
	if (height <= 0 or weight <= 0):
		return None # function returns None
	# if input is above world record of 107 inches or 1400 pounds
	if (height > 107 or weight > 1400):
		return None # function returns None
	# if input is below world record of 9.45 inches or 0.46738 pounds (infant)
	if (height < 9.45 or weight < 0.46738):
		return None # function returns None

	def get_BMI_score(height, weight):
		# BMI = (lbs / in^2) * 703
		BMI_score = (weight / (height ** 2)) * 703
		BMI_score = round(BMI_score, 1)
		return BMI_score

	BMI_score = get_BMI_score(height, weight)

	def get_classification(BMI_score):
		if (BMI_score < 18.5):
			BMI_classification = "Underweight"
		if (18.5 <= BMI_score < 25.0):
			BMI_classification = "Healthy"
		if (25.0 <= BMI_score < 30.0):
			BMI_classification = "Overweight"
		if (BMI_score >= 30.0):
			BMI_classification = "Obese"
		return BMI_classification

	BMI_classification = get_classification(BMI_score)

	return [height, weight, BMI_score, BMI_classification]

def main():
	inputted_height, inputted_weight, height_type, weight_type = validate_input()
	height, weight = convert_to_inches_and_pounds(inputted_height, inputted_weight, height_type, weight_type)
	result = calculateBMI(height, weight)
	if (result is None):
		print("Invalid input value(s)." + "\n")
		return
	height, weight, BMI_score, BMI_classification = result # unpack list
	if (inputted_weight.is_integer() and inputted_height.is_integer()):
		print(f"Height: {inputted_height:.0f} {height_type}" + "\n" + f"Weight: {inputted_weight:.0f} {weight_type}" + "\n")
		print(f"A weight of {inputted_weight:.0f} {weight_type} and a height of {inputted_height:.0f} {height_type} represents a ")
	if (inputted_weight.is_integer() and (not inputted_height.is_integer())):
		print(f"Height: {inputted_height} {height_type}" + "\n" + f"Weight: {inputted_weight:.0f} {weight_type}" + "\n")
		print(f"A weight of {inputted_weight:.0f} {weight_type} and a height of {inputted_height} {height_type} represents a ")
	if ((not inputted_weight.is_integer()) and inputted_height.is_integer()):
		print(f"Height: {inputted_height:.0f} {height_type}" + "\n" + f"Weight: {inputted_weight} {weight_type}" + "\n")
		print(f"A weight of {inputted_weight} {weight_type} and a height of {inputted_height:.0f} {height_type} represents a ")
	if ((not inputted_weight.is_integer()) and (not inputted_height.is_integer())):
		print(f"Height: {inputted_height} {height_type}" + "\n" + f"Weight: {inputted_weight} {weight_type}" + "\n")
		print(f"A weight of {inputted_weight} {weight_type} and a height of {inputted_height} {height_type} represents a ")
	print(f"BMI of {BMI_score}, which is classified as {BMI_classification.lower()}.")
	print("\n")

if __name__ == "__main__":
    main()