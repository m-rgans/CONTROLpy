import preproc
import compileunit
import pathutils

from pathutils import FilePath
from compileunit import CompileUnit


objects:set[CompileUnit] = set()

for f in pathutils.allFiles:
    print(f)

for f in pathutils.allCompUnits:
    print(f)
    #objects.add(CompileUnit(f))
