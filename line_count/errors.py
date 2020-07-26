class FileNotSupportedError(Exception):
	""" Error class for file types not supported yet

	"""

	def __init__(self, message, file):
		super().__init__(message)
		self.message = message
		self.file = file 