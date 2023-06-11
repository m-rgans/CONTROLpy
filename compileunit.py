import os

import subprocess

import preproc

import pathutils
from pathutils import FilePath

CPP_COMPILER = "g++"
C_COMPILER = "gcc"
COMPILER_FLAGS=["-g", "-Wall", "-Wextra"]
LINKER_FLAGS=["-lraylib"]

POSIX_MAX_FILENAME_LENGTH:int = 255

class CompileUnit:
	path:FilePath
	deps:list[FilePath] = []

	def __init__(self, path:FilePath):
		self.path = path
		deps = preproc.getDependencies(self.path)

	def objname(self) -> FilePath:
		p:str = str(self.path)
		p += ".o"

		if len(p) > POSIX_MAX_FILENAME_LENGTH:
			p = p[len(p) - POSIX_MAX_FILENAME_LENGTH:]

		p = p.replace("/",".")
		return FilePath("build/" + p)
		
	def checkUpdated(self) -> bool:
		p:FilePath = self.objname()
		#first, check if it exists
		if not os.path.exists(str(p)):
			return True
		
		objTime = os.path.getmtime(str(p))
		srcTime = os.path.getmtime(str(self.path))

		for d in self.deps:
			dTime = os.path.getmtime(str(d.path))
			if dTime > srcTime:
				srcTime = dTime

		return srcTime > objTime

	def compile(self) -> bool:
		print("COMPILING " + self.path.name + self.path.ext)
		procArgs = [CPP_COMPILER, "-c"]
		procArgs.extend(COMPILER_FLAGS)
		procArgs.extend(LINKER_FLAGS)
		procArgs.append(str(self.path))
		procArgs.append("-o" + str(self.objname()))
		proc = subprocess.Popen(procArgs)
		pass