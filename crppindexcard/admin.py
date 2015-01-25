from django.contrib import admin

import crppindexcard.models

admin.site.register(crppindexcard.models.IndexCard)
admin.site.register(crppindexcard.models.Section)
admin.site.register(crppindexcard.models.QuestionShort)
admin.site.register(crppindexcard.models.QuestionLong)