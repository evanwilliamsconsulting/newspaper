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
class IPositionable(Interface):
    """
	IElements are IPositionable within IContainer in a specific way.
    """

class ILayout(Interface):
    """
	IBlocks are layout on the page using this interface.
    """

class IObject(Interface):
    """
        Describes the Output Format
	Tells IPositionable and ILayout how to compute
	things like getPosition.
	Provides IContentish items with primitives 
	for rendering output.
    """

class IJSONOutput(IObject):
    """
	Extends IObject to provide JSON output.
    """

class IHTMLOutput(IObject):
    """
	Extends IObject to provide HTML output.
    """

class IPDFOutput(IObject):
    """
	Extends IObject to provide PDF output.
    """

class IContainer(Interface):
    """Marker interface for .Container.Container
    """

class IElement(Interface):
    """
	An Element within the Container.
    """

class ILocation(Interface):
    """Marker interface for .Location.Location
    """

class IPage(Interface):
    """
        A Page of an Issue that contains Blocks and Containers
    """

class IBroadsheet(IPage):
    """
	Extends a Page to provide Broadsheet aspect.
    """

class ITearsheet(IPage):
    """
	Extends a Page to provide a Tearsheet look.
    """

class ITabloid(IPage):
    """
	Extends a Page to provide a Tabloid look.
    """

class IColumn(IElement):
    """
	Extends IElement to support a Column-type element.
    """

class ITextColumn(IColumn):
    """
	Extends IColumn to provide a freeform Text column.
    """

class IRichColumn(IColumn):
    """
	Extends IColumn to provide a formatted Rich Text column.
    """

class IIssue(Interface):
    """
	An issue of Newspaper contains Pages
    """

class IPix(IElement):
    """
	Pix Element to include a Picture.
    """

class IContent(Interface):
    """Marker interface for .Content.Content
    """

class IArticle(Interface):
    """Marker interface for .Content.Content
    """

class ILine(IElement):
    """
	Supports a Line element.
    """

class IHeadline(IElement):
    """
	Supports a Headline element.
    """

class IWordage(Interface):
    """Marker interface for .Content.Content
    """

class IBlock(Interface):
    """Marker interface for .Content.Content
    """

class IPage(Interface):
    """Marker interface for .Content.Content
    """

class IGraphic(Interface):
    """Marker interface for .Content.Content
    """

class ILibrary(Interface):
    """Marker interface for .Content.Content
    """

##code-section FOOT
##/code-section FOOT
