import preproc
import compileunit
import pathutils

from pathutils import FilePath
from compileunit import CompileUnit


objects:set[CompileUnit] = set[CompileUnit]()

for f in pathutils.allCompUnits:
    # Fetch file
    print("Adding file " + str(f))
    objects.add(CompileUnit(f))

    # Check file for updates

    # If needs recompile, do that