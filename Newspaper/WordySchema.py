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

WordySchema = Schema((
    TextField(
        name='wordage',
        allowable_content_types=('text/rtf', 'text/structured', 'text/html', 'application/msword','text/plain'),
        widget=RichWidget(
            label='Wordage',
            label_msgid='Newspaper_label_verbage',
            i18n_domain='Newspaper',
        ),
        default_output_type='text/rtf',
    ),
    IntegerField(
        name='columnSize',
	widget=IntegerWidget(
		label='columnSize',
		label_msgid='Newspaper_label_results',
		i18n_domain='Newspaper',
	),
    ),        
),
)
