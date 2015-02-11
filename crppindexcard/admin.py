from django.contrib import admin

import crppindexcard.models

admin.site.register(crppindexcard.models.IndexCard)
admin.site.register(crppindexcard.models.Section)
admin.site.register(crppindexcard.models.Question)
admin.site.register(crppindexcard.models.Dimension)
admin.site.register(crppindexcard.models.Component)
admin.site.register(crppindexcard.models.Element)
admin.site.register(crppindexcard.models.ElementQuestionCharField)