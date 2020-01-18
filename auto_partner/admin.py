from django.contrib import admin
from auto_partner.models import Partner, Auto, partnerAdmin, autoAdmin, AutoPartnerRelation


admin.site.register(Partner, partnerAdmin)
admin.site.register(Auto, autoAdmin)
admin.site.register(AutoPartnerRelation)

