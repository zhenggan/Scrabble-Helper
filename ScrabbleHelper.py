import sys

"""
An object used to cheat in Scrabble, 
"""
class ScrabbleHelper:

	"""
	:brief initializes instance of this class
	"""
	def __init__(self):
		# open file to read
		with open("SOWPODS.txt", "r") as file:
			self.allWords = file.read().splitlines()
			
	"""
	:brief Returns valid words and their scores given the user's rack
	:param userRack the rack that the user currently has
	:return validRack whether the user's rack is valid
	:return answers the answers and their scores
	"""
	def processRack(self, userRack):
	
		# empty list to hold the return values
		returnValues = []
		
		# since the score is stored in uppercase letters
		# the rack the the user entered must also be converted
		userRack = userRack.upper()
		
		# Check rack is valid
		validRack = self.checkValidArg(userRack)
		
		answers = []
		
		# If rack is valid, get possible answers
		if validRack == True:
			answers = self.getAnswers(userRack)
		
		returnValues.append(validRack)
		returnValues.append(answers)
		return returnValues
		
	"""
	:brief checks whether the user's rack is valid
	:param userRack the rack that the user currently has
	:return true if user's rack is valid, false if not
	"""
	def checkValidArg(self, userRack):
	
		# if rack is all letters, it is valid
		if userRack.isalpha() == False:
			return False
		else:
			return True
			
	"""
	:brief gets the answers and scores given the user's current rack
	:param userRack the rack the the user currently has
	:return answers dictionary containing all valid answers and thir score
	"""
	def getAnswers(self, userRack):
		answers = []
		
		# loops through all words
		for word in self.allWords:
			validWord = True
			rackList = list(userRack)
			
			# check each letter in every word
			for letter in word:
				if letter not in rackList:
					validWord = False
					break
				else:
					rackList.remove(letter)
					
			# If the word is valid for that rack,
			# calculate score for that word
			if validWord == True:
				score = 0
				for letter in word:
					score = score + self.scores[letter]
				answers.append([score, word])	
		return answers
		
	# score for each corresponding letter
	scores = {"A": 1, "B": 3, "C": 3, "D": 1, "E": 2, "F": 2,
         "G": 4, "H": 1, "I": 4, "J": 5, "K": 8, "L": 3,
         "M": 1, "N": 1, "O": 1, "P": 10, "Q": 3, "R": 1,
         "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 4,
         "Y": 8, "Z": 10}
		 
	# list to score all words in SOWPODS dictionary
	allWords = []

# Creates an instance of ScrabbleHelper class
scrabbleHelper = ScrabbleHelper()

while True:
	userRack = input("Enter your current rack")
	processResults = scrabbleHelper.processRack(userRack)
	
	# If ran successful, returns the answers
	if processResults[0] == True:
		print (processResults[1])
	elif processResults[0] == False:
		print("Invalid input")

