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
	#self.lines = {}
	self.lines = []
	self.count = 0
	self.columnSize = columnSize 
	self.currentChar = ""
	self.currentWord = ""
	self.currentLine = ""
        f = open("/opt/newhol/press/products/Newspaper/en.dic","r")
        rae = f.read()
        f.close()
        mh = Hyphenator(rae)
	self.returnText(mh)
   
    def getLines(self):
	return self.lines

    def getCurrent(self):
	theResult = ""
	if self.current < self.end:
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
	if current == ',' or current==' ' or current == '\t' or current=='\n':
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

    def deleteLines(self):
        del self.lines

    def walk(self,statein):
	    self.currentWord+=self.getCurrent()
	    self.currentChar = self.getCurrent()
	    state=self.next(statein)
	    return state

    def columnFull(self):
	    if len(self.currentLine)+len(self.currentWord)>self.getColumnSize()-5:
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
	trythis = self.verbage
	trylen = len(self.verbage)
        l = 0
	# j is the number of characters in the line.
        j = 0
	word=''
	w = 0
	line=''
	lineid=0
	hy = []
        while l<trylen:
	    if j+w>self.columnSize:
	    #if j+w>self.columnSize-3:
		self.lines.append(line)
		lineid+=1
                line=''
		j=0
            word += trythis[l]
            if trythis[l]==' ':
		# does word already contain a hyphen?
		ishy = word.find("-")
		if ishy>=0: 
		    firstword = word[0:ishy]
		    secondword = word[ishy+1:len(word)]
		    hy = [firstword,'-',secondword]
                else:
	            hy = mh.hyphenate_word(word)
		hylen = len(hy)
                new = hy[0]
		m = 1
		w = len(word)
		k = len(new)
		# Flag is set to 1 if a hyphen was added.
		flag = 0
		if w<=1:
		    flag = 1
		while m<hylen:
                    if hylen==1:
			k += len(hy[m])
			new += hy[m]
			m += 1
		    # if the line ran over add a hyphen and set a flag.
		    elif j+w>self.columnSize:
			line+=new
			line+='-'
		        #self.lines[lineid]=line
			self.lines.append(line)
		        lineid+=1
                        line=''
			new = ''
			j=w
			flag = 1
		    else:
			k += len(hy[m])
		        new += hy[m] 
			j += len(hy[m])
		        m += 1
		if flag == 0:
                    #line+=' '
		    line+=new
		    #line+=' '
		    word=''
		    j+=1
		# if the flag was set use the remainder of the hyphenated word
		# and reset the count the the word that was hyphenated less what
		# was previously used on the line above.
	        else:
		    word=new
		    #line+=' '
		    #j+=len(new)
		    j=w-len(new)
	    l += 1
	    j += 1
	lastline = line+word
        self.lines.append(lastline)
        self.lineid=lineid
