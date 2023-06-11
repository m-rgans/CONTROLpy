
class TerminalColor:
	NONE = ""
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class MessageClass:
	DEFAULT = ""
	GATHER = "Project Indexing"
	DEPENDENCY = "Dependencies"
	COMPILATION = "Compiler"
	MISC = "Miscellaneous"
	PREPROCESSOR = "Preprocessor"

def printColor(mesg:str, color:str, mclass = MessageClass.DEFAULT):
	if mclass != MessageClass.DEFAULT:
		mesg = color + '[' + TerminalColor.BOLD + mclass + TerminalColor.RESET + color + ']' + ' ' + mesg
	print(mesg + TerminalColor.RESET)

def error(mesg:str, mclass = MessageClass.DEFAULT):
	printColor(mesg, TerminalColor.FAIL, mclass)

def warn(mesg:str, mclass = MessageClass.DEFAULT):
	printColor(mesg, TerminalColor.WARNING, mclass)

def info(mesg:str, mclass = MessageClass.DEFAULT):
	printColor(mesg, TerminalColor.NONE, mclass)

def success(mesg:str, mclass = MessageClass.DEFAULT):
	printColor(mesg, TerminalColor.OKGREEN, mclass)
