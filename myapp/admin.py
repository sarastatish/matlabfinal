from django.contrib import admin
from myapp.models import student, product,patient,Appointment

# Register your models here.
admin.site.register(student)
admin.site.register(product)
admin.site.register(patient)
admin.site.register(Appointment)
