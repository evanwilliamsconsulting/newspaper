# -*- coding: utf-8 -*-
#
# File: Block.py
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
from zope.interface import implements
from Products.CMFCore import permissions
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from archetypes.referencebrowserwidget import ReferenceBrowserWidget
from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

##code-section module-header #fill in your manual code here
##/code-section module-header

BlockishSchema = Schema((

    IntegerField(
	name='left',
	widget=IntegerField._properties['widget'](
	    label='left',
	    label_msgid='Newspaper_label_left',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='top',
	widget=IntegerField._properties['widget'](
	    label='top',
	    label_msgid='Newspaper_label_top',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='isBlockish',
	default=False,
        widget=BooleanField._properties['widget'](
	    label='isBlockish',
	    label_msgid='Newspaper_label_isBlockish',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='showLink',
        widget=BooleanField._properties['widget'](
	    label='showLink',
	    label_msgid='Newspaper_label_useRemainder',
	    i18n_domain='Newspaper',
	),
    ),
),
)
