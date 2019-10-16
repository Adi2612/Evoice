import _festival



'''
API for saying a text


'''
def sayText(text):
	return _festival._sayText(text)

def execCommand(cmd):
	return _festival.execCommand(cmd)


def sayFile(filename):
	return _festival.sayFile(filename)


def setStretchFactor(f):
	return _festival.setStretchFactor(f)



