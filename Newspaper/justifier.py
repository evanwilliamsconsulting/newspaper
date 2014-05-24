""" Puts Verbage into Columns and Provides Index by Lines

"""

__version__ = '1.0.20070709'

class Justifier:

    def __init__(self, verbage, width):
        self.verbage = verbage 
	self.width = width
	self.words = self.verbage.split()
	# get to work start counting
	self.numWords = len(self.words)
	self.lenChars = float(0)
	for word in self.words:
	    # add up the length of the characters
	    self.lenChars += len(word)
	self.lenChars = self.lenChars * 7
	self.totalWidth = float(self.width)

    def wordSpace(self):
	# Total Line Width = Length of Chars in Words + Total Length of WhiteSpace
	# Total Length of whitespace = Total Line Width - Length of Chars in Words
	totalWhitespace = float(self.totalWidth - self.lenChars)
	# Word Space is divided by number of spaces or total words less one
	if self.numWords <= 1:
	    wordSpace = 5
	else:
	    numberOfSpaces = float( self.numWords - 1)
	    wordSpace = int(totalWhitespace / numberOfSpaces)
	return wordSpace

    def getCharMultiplier(self,char):
	mul= float(0)
	if char=='a':
		mul = 1
	elif char=='b':
		mul = 1
	elif char=='c':
		mul = 1
	elif char=='d':
		mul = 1
	elif char=='e':
		mul = 1
	elif char=='f':
		mul = 1
	elif char=='g':
		mul = 1
	elif char=='h':
		mul = 1
	elif char=='i':
		mul = 1
	elif char=='j':
		mul = 1
	elif char=='k':
		mul = 1
	elif char=='l':
		mul = 1
	elif char=='m':
		mul = 1
	elif char=='n':
		mul = 1
	elif char=='o':
		mul = 1
	elif char=='p':
		mul = 1
	elif char=='q':
		mul = 1
	elif char=='r':
		mul = 1
	elif char=='s':
		mul = 1
	elif char=='t':
		mul = 1
	elif char=='u':
		mul = 1
	elif char=='v':
		mul = 1
	elif char=='w':
		mul = 1
	elif char=='x':
		mul = 1
	elif char=='y':
		mul = 1
	elif char=='A':
		mul = 1.2
	elif char=='B':
		mul = 1.2
	elif char=='C':
		mul = 1.2
	elif char=='D':
		mul = 1.2
	elif char=='E':
		mul = 1.2
	elif char=='F':
		mul = 1.2
	elif char=='G':
		mul = 1.2
	elif char=='H':
		mul = 1.2
	elif char=='I':
		mul = 1.2
	elif char=='J':
		mul = 1.2
	elif char=='K':
		mul = 1.2
	elif char=='L':
		mul = 1.2
	elif char=='M':
		mul = 1.2
	elif char=='N':
		mul = 1.2
	elif char=='O':
		mul = 1.2
	elif char=='P':
		mul = 1.2
	elif char=='Q':
		mul = 1.2
	elif char=='R':
		mul = 1.2
	elif char=='S':
		mul = 1.2
	elif char=='T':
		mul = 1.2
	elif char=='U':
		mul = 1.2
	elif char=='V':
		mul = 1.2
	elif char=='W':
		mul = 1.2
	elif char=='X':
		mul = 1.2
	elif char=='Y':
		mul = 1.2
	elif char=='Z':
		mul = 1.2
	elif char=='0':
		mul = 1.2
	elif char=='1':
		mul = 1.1
	elif char=='2':
		mul = 1.1
	elif char=='3':
		mul = 1.1
	elif char=='4':
		mul = 1.1
	elif char=='5':
		mul = 1.1
	elif char=='6':
		mul = 1.1
	elif char=='7':
		mul = 1.1
	elif char=='8':
		mul = 1.1
	elif char=='9':
		mul = 1.1
	else:
		mul = 1
	return mul
