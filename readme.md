# Line count

A utility package to enable developers count the actual number of lines of code they have written for a project.

# Installation
`
pip install line_count
`

`
easy_install line_count
`

# Usage
```bash
	python -m line_count --no_docs False --no_comments True --directory line_count --exclude .git __pycache__
```

# Internals

It defaults to the directory of call if no directory argument is provided. 
Defaults to True for no_docs and no_comments flags
Defaults to empty list for exclude parameter

## Todo
* Fix the need for command line arguments to be in a specific position
* Tests 

