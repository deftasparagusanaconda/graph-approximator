import graphapproximator.api as ga
"""
A = [	[3, 7, 1, 0],
	[6, 2, 4, 9],
	[8, 0, 5, 3],
	[1, 9, 2, 6]]

B = [	[4, 1, 3, 8],
	[7, 6, 2, 0],
	[5, 2, 9, 1],
	[0, 3, 6, 7]]
"""

# the following inputs shall be supported:
ga.input =  [3,7,1,0], [4,1,3,8]
ga.input = ([3,7,1,0], [4,1,3,8])
ga.input =  [1,2,3] ,([2,3,4] , [3,4,5] , [7,8,9])
ga.input = ([1,2,3] , [2,3,4] , [3,4,5]), [7,8,9]
ga.input = ([1,2,3] , [2,3,4]),([3,4,5] , [7,8,9])
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = # support for files
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = 
ga.input = "2x"		# same as 2*x
ga.input = "1/2x"	# same as (1/2)*x
ga.input = "x^2"	
ga.input = "x**2"	# same as x^2
ga.input = 
ga.input = 

# the following inputs shall show warnings:
ga.input = [3, 7, 1, 0]		# 1D array input will recommend x array assumption of [0, 1, 2, ...]
ga.input = [3, 7, 1, 0], [6, 2, 4, 9], [4, 1, 3, 8], [7, 6, 2, 0]	# no input/output distinction. user is shown correct format and given suggestions

ga.input = ([3, 7, 1, 0], [6, 2, 4, 9]), ([4, 1, 3, 8], [7, 6, 2, 0])

inputs = data[0]
outputs = data[1]

inputs need not be homogenous to outputs
inputs[n] and outputs[n] all need to have same length
inputs[n] or outputs[n] need not have the same data type (but should be warned anyway)
values in each input array need to have same type
values in each output array need to have same type

