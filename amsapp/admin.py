from django.contrib import admin

from .models import Registration, Feedback,product,categories,cart,payments

admin.site.register(Registration),
admin.site.register(Feedback),
admin.site.register(product),
admin.site.register(categories),
admin.site.register(cart),
admin.site.register(payments)