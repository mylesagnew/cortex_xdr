import os
import sys

def run(path):
	path = os.path.expanduser(path)
	path = os.path.expandvars(path)
	if os.path.isabs(path):
		return os.path.exists(path)
	else:
		sys.stderr.write(f"Input path <{path}> not valid, must be an absolute path")

	return False