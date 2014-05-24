# -*- coding: utf-8 -*-
#
# File: Graphic.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

import string 
from cStringIO import StringIO

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.Five.browser import BrowserView
from zope.interface import implements
import interfaces
from columnar import Columnar

import hyphenate 

from Products.CMFCore.utils import getToolByName

from browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *

from Products.CMFCore.utils import getToolByName


from zope.component import getMultiAdapter

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='graphic',
        allowable_content_types=('image/svg+xml',),
        widget=TextAreaWidget(
            label='Graphic',
            label_msgid='Newspaper_label_graphic',
            i18n_domain='Newspaper',
        ),
        default_output_type='image/svg+xml',
    ),
    IntegerField(
        name='width',
	widget=IntegerWidget(
		label='width',
		label_msgid='Newspaper_label_width',
		i18n_domain='Newspaper',
	),
    ),        
    IntegerField(
        name='height',
	widget=IntegerWidget(
		label='height',
		label_msgid='Newspaper_label_height',
		i18n_domain='Newspaper',
	),
    ),        
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Graphic_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Graphic(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IGraphic)

    meta_type = 'Graphic'
    _at_rename_after_creation = True

    schema = Graphic_schema
    containerChoice = None

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    def showGraphic(self):
	""" returns svg """
        skin = self.portal_skins.newspaper_templates
	showTemplate=skin.showGraphic
	return showTemplate()

    def returnSvg(self):
	""" returns svg """
	svg = self.getGraphic()
	return svg

registerType(Graphic, PROJECTNAME)
# end of class Graphic 

##code-section module-footer #fill in your manual code here
##/code-section module-footer
    
