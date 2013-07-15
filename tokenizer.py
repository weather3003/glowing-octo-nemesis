#!/usr/bin/env python

import fileinput
import json

from sys import argv
from base64 import b64encode

USAGE = '''%s <list of files>'''

if __name__ == '__main__':
	if len(argv) != 2:
		print USAGE % argv[0]
		exit(1)
		
	bagOfWords = set()
	for line in fileinput.input():
		bagOfWords.update(set([b64encode(token) for token in line.split()]))
		
	print json.dumps(list(bagOfWords))
	
