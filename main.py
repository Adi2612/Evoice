import _festival



'''
Function: sayText
Parameters: 

text:String - contains the input text

'''
def sayText(text):
	return _festival._sayText(text)


'''
Function: execCommand
Parameters: 

cmd:String - contains the input command

'''
def execCommand(cmd):
	return _festival.execCommand(cmd)


def sayFile(filename):
	return _festival.sayFile(filename)


def setStretchFactor(f):
	return _festival.setStretchFactor(f)



