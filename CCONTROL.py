
# IGNORE [filename] (or self)
# MACRO_IMPORT filename
# MACRO_INVOKE macname

class Command:
    NOP    = 0
    IGNORE = 1
    IMPORT = 2
    INVOKE = 3