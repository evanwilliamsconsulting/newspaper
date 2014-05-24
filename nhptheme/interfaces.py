from zope.interface import Interface,implements
from zope import schema
from persistent import Persistent
from zope.schema.fieldproperty import FieldProperty

class ISettings(Interface):
    """ Define schema for settings of the add-on product """
    issue = schema.TextLine(title=u"Issue")
