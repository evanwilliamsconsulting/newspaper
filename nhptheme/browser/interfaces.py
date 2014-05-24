from zope import schema
from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer
from plone.app.portlets.interfaces import IColumn
from plone.portlets.interfaces import IPortletManager
from zope.viewlet.interfaces import IViewletManager

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope browser layer.
    """

class INHPTheme(IPortletManager, IColumn):
    """Add top portlets manager
    """

class IAboveContentViews(IViewletManager):
    """
    """

class IPortletType(Interface):
    """A registration for a portlet type.
    
    Each new type of portlet should register a utility with a unique name
    providing IPortletType, so that UI can find them.
    """
    
    title = schema.TextLine(
        title = u'Title',
        required = True)
   
    description = schema.Text(
        title = u'Description',
        required = False)

    addview = schema.TextLine(
        title = u'Add view',
        description = u'The name of the add view for assignments for this portlet type',
        required = True)
