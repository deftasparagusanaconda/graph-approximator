# this enables gapprox to represent partial solutions

class Truth(

class Boolean(Truth):
	# one of two values: {False, True}
	def __init__(self, value):
		self.value

class Polyboolean(Truth):
	# tuple of booleans. polybooleans allow for representing partial truths/partial solutions. for example, complex numbers may have one component equal but not the other. then that is a partial equality.
	def __init__(self, dimensionality:int, values[]):
		self.dimensionality = dimensionality


