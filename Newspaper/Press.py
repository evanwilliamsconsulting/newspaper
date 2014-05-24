# -*- coding: utf-8 -*-
#
# File: Press.py
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
from reportlab.lib.units import inch
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper import Form

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='dateOfPublication',
        widget=DateTimeField._properties['widget'](
            label='Dateofpublication',
            label_msgid='Newspaper_label_dateOfPublication',
            i18n_domain='Newspaper',
        ),
    ),
    BooleanField(
	name='toggleDivTagsOn',
        widget=BooleanField._properties['widget'](
	    label='Display Div Tags',
	    label_msgid='Newspaper_label_toggleDivTagsOn',
	    i18n_domain='Newspaper',
	),
    ),
    FixedPointField(
        name='priceOfCopy',
        widget=FixedPointField._properties['widget'](
            label='Priceofcopy',
            label_msgid='Newspaper_label_priceOfCopy',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='tagLine',
        widget=StringField._properties['widget'](
            label='Tagline',
            label_msgid='Newspaper_label_tagLine',
            i18n_domain='Newspaper',
        ),
    ),
    ImageField(
        name='QRImage',
        widget=ImageField._properties['widget'](
            label='Qrimage',
            label_msgid='Newspaper_label_QRImage',
            i18n_domain='Newspaper',
        ),
        storage=AnnotationStorage(),
    ),
    StringField(
        name='headingTheme',
        widget=StringField._properties['widget'](
            label='Headingtheme',
            label_msgid='Newspaper_label_headingTheme',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='secondTheme',
        widget=StringField._properties['widget'](
            label='Secondtheme',
            label_msgid='Newspaper_label_secondTheme',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Press_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Press(BaseFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPress)

    meta_type = 'Press'
    _at_rename_after_creation = True

    schema = Press_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    aliases = {
        '(Default)'	:	PROJECTNAME.lower() + '_view',
	'view'		:	PROJECTNAME.lower() + '_view',
	}

    # Methods

##code-section module-footer #fill in your manual code here
##/code-section module-footer

