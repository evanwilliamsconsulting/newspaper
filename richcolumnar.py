""" Puts Verbage into Columns and Provides Index by Lines

"""

import re
from hyphenate import Hyphenator

__version__ = '1.0.20070709'

class RichColumnar:

    def __init__(self, verbage, columnSize):
        self.verbage = verbage 
	self.length = len(verbage)
	self.end = self.length
	self.start = 0
	self.current = 0
	self.lineid = 0
	self.lines = {}
	self.count = 0
	self.columnSize = columnSize 
	self.currentChar = ""
	self.currentWord = ""
	self.currentLine = ""
        f = open("/opt/development/newholland/press/products/Newspaper/en.dic","r")
        rae = f.read()
        f.close()
        mh = Hyphenator(rae)
	self.returnText(mh)
   
    def getLines(self):
	return self.lines

    def getCurrent(self):
	theResult=self.verbage[self.current]
        return theResult

    def next(self,statein):
	if self.current >= self.end-1:
	    return "END"
        else:
	    self.current += 1
	    self.count = self.current
	    return statein

    def wordClose(self):
	current = self.currentChar
	if current==' ' or current == '\t' or current=='\n':
	    return True
        else:
	    return False

    def setColumnSize(self,chars):
	self.columnSize = chars

    def getColumnSize(self):
	return self.columnSize

    def countLines(self):
	return self.lineid

    def getLines(self):
	return self.lines

    def setCountLines(self,theCount):
        self.count = theCount

    def returnLines(self):
	return self.lines

    def returnLine(self,i):
	return self.lines[i]

    def walk(self,statein):
	    self.currentWord+=self.getCurrent()
	    self.currentChar = self.getCurrent()
	    state=self.next(statein)
	    return state

    def columnFull(self):
	    if len(self.currentLine)+len(self.currentWord)>self.getColumnSize():
		return True
	    else:
		return False
    
    def getLineId(self):
	return self.lineid

    def getCurrentLine(self):
        return self.currentLine

    def returnText(self,mh):
        """
	Return the Verbage
	"""
	state = 'START'

	state = self.walk(state)
	trythis = ''
	j = 0
	k = 0
	lineid=0 
	print "verbage %s" % self.verbage
	while k<=len(self.verbage):
            if k==len(self.verbage):
                self.lines[lineid]=line.strip()
		print "lastline %s" % line
		self.lineid = lineid-1
	        return	
	    trythis+=self.verbage[k]
            k+=1
	    if j>self.columnSize or k>=len(self.verbage):
		l=0
                line=''
		word=''
		trylen=len(trythis)
                while l<=trylen:
                    word += trythis[l]
                    if trythis[l]==' ':
			hy = mh.hyphenate_word(word)
			print hy
			hylen = len(hy)
                       	new = hy[0]
			m = 1
			while m<=hylen:
 			    #new += '-'
			    new += hy[m] 
			    m += 1
                        line+=' '
			line+=new
			word=''
		    l+=1
		    #print "word: %s" % word
                line += trythis
		trythis=word
		yh = mh.hyphenate_word(word)
		if len(yh)>1:
                    j=len(yh[0])+1
		    line+=' '
		    line+=yh[0]
		    line+='-'
		    p = 1
		    remainder = ''
		    while p < len(yh):
			remainder+=yh[p]
			p+=1
		    j=len(remainder)
		    trythis=remainder
		else: 
                    j=len(trythis)
                self.lines[lineid]=line
		print "line %s" % line
		lineid += 1
            else:
                j+=1
