# -*- coding: utf-8 -*-

from zope.interface import Interface
from Products.Archetypes.interfaces import IBaseObject

class INewsFolder(IBaseObject):
    """Folderish base interface marker
    """
    def listFolderContents(contentFilter=None, suppressHiddenFiles=0):
        """
        """

    def folderlistingFolderContents(contentFilter=None, suppressHiddenFiles=0 ):
	"""
        """

##code-section HEAD
##/code-section HEAD

class IContainer(Interface):
    """Marker interface for .Container.Container
    """

class IBoxContainer(Interface):
    """Marker interface for .Container.Container
    """

class IBookContainer(Interface):
    """Marker interface for .BookContainer.BookContainer
    """

class ILocation(Interface):
    """Marker interface for .Location.Location
    """

class IBroadsheet(Interface):
    """Marker interface for .Broadsheet.Broadsheet
    """

class ITearsheet(Interface):
    """Marker interface for .Tearsheet.Tearsheet
    """

class IColumn(Interface):
    """Marker interface for .Column.Column
    """

class ITextColumn(Interface):
    """Marker interface for .TextColumn.TextColumn
    """

class IRichColumn(Interface):
    """Marker interface for .RichColumn.RichColumn
    """

class IIssue(Interface):
    """Marker interface for .Issue.Issue
    """

class IIssueList(Interface):
    """IIssueList
    """

class IPress(Interface):
    """Marker interface for .Issue.Issue
    """

class IPix(Interface):
    """Marker interface for .Picture.Picture
    """

class IRichText(Interface):
    """Marker interface for .RichText.RichText
    """

class IContent(Interface):
    """Marker interface for .Content.Content
    """

class IArticle(Interface):
    """Marker interface for .Content.Content
    """

class ILine(Interface):
    """Marker interface for .Content.Content
    """

class IHeadline(Interface):
    """Marker interface for .Content.Content
    """

class IWordage(Interface):
    """Marker interface for .Content.Content
    """

class IBlock(Interface):
    """Marker interface for .Content.Content
    """

class IWebpage(Interface):
    """Marker interface for .Content.Content
    """

class IWidget(Interface):
    """Marker interface for .Content.Content
    """

class IBook(Interface):
    """Marker interface for .Content.Content
    """

class IPage(Interface):
    """Marker interface for .Content.Content
    """

class ISection(Interface):
    """Marker interface for .Content.Content
    """

class IGraphic(Interface):
    """Marker interface for .Content.Content
    """

class ICorrespondant(Interface):
    """Marker interface for .Content.Content
    """

class IUsers(Interface):
    """Marker interface for .Content.Content
    """

class IBookContents(Interface):
    """Marker interface for .Content.Content
    """

##code-section FOOT
##/code-section FOOT
