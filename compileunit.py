import subprocess

import preproc

import pathutils
from pathutils import FilePath

CPP_COMPILER = "g++"
C_COMPILER = "gcc"
COMPILER_FLAGS=["-g", "-Wall", "-Wextra"]
LINKER_FLAGS=["-lraylib"]

class CompileUnit:
	path:FilePath
	deps:list[str] = []

	def __init__(self, path:FilePath):
		self.path = path
		deps = preproc.getDependencies(self.path)

	def objname(self) -> str:
		pass

	def checkUpdated(self) -> bool:
		pass

	def compile(self) -> bool:
		print("COMPILING " + self.path.name + self.path.ext)
		procArgs = [CPP_COMPILER]
		procArgs.extend(COMPILER_FLAGS)
		procArgs.extend(LINKER_FLAGS)
		procArgs.append(str(self.path))
		proc = subprocess.Popen(procArgs)
		pass