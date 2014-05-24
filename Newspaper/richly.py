""" Puts Verbage into Columns and Provides Index by Lines

"""

import re
import os
from hyphenate import Hyphenator

__version__ = '1.0.20070709'

class RichColumnar:

	checkTag = False
	expectClose = False
	waitClose = False
	tagMightBe = ''

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
		#f = open("/home/newholland/webapps/nhpdev/zinstance/products/Newspaper/en.dic","r")
		#d = os.getcwd()
		f = open("/opt/dev/zinstance/products/Newspaper/en.dic","r")
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
		if len(self.currentLine)+len(self.currentWord)>self.getColumnSize()-5:
			return True
		else:
			return False

	def getLineId(self):
		return self.lineid

	def getCurrentLine(self):
		return self.currentLine

	def parseable(self,goodword,char):
		"""
		parse the characters and trap tags, later special chars too

		There are three cases for tags:

		1. <open>
		2. </open>
		3. <open/>

		All cases start with a check for '<'
		Then as long as '/' does not occur we read in the tag.
		If '/' occurs we stop reading in the tag and wait for the '>'
		If '>' occurs we stop reading in the tag immediately.

		The below code would match <one/two> as onetwo
		The below code would cause an error if an opentag occurred and there was never a close.
		"""
		nextchar=''
		flush = False
		if self.expectClose:
			if char=='>': # we closed, this must have been a <br/>
				self.expectClose = False # so clean up and return to normal
				flush = True
			else:
				self.waitClose = True
				self.expectClose = False
				self.tagMightBe += char
		elif self.checkTag:
			if char == '/':
				self.expectClose = True # we expect the tag to go by again but don't count
				self.checkTag = False
			elif char == '>': # close an open tag and return results
				self.checkTag = False
				flush=True
			else:
				self.tagMightBe += char
		elif char == '<': # wait and expect a tag?
			self.checkTag = True
			self.expectClose = False
			self.tagMightBe = ''
		else:
			self.tagMightBe = ''
			if char==' ':
				nextchar=char
				flush = True
			else:	
				nextchar=char
		return goodword+nextchar,flush,self.tagMightBe

	# this would be a lot better if a proper tag that had come back had a tag handler
	# so that the core formatting code doesn't get messed up.
	def returnText(self,mh):
		"""
		Return the Verbage
		"""
		state = 'START'
		state = self.walk(state)
		trythis = self.verbage
		trylen = len(self.verbage)
		l = 0
		j = 0
		word=''
		w = 0
		new = ''
		line=''
		lineid=0
		hy = []
		theword = ''
		extra = 10
		while l<trylen:
			if j+w>self.columnSize-extra:
				self.lines[lineid]=line
				lineid+=1
				line=''
				j=0
				word = ''
				w = 0
			theword, parseComplete, tag = self.parseable(theword,trythis[l])
			br = False
			if parseComplete:
				# does word already contain a hyphen?
				#print theword
				#print tag
				if tag.strip()=="br": #Don't have two in a row.
					#print "tag is br"
					self.lines[lineid]=line+word
					word = theword
					new = ''
					#lineid+=1
					line=word
					self.lines[lineid]=line
					lineid+=1
					new = ''
					word = ''
					line = '----'
					theword = ''
				hy = mh.hyphenate_word(theword)
				theword = ''
				hylen = len(hy)
				#word += new
				m = 0
				w = len(word)
				k = len(new)
				new += hy[0]
				#word += hy[0]
				while m<hylen:
					if j+w>self.columnSize-extra:
						#line+=new
						line+='-'
						self.lines[lineid]=line
						lineid+=1
						line=''
						new = ''
						word = ''
						j=w
					k += len(hy[m])
					new += hy[m] 
					word += hy[m]
					j += len(hy[m])
					m += 1
				w = len(word)
				line+=word
				word = ''
				new = ''
			l += 1
		lastline = line+word+theword
		self.lines[lineid]=lastline
		self.lineid=lineid
