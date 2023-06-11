import os

import preproc
import compileunit
import pathutils

from pathutils import FilePath
from compileunit import CompileUnit

objects:set[CompileUnit] = set[CompileUnit]()

if not os.path.exists(pathutils.BUILD_DIRECTORY):
    os.mkdir(pathutils.BUILD_DIRECTORY)

for f in pathutils.allCompUnits:
    # Fetch file
    print("Adding file " + str(f))
    obj = CompileUnit(f)

    # Check file for updates
    if obj.checkUpdated():
        #obj.compile()
        pass



#linking phase