# the heart of the project
# when you do `import graphapproximator as ga`, ga is automatically replaced by an instance of API
# the instance manages your current configuration of generator, expression, interpolator, ...
# the instance also exposes a list of available modules (generators, expressions, interpolators, ...)

from . import converter, analyzers, expressions, outliers, plotters
from .utils import StatefulFunction
from .optimizer.optimizer import Optimizer
from .optimizer import strategies

# ga.generator = ga.generators.dct already works
# but i want ga.generator.<tab> to show dct's arguments
	# this can be done by setting __dir__
# and also to let ga.generator.dct_type = 3 to set the argument
	# this can be done by overriding __setattr__
# and also to let the approximator use the generator with those arguments
	# this can be done by a wrapper with a modified __call__

# youll also have to capture the `ga.generator = something` assignment to change the ComponentWrapper's component
# i think that has to be implemented *inside* API
	
class api():
	_stateful_components:list[str] = ["interpolator", "analyzer", "expression"]
	
	# expose modules through the class instance
	analyzers = analyzers
	optimizers = strategies
	expressions = expressions
	outliers = outliers
	plotters = plotters
	converter = converter
	plotters = plotters
	"""
	# store configuration
	def __init__(self):
		_warn:bool = True		# show warnings
		_multithread:bool = True	# use n threads for n outputs
		super().__setattr__("optimizer", Optimizer())	# because its checked by __setattr__
		super().__setattr__("interpolator", None)
		super().__setattr__("analyzer", None)
		super().__setattr__("expression", None)

		self.input = None
		self.output = None
	"""	

	def __init__(self):
		analyzer = None
		expression = None
		
		input = None
		output = None

		_check_input:bool = True	# check input signature
		_multithread:bool = True	# use n threads for n outputs
	
	reset = __init__	# ga.reset() now resets the instance
	
	def __setattr__(self, name, value):
		#if name in self._stateful_components:
		#	if value is not None:
		#		name = StatefulFunction(value)
		#	else:
		#		name = None
		if name == "optimizer":
			super().__setattr("optimizer.strategy", value)

		elif name == "input" and self._warn:
			super().__setattr__(name, value)
			if utils.warn_input(self.input):
				print(f"{utils.Colours.BRIGHT_BLACK}disable check{utils.Colours.RESET}\t: ga._check_input = False\n")

		else:
			super().__setattr__(name, value)
	
	#def __getattr__(self, name):
	#	print("__getattr__", self, name)

#	def __getattr__(self, name):
#		if name in self._params:
#			return self._params[name]
#		raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
		
#	def __dir__(self):
#		

	# THE PIPELINE!!!! -----------------------------------------------------
	def approximate(self, input=None):
		# input=None is kept for convenience-sake because
		# ga.approximate(something) is easier than
		# ga.input = something; ga.approximate()
		"""calculate an approximation with the configuration given"""
		print("press ctrl+c to abort")
		if input is not None:
			self.input = input
		temp = self.input


		if self.analyzer:
			temp = self.analyzer(temp)
		#if self.optimizer.strategy:
		#	temp = self.optimizer(self, temp, self.input, self.expression)
		if self.expression:	# params to any
			temp = self.expression(temp)
		self.output = temp
		return temps
	# the end ~w~ ----------------------------------------------------------

	__call__ = approximate	# ga() and ga.approximate() are now same
	
	# provided for convenience, so you can do ga.line(something)
	@staticmethod
	def line(input, output_type="string"):
		"""least squares line approximation (https://en.wikipedia.org/wiki/Linear_least_squares)
provided for convenience"""
		return expressions.polynomial(analyzers.line.least_squares(input), number_of_points=len(input), output_type=output_type)
	
	@staticmethod
	def plot(self):
               plotters.plotter(self.input, self.output)

	def show(self):
		"""print current configuration"""
		print("input =", self.input)
		print("analyzer =", self.analyzer)
		#print("optimizer =", self.optimizer.strategy)
		print("expression =", self.expression)
		print("output =", self.output)
	
	def show_full(self):
		"""print current configuration + ALL sub-configurations"""
		self.show()
		print()
		print("optimizer:")
		self.optimizer.show_full()

	# basically what you see when you do `print(ga)` in the python interpreter
	def __repr__(self):
		return f"<API instance & module 'graphapproximator' at {hex(id(self))}>"
		
	def new(self):			# foo = ga.new() creates new instance
		"""return a new instance of Engine"""
		return type(self)()
	
	def copy(self):			# foo = ga.copy() creates a copy
		"""returns a copy of the current Engine instance"""
		from copy import deepcopy
		return deepcopy(self)

# ideally, API should not have any static methods
