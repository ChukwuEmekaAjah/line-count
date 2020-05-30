def count_lines(file, flags = {}):
	"""
		returns the number of lines of code in a python file
		:param file: - string file name representing the file full address
		:param flags: - a dictionary of conditions to note while reading the file
		:param flags.no_comments: - a flag to remove comments from the counting
		:param flags.no_docs: - a flag to remove documentation lines from the counting
		:return int: number of lines in the code file
	"""
	number_of_lines = 0

	try:
		file_object = open(file, 'r')
	except IOError as err:
		print(err)
		return 0
	except Exception as exc:
		print(exc)
		return 0
	else:
		file_lines = file_object.readlines()
		file_lines = list(filter(is_not_empty, file_lines))

		if flags and bool(flags.get('no_comments')) is True:
			# remove code comments from the code lines count
			file_lines = list(filter(is_not_comment, file_lines))
			print("number of lines is ", len(file_lines))

		if flags and bool(flags.get('no_docs')) is True:
			# remove function and class documentation string
			file_lines = remove_docs(file_lines)
			print("number of lines after removing docs", len(file_lines))
		
		number_of_lines = len(file_lines)
		return number_of_lines

def is_not_empty(file_line):
	"""
		returns True if a file is not empty otherwise False
		:param file_line: a string of characters representing a line in a file
		:return bool
	"""
	stripped_line = file_line.strip()
	if bool(stripped_line) is False:
		return False

	return True

def is_not_comment(file_line):
	"""
		returns True if the file line is not a comment otherwise False
		:param file_line: a string of characters representing a line in a file
		:return bool
	"""
	stripped_line = file_line.strip()
	if stripped_line.startswith("#"):
		return False

	return True

def remove_docs(file_lines):
	'''
		returns a list of file lines without docstrings
		:param file_lines: a list of strings representing a line in a file
		:return list: a list of strings representing lines in the list that are not documentation text
	'''
	doc_start_line = []
	doc_end_line = []

	for line_number, line in enumerate(file_lines):
		stripped_line = line.strip()
		# check for double quotes version
		if len(doc_start_line) > len(doc_end_line) and (stripped_line.startswith('"""') or stripped_line.endswith('"""')):
			if line_number != doc_start_line[-1] :
				doc_end_line.append(line_number)
		elif stripped_line.startswith('"""'):
			doc_start_line.append(line_number)
		
		#check for single quotes version
		if len(doc_start_line) > len(doc_end_line) and (stripped_line.startswith("'''") or stripped_line.endswith("'''")):
			if line_number != doc_start_line[-1]:
				doc_end_line.append(line_number)
		elif stripped_line.startswith("'''"):
			doc_start_line.append(line_number)

	file_without_docs = []

	for i in range(len(doc_start_line)):
		if i == 0:
			file_without_docs.extend(file_lines[0:doc_start_line[i]])
		if i < (len(doc_start_line) - 1):
			file_without_docs.extend(file_lines[doc_end_line[i]+1:doc_start_line[i+1]])
		else:
			file_without_docs.extend(file_lines[doc_end_line[len(doc_start_line) - 1]+1:])

	return file_without_docs	

count_lines("count.py", {"no_docs":True, "no_comments":True})