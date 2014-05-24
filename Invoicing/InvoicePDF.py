# -*- coding: utf-8 -*-
#
# File: NewspaperView.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

##code-section module-header #fill in your manual code here
##/code-section module-header

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class InvoicePDF(BrowserView):
    """
    """

    ##code-section class-header_NewspaperView #fill in your manual code here
    ##/code-section class-header_NewspaperView
    something="ferf"

    def pdf(self):
        """
	"""
	return "Where do you want me to store the pdf?"
        request = getattr(context, 'REQUEST', None)
	cache = request.get('_plone_ec_cache', None)
	return cache

##code-section module-footer #fill in your manual code here
##/code-section module-footer
