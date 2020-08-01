import utilities

class LineCount:
	
	def __init__(self, directory, flags={'no_comments':True, 'no_docs':True, 'exclude':['__pycache__']}):
		self.line_count = 0
		self.directory = directory
		self.flags = flags

	def count_lines(self):
		files_list = utilities.read_directory(self.directory, exclude=self.flags.get('exclude',[]))

		for file in files_list:
			self.line_count += utilities.count_lines(file, self.flags)

		return self.line_count


lc = LineCount('C:/Users/Ajah Chukwuemeka/Desktop/2020/Python/line_count/line_count')
print("number of lines in folder is", lc.count_lines())