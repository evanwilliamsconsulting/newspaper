    def __init__(self, id, filepath, fullname=None, properties=None,width=11,height=17):
        self.width = width
	self.height = height	
        FSObject.__init__(self, id, filepath, fullname, properties)
        self.ZBindings_edit(self._default_bindings)
