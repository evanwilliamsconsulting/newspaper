# -*- coding: utf-8 -*-
#
# File: Newspaper.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
##code-section config-head #fill in your manual code here
##/code-section config-head


PROJECTNAME = "Newspaper"

# Permissions
VIEW_PERMISSION = "View"
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Contributor'))
setDefaultRoles(VIEW_PERMISSION,('Anonymous','Authenticated'))
ADD_CONTENT_PERMISSIONS = {
    'Container': 'Newspaper: Add Container',
    'BookContainer': 'Newspaper: Add BookContainer',
    'Block': 'Newspaper: Add Block',
    'Webpage': 'Newspaper: Add Webpage',
    'Widget': 'Newspaper: Add Widget',
    'Location': 'Newspaper: Add Location',
    'Broadsheet': 'Newspaper: Add Broadsheet',
    'Tearsheet': 'Newspaper: Add Tearsheet',
    'Column': 'Newspaper: Add Column',
    'TextColumn': 'Newspaper: Add TextColumn',
    'RichColumn': 'Newspaper: Add RichColumn',
    'Issue': 'Newspaper: Add Issue',
    'Press': 'Newspaper: Add Press',
    'Pix': 'Newspaper: Add Pix',
    'RichText': 'Newspaper: Add RichText',
    'Content': 'Newspaper: Add Content',
    'Article': 'Newspaper: Add Article',
    'BookContents': 'Newspaper: Add BookContents',
    'Graphic': 'Newspaper: Add Graphic',
    'Wordage': 'Newspaper: Add Wordage',
    'Word': 'Newspaper: Add Word',
    'Line': 'Newspaper: Add Line',
    'Hyphenate': 'Newspaper: Add Hyphenate',
    'Headline': 'Newspaper: Add Headline',
    'Line': 'Newspaper: Add Line',
    'Book': 'Newspaper: Add Book',
    'Page': 'Newspaper: Add Page',
    'Correspondant': 'Newspaper: Add Correspondant',
    'Library': 'Newspaper: Add Library',
    'Users': 'Newspaper: Add Users',
    'Section': 'Newspaper: Add Section',
    'Wordy': 'Newspaper: Add Wordy',
}

setDefaultRoles('Newspaper: Add Container', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add BookContainer', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Location', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add Broadsheet', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add Tearsheet', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add Column', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add TextColumn', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add RichColumn', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add Issue', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add Press', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add RichText', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add Content', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add Line', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add Block', ('Manager','Owner'))
setDefaultRoles('Newspaper: Add Webpage', ('Contributor','Editor','Anonymous','Manager','Owner'))
setDefaultRoles('Newspaper: Add Widget', ('Contributor','Editor','Anonymous','Manager','Owner'))

setDefaultRoles('Newspaper: Add Headline', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Line', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Wordage', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Hyphenate', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Word', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Article', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add BookContents', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Pix', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Graphic', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Book', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Page', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Section', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Correspondant', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Library', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Users', ('Contributor','Editor','Manager','Owner'))
setDefaultRoles('Newspaper: Add Wordy', ('Contributor','Editor','Manager','Owner'))

product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
##/code-section config-bottom
SKINS_DIR="skins"
GLOBALS = globals()

# Load custom configuration not managed by archgenxml
try:
    from Products.Newspaper.AppConfig import *
except ImportError:
    pass
