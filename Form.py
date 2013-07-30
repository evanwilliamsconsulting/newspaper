from zope import interface, schema
from z3c.form import form, field, button
from plone.app.z3cform.layout import wrap_form

class MySchema(interface.Interface):
    age = schema.Int(title=u"Age")

class MyForm(form.Form):
    fields = field.Fields(MySchema)
    ignoreContext = True
    label = u"Please enter your age"

    @button.buttonAndHandler(u'Apply')
    def handleApply(self,action):
        data,errors = self.extractData()
        print data['age']
