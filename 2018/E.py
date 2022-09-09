import sys
class Calculator:
	storage = []
	def __init__(self, value):
		# variables
		value = value.split(" ")
		self.operation = [x.upper() for x in value if x.isalpha()][0]
		self.number = 0
		for i in value:
			if i.isdigit(): self.number = int(i)
			else: self.number = 0
			
		# conditions
		if self.operation == "P": self.addToStorage()
		elif self.operation == "A": self.addition()
		elif self.operation == "S": self.subtraction()
		elif self.operation == "M": self.multiplication()
		elif self.operation == "D": self.division()
		elif self.operation == "R": self.result()
		else: print("Entered input is wrong, please input again.")
		
	# methods
	def mutual_code(self):
		self.storage.pop()
		self.storage.pop()
		self.storage.append(self.result)
		
	def addToStorage(self):
		if self.number > 0:self.storage.append(self.number)
		else: return
		
	def addition(self):
		if len(self.storage) < 2: sys.exit("Error. Needs two operands.")
		self.result = self.storage[len(self.storage) -1] + self.storage[len(self.storage) -2]
		self.mutual_code()
		
	def subtraction(self):
		if len(self.storage) < 2: sys.exit("Error. Needs two operands.")
		self.result = self.storage[len(self.storage) -2] - self.storage[len(self.storage) -1]
		self.mutual_code()

	def multiplication(self):
		if len(self.storage) < 2: sys.exit("Error. Needs two operands.")
		self.result = self.storage[len(self.storage) -2] * self.storage[len(self.storage) -1]
		self.mutual_code()
	
	def division(self):
		if len(self.storage) < 2: sys.exit("Error. Needs two operands.")
		self.result = int(self.storage[len(self.storage) -2] / self.storage[len(self.storage) -1])
		self.mutual_code()
		
	def result(self):
		if len(self.storage) > 1: print("Error. More than two operands")
		elif len(self.storage) == 0: sys.exit("Error. No operands.")
		else:
			print(f"The Result Is: {self.storage[0]}")
			sys.exit()
		
while True:
	test = Calculator(input("-> ").upper())