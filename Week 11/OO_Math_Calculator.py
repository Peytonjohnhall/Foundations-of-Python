# -----------------------------------------------
# Programmer : Peyton John Hall
# Date : 04/21/2026
# Description: A class with mathematical methods
# built for object-oriented programming practice
# -----------------------------------------------

class MyAwesomeMath:
	def __init__(self, firstNumber, secondNumber): # "__init__" is a method
		""" 
		__init__ is employed in Python for the purpose of object-oriented
		initialization, whereby the objects, in this case, firstNumber and 
		secondNumber, shall be directed to a memory storage location when 
		the user furnishes the values they point to as input.
		"""
		self.firstNumber = firstNumber # firstNumber is an attribute object
		self.secondNumber = secondNumber # secondNumber is an attribute object

	def Operations(self): # "Operations" is a method/ function
		"""
		The syntax in each nested function reads as follows:
		Object = self.firstNumber (either + or - or * or /) self.secondNumber

		Herein, "self" denotes the instance of the class object itself, 
		"MyAwesomeMath," by which each method gains access to those, belonging
		to the class, attributes, viz. firstNumber and secondNumber, which 
		were established and bound to the instance at the time of its 
		initialization. The class is the cookie cutter; the instance, or, self,
		which is the object, is the cookie, according to the analogy of 
		Professor Ali Naqvi. In the same way that, for example, the class 
		"list" uses a period (.) to point to its built-in methods like 
		"append()" or "remove()," "self" is a reference to its class, 
		"MyAwesomeMath," and what belongs to that class object, are its 
		attributes limited to how many are defined by the programmer.
		"""
		def Addition():
			Summa = self.firstNumber + self.secondNumber
			return Summa # Latin spelling
		def Subtraction():
			Differentia = self.firstNumber - self.secondNumber
			return Differentia # Latin spelling
		def Multiplication():
			Productum = self.firstNumber * self.secondNumber
			return Productum # Latin spelling
		def Division():
			Quotiens = self.firstNumber / self.secondNumber
			return Quotiens # Latin spelling
		Results = Addition(), Subtraction(), Multiplication(), Division()
		# print(type(Results))
		return Results

class Main: # not case sensitive like it would be in Java, C, C#, or C++
	def Main(): # "Main" is the main method/ function
		"""
		When programming with classes and objects, the practice generally
		considered good is to create a main method in a class, "Main." This 
		concept is inherited from programming languages like Java, C, C#, 
		and C++. It separates the program's entry point from its implementation 
		logic, a sepatation which ensures code is run only when explicitly 
		invoked, i.e. called upon, to avoid an unwanted output.
		"""
		first = float(input("Enter first number: "))
		second = float(input("Enter second number: "))
		calculation = MyAwesomeMath(first, second)
		Summa, Differentia, Productum, Quotiens = calculation.Operations()
		while True:
			print("1. ADDITION")
			print("2. SUBTRACTION")
			print("3. MULTIPLICATION")
			print("4. DIVISION")
			choice = input("Enter your choice: ")
			if choice == "1":
				print(Summa)
			if choice == "2":
				print(Differentia)
			if choice == "3":
				print(Productum)
			if choice == "4":
				print(Quotiens)
			if choice not in ["1", "2", "3", "4"]:
				print("Invalid input. Select either " +
					  "\"1,\" \"2,\" \"3,\" or \"4.\"", sep = "")
			break

if __name__ == "__main__":
	Main.Main()