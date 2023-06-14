import os

import mesg
import globals
import preproc
import compileunit
import pathutils
import subprocess

from pathutils import FilePath
from compileunit import CompileUnit

print("Operation: " + str(globals.OPERATION))

#linking phase

def clean():
    for f in pathutils.allCompUnits:
        os.remove(pathutils.BUILD_DIRECTORY + f.objName())

def build():

    if not os.path.exists(pathutils.BUILD_DIRECTORY):
        os.mkdir(pathutils.BUILD_DIRECTORY)

    objects:set[CompileUnit] = set[CompileUnit]()

    objectPaths:list[str] = []

    for f in pathutils.allCompUnits:
        objects.add(CompileUnit(f))
        objectPaths.append(str(f))

    for f in objects:
        mesg.info("Compiling:" + f.path.name, mesg.MessageClass.COMPILATION)
        if f.checkUpdated():
            x:int = f.compile()
            if x != 0:
                mesg.error("Program failed to compile.", mesg.MessageClass.COMPILATION)
                exit(2)
    
    #linking phase
    procArgs:list[str] = [globals.CPP_COMPILER]
    procArgs.extend(objectPaths)
    procArgs.extend(globals.LINKER_FLAGS)
    procArgs.append("-o" + globals.EXECUTABLE_NAME)
    proc = subprocess.run(procArgs)

    if proc.returncode != 0:
        mesg.error("Program failed to link.", mesg.MessageClass.COMPILATION)

def test():
    build()
    proc = subprocess.run(globals.BUILD_DIRECTORY + globals.EXECUTABLE_NAME)

from globals import OPERATION
from globals import OPERATION_ID

if OPERATION == OPERATION_ID.BUILD:
    build()
elif OPERATION == OPERATION_ID.CLEAN:
    clean()
elif OPERATION == OPERATION_ID.TEST:
    test()