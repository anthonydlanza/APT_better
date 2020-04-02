from decimal import Decimal
from itertools import permutations

# line ~~ the line number that will be printed out e.g. 00010
line = ""
# tens ~~ the line spacing that we want statement number
tens = 10
# n ~~ holding value for line spacing * 0.00001
tens_holder = 0

def addLine():
	# utilize variables from outside the scope of this function.
	global tens_holder
	global tens
	global line
	# zeros ~~ 
	zeros = ""
	# line_length ~~ number of digits in the line. for example, 00010 has 5 digits.
	line_length = 0
	# set n = to tens * .00001 (for example, if tens is 10, n = 0.0001)
	tens_holder = tens * .00001
	# add 2 to tens (for example, on the second implementation of addLine, tens = 12 and n = 0.00012)
	tens+=2
	# because n is a floating point number, we must recast it as a string.
	line = str(tens_holder)
	# using python slice, we cut off the first two characters of our string (for example, 0.0001 becomes 0001)
	line = line[2:]
	"""
	there's some math involved in this next section. 

	for every statement that ends in 0 or 0s, the line length
	will be <= 4, for example, using our python slice from earlier, line 10 will look like 0001 and
	line 100 will look like 001 and so on and so forth. 
	For every statement that ends in a real number, the length should be 5. For example, 16 will look like
	00016 and line 101 will look like 00101.

	With this in mind, if we have a line number that ends in 0, we must add a zero's to the end of the line 
	until the line length equals 5.
	"""
	line_length = len(line)
	if line_length > 5:
		line = line[:5]
		line_length = len(line)
	while(line_length < 5):
		zeros = zeros + "0"
		line_length = line_length + 1
	# Our new line will be equal to line (for example line 100 would be 001, plus the number of zeros we needed to add in order
	# to make line_length = 5. Therefore, our new line would be 00100)
	line = (str(line) + zeros)
	return str(line) 

# # The first 10 lines will serve as our Boiler Plate.
# for x in range(10):
# 	print(addLine() + "	C **** Code Built by Toast4PPCL // Plz no steal. ***\n")

# # The next 5 lines will be used to space out the code for readability.
# for x in range(5):
# 	print(addLine() + "	C *\n")

# # Declare creation of locals
# print(addLine() + "	C **** CREATE LOCAL POINTS FOR PROGRAM ****\n")
# print(addLine() + "	C *\n")
	
















