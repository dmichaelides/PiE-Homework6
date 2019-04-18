"""
'Python-is-Easy' Homework #6 (Advanced Loops)
DESCRIPTION: 
The main goal of this file created, is to get acquianted with Loops in Python.  It is the sixth homework assigment in the
'Python is Easy' course, from Pirple.


The code below includes a function where parameter for rows and columns are defined, which in turn would print a chess board on the terminal you run the application on.

Function is: MakeChessBoard(rows,column).

See below an example of a single 'unit' for a ROW or COLUMN in this chessboard, which is basically a series of one of the two shapes defined as variables.

Example of one unit in a ROW or COLUMN:
|||||
|||||
|||||

"""

shape = "|"
shape2 = "."

# First is a series of 4 'sub-functions', which will be used within the main function which will print the chessboard. 

# This function prints one of the shapes, to form the first line in the unit of the character 'shape'. It is used for all units in the chessboard EXCEPT the last one in the row from left to right. 
def ContBuildFill():
	for row in range(1):
		for col in range(1,6):
			print(shape,end="")

# This function prints one of the shapes, to form the first line in the unit of the character 'shape2'. It is used for all units in the chessboard EXCEPT the last one in the row from left to right. 
def ContBuildNoFill():
	for row in range(1):
		for col in range(1,6):
			print(shape2,end="")

# This function prints one of the shapes, to form the first line in the unit of the character 'shape', for ONLY the last unit on the row. 
def EndBuildFill():
	for row in range(1):
		for col in range(1,6):
			if col == 5:
				print(shape)
			else:
				print(shape,end="")

# This function prints one of the shapes, to form the first line in the unit of the character 'shape2', for ONLY the last unit on the row. 
def EndBuildNoFill():
	for row in range(1):
		for col in range(1,6):
			if col == 5:
				print(shape2)
			else:
				print(shape2,end="")

# This is the function that draws the chessboard. 
def MakeChessBoard(rows,column):
	for outrow in range(rows):
		for inrow in range(3):
			for outcol in range(column):
				if outcol == column-1:
					if column%2 > 0:
						if outrow%2 == 0:
							EndBuildFill()
						else:
							EndBuildNoFill()
						continue
					if outrow%2 == 0:
						EndBuildNoFill()
					else:
						EndBuildFill()
					continue
				if outrow%2 == outcol%2:
					ContBuildFill()
				else:
					ContBuildNoFill()
	return True

MakeChessBoard(3,3)



# all the code below was draft work progress, to get to the final point of the code above. 

'''
 let's try print a chess board!!



#####     #####     #####      0
#####     #####     #####      1	0			
#####     #####     #####      2
     #####     #####     ##### 0
     #####     #####     ##### 1    1
     #####     #####     ##### 2
#####     #####     #####      0
#####     #####     #####      1	2			
#####     #####     #####      2
     #####     #####     ##### 0
     #####     #####     ##### 1    3 
     #####     #####     ##### 2
#####     #####     #####      0
#####     #####     #####      1	4			
#####     #####     #####      2 
     #####     #####     ##### 0
     #####     #####     ##### 1    5
     #####     #####     ##### 2
123451234512345123451234512345
 0    1    2    3    4    5     


         

#####      0
#####      1
#####      2
     ##### 0
     ##### 1
     ##### 2
1234512345


##### 0
##### 1
##### 2
12345
      0
      1
      2
12345

'''


### below works for the larger fixed chess board.

# def MakeChessBoard(rows,column):
# 	for outrow in range(rows):
# 		for midrow in range(1,3):
# 			for inrow in range(3):
# 				for outcol in range(column):
# 					for midcol in range(1,3):
# 						for incol in range(1,6):
# 							if outcol == column-1 and midcol == 2 and incol == 5:
# 								if midrow == 1:
# 									print(" ")
# 								else:
# 									print(shape)
# 								continue
# 							if midrow == midcol:
# 								print(shape,end="")
# 							else:
# 								print(" ",end="")
# 	return True


# def MakeChessBoard(rows,column):
# 	for outrow in range(rows):
# 		for midrow in range(1,3):
# 			for inrow in range(3):
# 				for outcol in range(column):
# 					for midcol in range(1,3):
# 						if outcol == column-1 and midcol == 2:
# 							if midrow == 1:
# 								EndBuildNoFill()
# 							else:
# 								EndBuildFill()
# 							continue
# 						if midrow == midcol:
# 							ContBuildFill()
# 						else:
# 							ContBuildNoFill()
# 	return True




# def MakeChessBoardODD(rows,column):
# 	for outrow in range(rows):
# 		for midrow in range(1,3):
# 			for inrow in range(3):
# 				for outcol in range(column):
# 					for midcol in range(1,3):
# 						for incol in range(1,6):
# 							if outcol == 2 and midcol == 2 and incol == 5:
# 								if midrow == 1:
# 									print(" ")
# 								else:
# 									print(shape)
# 								continue
# 							if midrow == midcol:
# 								print(shape,end="")
# 							else:
# 								print(" ",end="")
# 	return True



# for outrow in range(3):
# 	for midrow in range(1,3):
# 		for inrow in range(3):
# 			for outcol in range(3):
# 				for midcol in range(1,3):
# 					for incol in range(1,6):
# 						if outcol == 2 and midcol == 2 and incol == 5:
# 							if midrow == 1:
# 								print(" ")
# 							else:
# 								print(shape)
# 							continue
# 						if midrow == midcol:
# 							print(shape,end="")
# 						else:
# 							print(" ",end="")
