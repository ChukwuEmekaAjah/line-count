import sys
import line_count

flags = {
	'no_docs': True,
	'no_comments': True,
	'exclude': []
}

arguments = sys.argv

arguments_counter = 0

no_docs_flag = None 
no_comments_flag = None
exclude_flag = None
directory = None
try:
	no_docs_flag = arguments.index('--no_docs')
	no_comments_flag = arguments.index('--no_comments')
	exclude_flag = arguments.index('--exclude')
	directory_flag = arguments.index('--directory')
except ValueError as exc:
	pass

if no_docs_flag is not None and (no_docs_flag+1) < len(arguments):
	if arguments[no_docs_flag+1] == 'False':
		flags['no_docs'] = False

if no_comments_flag is not None and (no_comments_flag+1) < len(arguments):
	if arguments[no_comments_flag+1] == 'False':
		flags['no_comments'] = False

if directory_flag is not None and (directory_flag+1) < len(arguments):
	directory = arguments[directory_flag+1]

if exclude_flag is not None and (exclude_flag+1) < len(arguments):
	flags['exclude'] = arguments[exclude_flag+1:]

lc = line_count.LineCount(directory or '.', flags=flags)
print("total number of lines in directory is: ", lc.count_lines())
