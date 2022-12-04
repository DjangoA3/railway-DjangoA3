from django.contrib import admin
from.models import fcsit
# Register your models here.
class fcsit(admin.ModelAdmin):
    list_display = ('first_name', 'reg_no')
    list_filter = ('reg_no', )

admin.site.register(fcsit)