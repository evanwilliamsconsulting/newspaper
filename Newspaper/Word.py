# -*- coding: utf-8 -*-
#
# File: Wordage.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.Five.browser import BrowserView
from zope.interface import implements
import interfaces
from richly import RichColumnar

import hyphenate 

from Products.CMFCore.utils import getToolByName

from browserdefault import BrowserDefaultMixin

from richly import RichColumnar

from Products.Newspaper.config import *

from Products.CMFCore.utils import getToolByName

from WordySchema import WordySchema


from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

import string 
from cStringIO import StringIO


from zope.component import getMultiAdapter

##code-section module-header #fill in your manual code here
##/code-section module-header

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Wordage_schema = BaseSchema.copy() + \
	WordySchema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Word(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IWordage,interfaces.IContainer)

    meta_type = 'Word'
    _at_rename_after_creation = True

    schema = Wordage_schema
    containerChoice = None

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Word, PROJECTNAME)
# end of class Wordage

##code-section module-footer #fill in your manual code here
##/code-section module-footer
    
