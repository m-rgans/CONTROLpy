import compileunit
from compileunit import CompileUnit

import pathutils
from pathutils import FilePath

#todo: chain dependencies
def getDependencies(unit:FilePath) -> set[FilePath]:
	pool:set[FilePath] = set[FilePath]()

	def addToPool(unit:FilePath):
		nonlocal pool
		if len(pool) > 50 :
			return pool
		#Get not present dependencies
		newDeps = getDependenciesIndividual(unit).difference(pool)

		#Add them to the pool
		pool = pool.union(newDeps)

		#And process them
		for d in newDeps:
			addToPool(d)

	addToPool(unit)

	return pool

def getDependenciesIndividual(unit:FilePath) -> set():
	deps = set()
	f = open(str(unit), "r")

	comment:bool = False
	
	for line in f:
		tokens:list[str] = tokenizeString(line)

		if "/*" in tokens and not "*/" in tokens:
			comment = True
		elif "*/" in tokens and not "/*" in tokens:
			comment = False

		if len(tokens) < 2:
			continue
		if tokens[0] == "#include" and not tokens[1][0] == "<" and not comment:
			p :str = tokens[1][1:len(tokens[1])-1]
			fp = FilePath(p)
			deps.add(FilePath(p))

	return deps

def tokenizeString(line:str):
	WHITESPACE = (' ', '	', '\n', "")
	tokens:list[str] = []
	
	inQuote:bool = False
	token:str = ""

	for c in line:
		if c in WHITESPACE and not inQuote:
			tokens.append(token)
			token = ""
		else:
			token += c
		
		if c == "\"":
			inQuote = not inQuote
		
		if token == "//":
			break
	
	tokens.append(token)

	for t in tokens:
		if t in WHITESPACE:
			tokens.remove(t)

	return tokens

def dumpSet(s:set[FilePath]):
	for d in s:
		print(str(d))