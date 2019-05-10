from django.contrib import admin
from .models import witness_for, witness_against

# admin.site.register(witness_for, witness_for_admin)
# admin.site.register(witness_against, witness_against_admin)

class witness_for_admin(admin.ModelAdmin):
    list_display = (
        'year',
        'bill_no',
        'bill_sponsor',
        'party',
        'committee',
        'witness_for',
        'witness_for_org',
        'law',
    )
    search_fields = ('year', 'bill_no')
admin.site.register(witness_for, witness_for_admin)

class witness_against_admin(admin.ModelAdmin):
    list_display = (
        'year',
        'bill_no',
        'bill_sponsor',
        'party',
        'committee',
        'witness_against',
        'witness_against_org',
        'law',
    )
    search_fields = ('year', 'bill_no')
admin.site.register(witness_against, witness_against_admin)
