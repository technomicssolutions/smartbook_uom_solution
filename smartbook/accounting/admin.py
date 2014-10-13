from django.contrib import admin

from accounting.models import Ledger, LedgerEntry, Transaction

admin.site.register(Ledger)
admin.site.register(LedgerEntry)
class TransactionAdmin(admin.ModelAdmin):
	search_fields = ['transaction_ref']
admin.site.register(Transaction, TransactionAdmin)
