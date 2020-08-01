import os
def read_directory(directory, files=[]):
	""" a function that reads a directory and returns all the files in it

	"""
	files_list = files
	try:
		directory_files = os.listdir(directory)
	except Exception as exc:
		return files_list
	else:
		for file in directory_files:
			if os.path.isfile(f'{directory}/{file}'):
				files_list.append(f'{directory}/{file}')
			else:
				read_directory(f'{directory}/{file}', files_list)

	return  files_list

print(read_directory('C:/Users/Ajah Chukwuemeka/Desktop/2020/Python/line_count/line_count', []))