    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top):
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    result=skin.broadsheet.continuePDF(c,x,y,REQUEST,parent)
	    return (result[0],result[1])
