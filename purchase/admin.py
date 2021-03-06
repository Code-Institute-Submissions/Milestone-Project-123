from django.contrib import admin
from .models import Car_Order


class Car_OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date_of_purchase',
                       'total', 'original_purchase', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'car', 'date_of_purchase',
              'full_name', 'email', 'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1', 'street_address2', 'county',
              'total', 'original_purchase', 'stripe_pid')
    
    list_display = ('user_profile', 'order_number', 'date_of_purchase',
                    'full_name', 'total')

    ordering = ('-date_of_purchase',)


admin.site.register(Car_Order, Car_OrderAdmin)
