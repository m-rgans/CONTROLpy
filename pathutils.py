import os

#print(allfiles)

class FilePath:
	root:str=""
	offset:str=""
	name:str =""
	ext:str = ""

	def __init__(self, path):
		self.root,self.offset,self.name,self.ext = FilePath.breakPath(path)
		pass

	def __str__(self) -> str:
		return self.root + self.offset + self.name + self.ext

	def __eq__(self, other) -> bool:
		return str(self) == str(other)
	
	def __hash__(self) -> int:
		return str(self).__hash__()

	def breakPath(p:str) -> tuple[str, str, str, str]:
		root:str   = ""
		offset:str = ""
		name:str   = ""
		ext:str    = ""

		curs:int = len(p)
		for c in p[::-1]:
			ext = c + ext
			curs -= 1
			if c == '.':
				curs -= 1
				break
			elif c == '/':
				curs = len(p)
				ext = ""
				break
			elif curs == 0:
				curs = len(p)
				ext = ""
				break
		
		for c in p[curs::-1]:
			if c == '/':
				break
			name = c + name
			curs -= 1
		
		root = p[0:curs]
		
		if p[0] != '/' and p[0] != '~':
			root = PROJECT_DIRECTORY + root

		return root, offset, name, ext

PROJECT_DIRECTORY = "/home/morgan/Desktop/CONTROLpy/TESTBENCH/"
allFiles = set[FilePath]()
allCompUnits = set[FilePath]()
IGNORED_FOLDERS = {
    ".git",
    "build"
}

for root,dirs,files in os.walk(PROJECT_DIRECTORY):
	ignored = False
	for ignDir in IGNORED_FOLDERS:
		if root.startswith(PROJECT_DIRECTORY + ignDir):
			ignored = True
			break
	
	if ignored:
		continue

	for f in files:
		allFiles.add(FilePath(PROJECT_DIRECTORY + root + f))

for f in allFiles:
	if f.ext == ".cpp" or f.ext == ".c":
		allCompUnits.add(f)
