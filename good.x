from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
ReferenceField(
        name='containers',
        widget=ReferenceBrowserWidget(
            label='Containers',
            label_msgid='Newspaper_label_containers',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Container','YouCanBox','CreditsBox','Puzzle',),
        multiValued=1,
        relationship='containerLocation',
    ),
),
