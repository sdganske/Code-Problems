 #/usr/bin/env python

#Problem 1. 
#Magic Square Verifer. Written in python 2.7.3 by S.Ganske.
#Standing alone, this will ask for a pontential magic square. If the 
#sqr_verifer is called within a larger function, it will assume that the
#input is a list or tuple(?) consisting of nine numbers. Might write a 
#safer version that checks first afterwards. and then a version that can
#accept magic squares of arbitrary size.

#V. 0.0.1
#Finished first version of stand alone framework.
 
#Module Imports

#Function Declarations
def sqr_verifer(magic_square):
	#A proper 3X3 magic square has nine unique numbers that all sum to 
	#the same number. So the first test should be uniqueness...
	
	#After that, are the sums. it would be easier to sum everything with
	# a two dimensional grid.
	
	#test rows
	
	#test columns
	
	#test diagonals
	 
	#output the sum. if this isn't a magic square, then the tests will
	#break and return false.
	#This is just here so I can test the stand alone function.
	sqr_sum = False
	return sqr_sum

#Will go back and add code to verify that the input is nine numbers.	
def magic_str_converter(magic_string):
	magic_square = magic_string.split()
	return magic_square
	
def stand_alone():
	print("Enter your magic square, starting from the top and left,"+
	"finishing at the bottom right, and with each of the numbers"+
	"separated by a space:")
	magic_string = raw_input()
	magic_square = magic_str_converter(magic_string)
	is_magic_square = sqr_verifer(magic_square)
	
	if is_magic_square == False:
		print ("Sorry, this isn't a magic square...")
	else:
		#Need a more elegent way of displaying magic squares... 
		print("This Magic square, composed of: \n" + 
		str(magic_square[0]) + " " + str(magic_square[1]) + " " + str(magic_square[2]) + "\n" + 
		str(magic_square[3]) + " " + str(magic_square[4]) + " " + str(magic_square[5]) + "\n" +
		str(magic_square[6]) + " " + str(magic_square[7]) + " " + str(magic_square[8]) +
		"\nHas a sum of: " + str(is_magic_square))
		

#Main body
if __name__ == '__main__':
	stand_alone()

