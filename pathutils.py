import os
import mesg

class FilePath:
	dir:str = ""
	name:str =""
	ext:str = ""

	def __init__(self, path):
		self.dir,self.name,self.ext = FilePath.breakPath(path)
		pass

	def __str__(self) -> str:
		if not self.ext == "":
			return self.dir + self.name + '.' + self.ext
		else:
			return self.dir + self.name

	def __eq__(self, other) -> bool:
		return str(self) == str(other)
	
	def __hash__(self) -> int:
		return str(self).__hash__()

# Starts with tilde -> prefix with home directory
# Starts with '.'
# Starts with characters (prefix with '.')

	def breakPath(p:str) -> tuple[str, str, str]:

		p = os.path.abspath(p)

		directory:str = ""
		name:str   = ""
		ext:str    = ""

		dotFound:bool = False
		baseName = os.path.basename(p)

		if '.' in baseName:
			for c in baseName[::-1]:
				if c == '.':
					dotFound = True
					continue
				elif dotFound:
					name = c + name
				elif not dotFound:
					ext = c + ext
		else:
			name = baseName

		directory = os.path.dirname(p) + '/'

		return directory, name, ext

import globals
from globals import PROJECT_DIRECTORY
from globals import BUILD_DIRECTORY
from globals import IGNORED_FOLDERS

os.chdir(PROJECT_DIRECTORY)

allFiles = set[FilePath]()
allCompUnits = set[FilePath]()

for root,dirs,files in os.walk(PROJECT_DIRECTORY):
	ignored = False
	for ignDir in IGNORED_FOLDERS:
		if ignDir in root:
			ignored = True
			break
	
	if ignored:
		continue

	for f in files:
		mesg.info("Adding " + root + "/" + f, mesg.MessageClass.GATHER)
		allFiles.add(FilePath(root + "/" + f))

for f in allFiles:
	if f.ext == "cpp" or f.ext == "c":
		mesg.info("Adding " + str(f), mesg.MessageClass.GATHER)
		allCompUnits.add(f)

import hashlib


def hashFunc(s:str) -> str:
	h = hashlib.sha256(usedforsecurity=False)
	h.update(s)
	return str(h.digest())