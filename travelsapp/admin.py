from django.contrib import admin
from .models import *


admin.site.site_header='Admin panel'
admin.site.index_title='Welcome to admin portal'


admin.site.register(Car)
admin.site.register(Booking)