#############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Customizable page templates that come from the filesystem.

$Id: FSPageTemplate.py 110577 2010-04-07 06:33:17Z jens $
"""

import re
import sys
import urllib2
import os

from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.SecurityManagement import getSecurityManager
from App.class_init import InitializeClass
from App.special_dtml import DTMLFile
#from Products.PageTemplates.PageTemplate import PageTemplate
from pageTemplate import PageTemplate
from Products.PageTemplates.utils import charsetFromMetaEquiv
from Products.PageTemplates.utils import encodingFromXMLPreamble
from Products.PageTemplates.ZopePageTemplate import preferred_encodings
from Products.PageTemplates.ZopePageTemplate import Src
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate
from Shared.DC.Scripts.Script import Script

from Products.CMFCore.DirectoryView import registerFileExtension
from Products.CMFCore.DirectoryView import registerMetaType
from Products.CMFCore.FSObject import FSObject
from Products.CMFCore.permissions import FTPAccess
from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ViewManagementScreens
from Products.CMFCore.utils import _checkConditionalGET
from Products.CMFCore.utils import _dtmldir
from Products.CMFCore.utils import _setCacheHeaders

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import string 
from cStringIO import StringIO

xml_detect_re = re.compile('^\s*<\?xml\s+(?:[^>]*?encoding=["\']([^"\'>]+))?')
charset_re = re.compile(r'charset.*?=.*?(?P<charset>[\w\-]*)', re.I|re.M|re.S)
_marker = object()


class PDFPageTemplate(FSObject, Script, PageTemplate):

    """Wrapper for Page Template.
    """

    offset = 0

    expand = 0
    func_defaults = None
    func_code = ZopePageTemplate.func_code
    _default_bindings = ZopePageTemplate._default_bindings

    meta_type = 'Filesystem Page Template'
    _owner = None  # Unowned

    manage_options=({'label':'Customize', 'action':'manage_main'},
                    {'label':'Test', 'action':'ZScriptHTML_tryForm'},
                   )

    security = ClassSecurityInfo()
    security.declareObjectProtected(View)

    security.declareProtected(ViewManagementScreens, 'manage_main')
    manage_main = DTMLFile('custpt', _dtmldir)

    # Declare security for unprotected PageTemplate methods.
    security.declarePrivate('pt_edit', 'write')

    def __init__(self, id, filepath, fullname=None, properties=None,width=11,height=17):
        self.width = width
	self.height = height	
	self._filepath = filepath
        #FSObject.__init__(self, id, filepath, fullname, properties)
        self.ZBindings_edit(self._default_bindings)

    security.declareProtected(View, '__call__')

    def continuePDF(self,c,x,y,request,parent,pagenumber):
	#script = self.script
	# Cook the Macros yourself!
	# For Now, just to demonstrate that it works,
	# Just Return the script itself
        ynew=y
	for aLine in parent.listFolderContents():
                theId = aLine.getId()
		result=self.callPDFTemplate(theId,c,x,y,request,parent,pagenumber)
                #x=result[0]
                #y=result[1]
	return (x,y)

    def pdf(self,request,parent):
	return self.pt_render(request,parent)

    def pdfPartial(self):
	return

    def web(self,request,parent):
	fptr = open (self._filepath,"r")
	allLines = fptr.readlines()
	all = ""
	for aLine in allLines:
		lengthOfLine = len(aLine)
		aLine = aLine[0:lengthOfLine-1]
		if aLine=='masthead':
			all+=""
		elif aLine=='newcanvas':
			all+=''
		elif aLine=='showpage':
			all+=''
		elif aLine=='save':
			all+=''
		elif aLine=='pageone':
		    all+=self.callTemplate(aLine,request,parent)
		else:
                    all+= ''
	return all

    def continueWEB(self,request,parent,thething,start="",end="",top=0,left=0,width=0,height=0):
	all = ""
        width=0
        height=0
        top = top
        left = left	
	for theObject in parent.listFolderContents():
                toplevel = request.PARENTS[0]
		#if start != 0:
		#all += start
                result = theObject.callPDTBySameName(request,theObject,top,left,width,height,"","")
		if result is None:
                    result = ('','0','0','0','0')
                all += result[0]
		top = str(int(result[1]))
		left = str(int(result[2]))
                if result[3] is None:
		    width = '0'
                else:
                    width = '0'
                if result[4] is None:
                    height = '0'
                else:
                    height = '0'
		#all += end
	return (all,top,left,width,height)

    def callTemplate(self,requestedTemplate,request,parent):
	    # Call the web function on the requested template
	    # In the same zopish folder as this template.
	    all = ""
	    toplevel = request.PARENTS[0]
	    #result = str(theContent.__dict__)
	    #try:
	    #print parent.__dict__
	    #print request.__dict__
	    result = parent[requestedTemplate]
	    parent = result
	    result = result.callPDTBySameName(all,request,parent,0,0)
	    result = str(result)
	    #except:
	    # 	result = requestedTemplate
	    return result

    def webPartial(self):
	return

    def pt_macros(self):
        # Tie in on an opportunity to auto-reload
        self._updateFromFS()
        return PDFPageTemplate.inheritedAttribute('pt_macros')(self)

    def callPDFTemplate(self,result,c,x,y,request,parent,pagenumber):
	    # Call the web function on the requested template
	    # In the same zopish folder as this template.
	    toplevel = request.PARENTS[0]
	    #result = str(theContent.__dict__)
	    #try:
	        #result = str(theContent[requestedTemplate].callPDTBySameName(request))
	    #print requestedTemplate
	    result=parent[result]
	    #parent = 
	    #print result
            #c.drawString(x,y,'callPDFTemplate')
	    result = result.callPDFPDTBySameName(c,x,y,request,parent,toplevel,pagenumber)
	    #except:
	    # 	result = requestedTemplate
            #x=result[0]
            #y=result[1]
	    return  (x,y)

    def renderPageHeader(self,c,x,y,pagenumber,parent):
	    #y += 1150
	    y += 1080
	    x -= 30
	    if pagenumber == 'pagetwo':
	        number = 2
	    elif pagenumber == 'pagethree':
                number = 3
            elif pagenumber == 'pagefour':
                number = 4
	    else:
		number = 5
            textobject = c.beginText()
            textobject.setTextOrigin(x,y+40)
            textobject.setFont('Caslon',16)
	    textobject.textLine("New Holland Press")
	    textobject.setTextOrigin(x+250,y+40)
            textobject.setFont("Caslon",16)
            textobject.textLine("A Paper Of Discussion")
            textobject.setTextOrigin(x+450,y+40)
            textobject.setFont('Caslon',16)
	    #theDateOfPublication = str(parent.dateOfPublication)
	    theDateOfPublication = "2014:05:02"
	    year=theDateOfPublication[0:4]
	    day=str(int(theDateOfPublication[8:10]))
	    month=int(theDateOfPublication[5:7])
	    monthtext = ['January','February','March','April','May','June','July','August','September','October','November','December']
	    theMonth=monthtext[month-1]
	    useThisDate=day+" "+theMonth+" "+year
            textobject.textLine(useThisDate)
            textobject.setTextOrigin(x+625,y+40)
	    thePage = "Page " + str(number)
            textobject.textLine(thePage)
	    c.drawText(textobject)
            y+=50
	    return (x,y)
    
    def renderMasthead(self,c,x,y,parent):
	    #y = 970  + y
	    #y = 1070  + y
	    y = 970  + y
	    #width = 225
	    #height = 200
	    #fptr = open('/opt/newhol/press/products/Newspaper/pjs.jpg',"r")
	    #theQRFile = ImageReader(fptr)
	    #c.drawImage(theQRFile,x-20,y-30,width,height)
	    #fptr = open('/opt/newhol/press/products/Newspaper/hamilton.jpg',"r")
	    #fptr = open('/opt/newhol/press/products/Newspaper/santa.jpg',"r")
	    #theQRFile = ImageReader(fptr)
	    #c.drawImage(theQRFile,x+220,y-30,width,height)
	    #y = y - 100
	    #fptr = open('/root/magnolia.png',"r")
	    #theTurkey = ImageReader(fptr)
	    #theMask = [100,255,100,255,100,255]
	    #c.drawImage(theTurkey,x+300,y-400,825,882,mask=theMask)
	    #c.drawImage(theTurkey,x+300,y-400,825,882)
            textobject = c.beginText()
            textobject.setTextOrigin(x-20,y)
	    #thePress=parent.aq_parent['nhp']
	    #theTagLine = parent.tagLine
	    #theDateOfPublication = str(parent.dateOfPublication)
	    theDateOfPublication = "2014:05:02"
	    year=theDateOfPublication[0:4]
	    day=str(int(theDateOfPublication[8:10]))
	    month=int(theDateOfPublication[5:7])
	    monthtext = ['January','February','March','April','May','June','July','August','September','October','November','December']
	    theMonth=monthtext[month-1]
	    useThisDate=day+" "+theMonth+" "+year
            width = 600 
            height = 75
	    #thePress = ImageReader(StringIO(thePress.data))
	    #c.drawImage(thePress,x,y,width,height)
            width = 80
            height = 80 
	    #thePress=parent.aq_parent['nqr']
	    #thePress = ImageReader(StringIO(thePress.getQRImage().data))
	    #c.drawImage(thePress,x,y,width,height)
	    #c.drawImage(thePress,x+615,y-115,width,height)
            textobject.setFont('Caslon',80)
	    textobject.setFillColorRGB(0,0,0)
	    textobject.textLine("New Holland Press")
	    textobject.setTextOrigin(x,y-20)
            textobject.setFont("Caslon",16)
	    textobject.setFillColorRGB(0,0,0)
            textobject.textLine("A Paper Of Discussion")
            textobject.setFont("Caslon",16)
	    textobject.setFillColorRGB(0,0,0)
            textobject.setTextOrigin(x+470,y-20)
            textobject.textLine("www.newhollandpress.com")
	    textobject.setTextOrigin(x+525,y+50)
            textobject.textLine(useThisDate)
	    textobject.setFillColorRGB(0,0,0)
	    textobject.setTextOrigin(x+55,y+65)
            textobject.textLine("Free to Interested Parties!")
            textobject.setTextOrigin(x+250,y+45)
            #textobject.textLine("Advance Copy!")
	    textobject.setFillColorRGB(0,0,0)
	    c.drawText(textobject)
            y+=50
	    return (x,y)

    def setOffset(self,amount):
	    """
            TEST
            """
	    self.offset = amount

    def getOffset(self):
	    """
            TEST
            """
	    return self.offset

    def pt_render(self, request, parent):
        #self._updateFromFS()  # Make sure the template has been loaded.

	#fptr = open (self._filepath,"r")
	fptr = open ("/opt/dev/zinstance/products/Newspaper/issue.pd","r")
	allLines = fptr.readlines()
	
	#output = open('tmp.pdf','w')
	output = StringIO()


	#c = canvas.Canvas(output,pagesize=(792,1250),bottomup=1)
	c = canvas.Canvas(output,pagesize=(720,1152),bottomup=1)
	x=35
	y=0
	all = ""
	for aLine in allLines:
		lengthOfLine = len(aLine)
		aLine = aLine[0:lengthOfLine-1]
		if aLine=='masthead':
			x=35
			y=100
			result=self.renderMasthead(c,x,y,parent)
			x=result[0]
			y=result[1]
			all+="New Holland Press"
			y = 125
			self.setOffset(150)
		elif aLine=='newcanvas':
			all+=''
			y=100
		elif aLine=='showpage':
	                c.showPage()
			x=50
                        y=0
			all+=''
                elif aLine == 'pageone':
        		pdfmetrics.registerFont(TTFont('Times-Roman','Times-Roman.ttf'))
        		pdfmetrics.registerFont(TTFont('Italic','FilosIta.ttf'))
        		pdfmetrics.registerFont(TTFont('Caslon','Caslon.ttf'))
        		pdfmetrics.registerFont(TTFont('VeraBd','VeraBd.ttf'))
			y = 150
			pagenumber = 1
		        result=self.callPDFTemplate(aLine,c,x,y,request,parent,pagenumber)
                        x+=result[0]
                        y+=result[1]
		elif aLine=='save':
			all+=''
		elif aLine == 'pagetwo':
		    y = 0
		    result=self.renderPageHeader(c,x,y,aLine,parent)
		    x=result[0]
		    y=result[1]
		    pagenumber = 2
		    result=self.callPDFTemplate(aLine,c,x,y,request,parent,pagenumber)
                    x+=result[0]
                    y+=result[1]
		elif aLine == 'pagethree':
		    y = 0
		    result=self.renderPageHeader(c,x,y,aLine,parent)
		    x=result[0]
		    y=result[1]
		    result=self.callPDFTemplate(aLine,c,x,y,request,parent,pagenumber)
                    x+=result[0]
                    y+=result[1]
		elif aLine == 'pagefour':
		    y = 0
		    result=self.renderPageHeader(c,x,y,aLine,parent)
		    x=result[0]
		    y=result[1]
		    result=self.callPDFTemplate(aLine,c,x,y,request,parent,pagenumber)
                    x+=result[0]
                    y+=result[1]
	c.save()


	#pdfresult = open('tmp.pdf','r')
        #result = pdfresult.read()
	result = output.getvalue()
	output.close()
	#pdfresult.close()

	#print self.__dict__

	response = request.RESPONSE

        response.setHeader('Content-type','application/pdf')
        response.setHeader('Content-disposition','inline; filename="%s.pdf"' % 'tmp')

	return result

        #if not source:
        #    _setCacheHeaders(self, extra_context)

    security.declareProtected(ViewManagementScreens, 'pt_source_file')
    def pt_source_file(self):

        """ Return a file name to be compiled into the TAL code.
        """
        return 'file:%s' % self._filepath

    security.declarePrivate( '_ZPT_exec' )
    _ZPT_exec = ZopePageTemplate._exec.im_func

    security.declarePrivate( '_exec' )
    def _exec(self, bound_names, args, kw):
        """Call a PDFPageTemplate"""
        try:
            response = self.REQUEST.RESPONSE
        except AttributeError:
            response = None
        # Read file first to get a correct content_type default value.
        self._updateFromFS()

        if not kw.has_key('args'):
            kw['args'] = args
        bound_names['options'] = kw

        try:
            response = self.REQUEST.RESPONSE
            if not response.headers.has_key('content-type'):
                response.setHeader('content-type', self.content_type)
        except AttributeError:
            pass

        security=getSecurityManager()
        bound_names['user'] = security.getUser()

        # Retrieve the value from the cache.
        keyset = None
        if self.ZCacheable_isCachingEnabled():
            # Prepare a cache key.
            keyset = {
                      # Why oh why?
                      # All this code is cut and paste
                      # here to make sure that we
                      # dont call _getContext and hence can't cache
                      # Annoying huh?
                      'here': self.aq_parent.getPhysicalPath(),
                      'bound_names': bound_names}
            result = self.ZCacheable_get(keywords=keyset)
            if result is not None:
                # Got a cached value.
                return result

        # Execute the template in a new security context.
        security.addContext(self)
        try:
            result = self.pt_render(extra_context=bound_names)
            if keyset is not None:
                # Store the result in the cache.
                self.ZCacheable_set(result, keywords=keyset)
            return result
        finally:
            security.removeContext(self)

        return result

    # Copy over more methods
    security.declareProtected(FTPAccess, 'manage_FTPget')
    manage_FTPget = ZopePageTemplate.manage_FTPget.im_func

    security.declareProtected(View, 'get_size')
    get_size = ZopePageTemplate.get_size.im_func
    getSize = get_size

    security.declareProtected(ViewManagementScreens, 'PrincipiaSearchSource')
    PrincipiaSearchSource = ZopePageTemplate.PrincipiaSearchSource.im_func

    security.declareProtected(ViewManagementScreens, 'document_src')
    document_src = ZopePageTemplate.document_src.im_func

    pt_getContext = ZopePageTemplate.pt_getContext.im_func

    ZScriptHTML_tryParams = ZopePageTemplate.ZScriptHTML_tryParams.im_func

    source_dot_xml = Src()

class ScriptedPageTemplate(PDFPageTemplate):

    """Wrapper for Scripted Page Template.
    """

    meta_type = 'Scripted Page Template'

    security = ClassSecurityInfo()

    def __init__(self, id, script, fullname=None, properties=None,width=11,height=17):
        self.width = width
	self.height = height	
	self.script = script

    security.declareProtected(View, '__call__')

    def continuePDF(self,c,x,y,request,parent,pagenumber):
	# Here is where it has to process the instructions in the .pd script
        #self._updateFromFS()  # Make sure the template has been loaded.

	#fptr = open (self._filepath,"r")
	#allLines = fptr.readlines()

	script = self.script

	textobject = c.beginText()
	textobject.textLine(script)
	c.drawText(textobject)

	return (x,y)

    source_dot_xml = Src()

setattr(PDFPageTemplate, 'source.xml',  PDFPageTemplate.source_dot_xml)
setattr(PDFPageTemplate, 'source.html', PDFPageTemplate.source_dot_xml)
InitializeClass(PDFPageTemplate)
registerMetaType('PDF Page Template', PDFPageTemplate)
setattr(ScriptedPageTemplate, 'source.xml',  ScriptedPageTemplate.source_dot_xml)
setattr(ScriptedPageTemplate, 'source.html', ScriptedPageTemplate.source_dot_xml)
InitializeClass(ScriptedPageTemplate)
registerMetaType('Scripted Page Template', ScriptedPageTemplate)
