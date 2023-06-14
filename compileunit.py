import os

import subprocess

import preproc
import mesg
import pathutils
from pathutils import FilePath

import globals

from globals import CPP_COMPILER
from globals import C98_COMPILER

from globals import C_FLAGS
from globals import CPP_FLAGS
from globals import C98_FLAGS

from globals import LINKER_FLAGS

from globals import POSIX_MAX_FILENAME_LENGTH

class CompileUnit:
	path:FilePath
	deps:list[FilePath] = []

	def __init__(self, path:FilePath):
		self.path = path
		deps = preproc.getDependencies(self.path)

	def objname(self) -> FilePath:
		return globals.BUILD_DIRECTORY + pathutils.hashFunc(str(self.path)) + ".o"
		p:str = str(self.path)
		p += ".o"

		if len(p) > POSIX_MAX_FILENAME_LENGTH:
			p = p[len(p) - POSIX_MAX_FILENAME_LENGTH:]

		p = p.replace("/",".")
		return FilePath(globals.BUILD_DIRECTORY + p)
		
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

	def compile(self) -> int:
		mesg.info("Compiling " + str(self.path), mesg.MessageClass.COMPILATION)
		procArgs:list[str] = []
		
		if self.path.ext == "cpp":
			procArgs.append(CPP_COMPILER)
			procArgs.extend(C_FLAGS)
			procArgs.extend(CPP_FLAGS)
		else:
			procArgs.extend(
				[
					C98_COMPILER,
					C_FLAGS,
					C98_FLAGS,
				]
			)

		#join the procs and deal with them, this is thread bad
		procArgs.append("-c")
		procArgs.append(str(self.path))
		procArgs.append("-o" + str(self.objname()))
		print(procArgs)
		proc = subprocess.run(procArgs)
		print("RESULT: " + str(proc.returncode))
		return proc.returncode