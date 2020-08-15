from django.contrib import admin
from .models import userdetails,impdetails,hospital_list,history,relativedetails
# Register your models here.
admin.site.register(userdetails)
admin.site.register(impdetails)
admin.site.register(hospital_list)
admin.site.register(history)
admin.site.register(relativedetails)
