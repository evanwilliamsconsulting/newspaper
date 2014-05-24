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


class BookTemplate(FSObject, Script, PageTemplate):

    """Wrapper for Page Template.
    """

    offset = 0
    width = 8.5
    height = 11

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

    def __init__(self, id, filepath, fullname=None, properties=None):
        FSObject.__init__(self, id, filepath, fullname, properties)
        self.ZBindings_edit(self._default_bindings)

    def _createZODBClone(self):
        """Create a ZODB (editable) equivalent of this object."""
        obj = ZopePageTemplate(self.getId(), self._text, self.content_type)
        obj.expand = 0
        obj.write(self.read())
        return obj

    def setWidth(self,width):
	""" Set Width"""
	self.width = width

    def setHeight(self,height):
	""" Set Height"""
	self.height = height 

#    def ZCacheable_isCachingEnabled(self):
#        return 0

    def _readFile(self, reparse):
        """Read the data from the filesystem.
        """
        if reparse:
            file = open(self._filepath, 'rU') # not 'rb', as this is a text file!
            try:
                data = file.read()
            finally:
                file.close()

            # If we already have a content_type set it must come from a
            # .metadata file and we should always honor that. The content
            # type is initialized as text/html by default, so we only
            # attempt further detection if the default is encountered.
            # One previous misbehavior remains: It is not possible to
            # force a text/html type if parsing detects it as XML.
            encoding = None
            preferred = preferred_encodings[:]

            if getattr(self, 'content_type', 'text/html') == 'text/html':
                xml_info = xml_detect_re.match(data)
                if xml_info:
                    # Smells like xml
                    # set "content_type" from the XML declaration
                    encoding = xml_info.group(1) or 'utf-8'
                    self.content_type = 'text/xml; charset=%s' % encoding

            if not isinstance(data, unicode):
                if encoding is None:
                    charset = getattr(self, 'charset', None)

                    if charset is None:
                        if self.content_type.startswith('text/html'):
                            mo = charset_re.search(self.content_type)
                            if mo:
                                charset = mo.group(1).lower()

                            if charset is None:
                                charset = charsetFromMetaEquiv(data)
                                
                        elif self.content_type.startswith('text/xml'):
                            charset = encodingFromXMLPreamble(data)

                        else:
                            raise ValueError('Unsupported content_type: %s'
                                                % self.content_type)

                    if charset is not None:
                        preferred.insert(0, charset)

                else:
                    preferred.insert(0, encoding)

                for enc in preferred:
                    try:
                        data = unicode(data, enc)
                        if isinstance(data, unicode):
                            break
                    except UnicodeDecodeError:
                            continue
                else:
                    data = unicode(data)

            self.write(data)


    security.declarePrivate('read')
    def read(self):
        # Tie in on an opportunity to auto-update
        self._updateFromFS()
        return PDFPageTemplate.inheritedAttribute('read')(self)

    ### The following is mainly taken from ZopePageTemplate.py ###

    expand = 0

    func_defaults = None
    func_code = ZopePageTemplate.func_code
    _default_bindings = ZopePageTemplate._default_bindings

    security.declareProtected(View, '__call__')

    def continuePDF(self,c,x,y,request,parent,pagenumber):
        #self._updateFromFS()  # Make sure the template has been loaded.

	#fptr = open (self._filepath,"r")
	#allLines = fptr.readlines()
        ynew=y
	pagenumber = 1
	for aLine in parent.listFolderContents():
                theId = aLine.getId()
		result=self.callPDFTemplate(theId,c,x,y,request,parent,pagenumber)
		pagenumber += 1
                x=result[0]
                y+=result[1]
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
	    #parent = 
	    print result
            #c.drawString(x,y,'callPDFTemplate')
	    result = result.callPDFPDTBySameName(c,x,y,request,parent,toplevel,pagenumber)
	    #except:
	    # 	result = requestedTemplate
            x=result[0]
            y=result[1]
	    return  (x,y)

    def renderPageHeader(self,c,x,y,pagenumber,parent):
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
	    thePage = "Page " + str(number)
            textobject.textLine(thePage)
	    c.drawText(textobject)
            y+=50
	    return (x,y)
    
    def renderMasthead(self,c,x,y,parent):
            textobject = c.beginText()
            textobject.setTextOrigin(x,y)
	    #thePress=parent.aq_parent['nhp']
	    theTagLine = 'A Press Publication' 
	    theDateOfPublication = str(parent.dateOfPublication)
	    year=theDateOfPublication[0:4]
	    day=str(int(theDateOfPublication[8:10]))
	    month=int(theDateOfPublication[6:7])
	    monthtext = ['January','February','March','April','May','June','July','August','September','October','November','December']
	    theMonth=monthtext[month-1]
	    useThisDate=day+" "+theMonth+" "+year
            width = 600 
            height = 75
	    #thePress = ImageReader(StringIO(thePress.data))
	    #c.drawImage(thePress,x,y,width,height)
	    pdfmetrics.registerFont(TTFont('Caslon','Caslon.ttf'))
            textobject.setFont('Caslon',36)
	    textobject.textLine("Chat Book")
	    textobject.setTextOrigin(x,y+30)
            textobject.setFont("Caslon",30)
            textobject.textLine("by Christopher Kenneth Hanson")
	    c.drawText(textobject)
            width = 135 
            height = 80 
	    #thePress=parent.aq_parent['nqr']
	    #thePress = ImageReader(StringIO(thePress.getQRImage().data))
	    #c.drawImage(thePress,x,y,width,height)
	    fptr = open('/opt/development/newholland/press/products/Newspaper/new_holland.gif',"r")
	    theQRFile = ImageReader(fptr)
	    c.drawImage(theQRFile,x+610,y-60,width,height)
	    #c.drawImage(thePress,x+615,y-115,width,height)
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
        self._updateFromFS()  # Make sure the template has been loaded.

	output = StringIO()

	c = canvas.Canvas(output,bottomup=0)
	x=35
	y=0
	all = ""
	pagenumber = 1
	for aLine in parent.listFolderContents():
		lengthOfLine = len(aLine)
		y = 150
		pagenumber += 1
		result=self.callPDFTemplate(aLine,c,x,y,request,parent,pagenumber)
                y+=result[1]
		c.showPage()
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

setattr(BookTemplate, 'source.xml',  BookTemplate.source_dot_xml)
setattr(BookTemplate, 'source.html', BookTemplate.source_dot_xml)
InitializeClass(BookTemplate)


registerMetaType('Book Template', BookTemplate)
