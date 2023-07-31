from django.contrib import admin

# Register your models here.

from .models import departments
from .models import booking
from .models import doctors

admin.site.register(departments)



admin.site.register(doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display =  ('id', 'p_name', 'p_phone', 'p_email', 'doc_name','booking_date', 'booked_on' )

admin.site.register(booking,BookingAdmin)
