from django.contrib import admin

from purchase_order.models import PurchaseOrder


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    pass
