import sys
from line_count import utilities


class LineCount:
	"""
		returns the number of lines of code in a python project directory
		:param file: - string file name representing the file full address
		:param flags: - a dictionary of conditions to note while reading the file
		:param flags.no_comments: - a flag to remove comments from the counting
		:param flags.no_docs: - a flag to remove documentation lines from the counting
		:param flags.exclude: - a list of folders to exclude while counting files
		:return int: number of lines in the code file
	"""
	def __init__(self, directory, flags={'no_comments':True, 'no_docs':True, 'exclude':['__pycache__']}):
		self.line_count = 0
		self.directory = directory
		self.flags = flags

	def count_lines(self):
		files_list = utilities.read_directory(self.directory, exclude=self.flags.get('exclude',[]))

		for file in files_list:
			self.line_count += utilities.count_lines(file, self.flags)

		return self.line_count


# lc = LineCount('C:/Users/Ajah Chukwuemeka/Desktop/2020/Python/line_count/line_count')
# print("number of lines in folder is", lc.count_lines())