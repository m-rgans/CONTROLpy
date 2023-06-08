
import preproc

import pathutils
from pathutils import FilePath

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