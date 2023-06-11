import os

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

		#print(directory + "%" + name + "%" + ext)

		return directory, name, ext

PROJECT_DIRECTORY = "/mnt/ARCHIVAL/BUP2/code/python/CONTROLpy/TESTBENCH"
PROJECT_DIRECTORY = os.path.abspath(PROJECT_DIRECTORY)

os.chdir(PROJECT_DIRECTORY)

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
		print("[All files] Adding "+ root + "/" + f)
		allFiles.add(FilePath(root + "/" + f))

for f in allFiles:
	if f.ext == "cpp" or f.ext == "c":
		print("[Compilation Units] Adding " + str(f))
		allCompUnits.add(f)
