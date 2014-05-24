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

ScriptishSchema = Schema((
    TextField(
        name='script',
        allowable_content_types=('text/plain'),
        widget=TextAreaWidget(
            label='Script',
            label_msgid='Newspaper_label_script',
            i18n_domain='Newspaper',
        ),
        default_output_type='text/plain',
    ),
),
)
