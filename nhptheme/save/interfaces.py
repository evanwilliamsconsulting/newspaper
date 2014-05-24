from plone.theme.interfaces import IDefaultPloneLayer
from plone.app.portlets.interfaces import IColumn
from plone.portlets.interfaces import IPortletManager

class IThemeSchools(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IThemeSchoolsPortlets(IPortletManager, IColumn):
    """Add top portlets manager
    """