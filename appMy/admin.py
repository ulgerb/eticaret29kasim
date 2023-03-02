from django.contrib import admin
from .models import *

# Register your models here.


class ShopsAdmin(admin.ModelAdmin):
    '''Admin View for Shops'''

    list_display = ('user','product','count','id')
    
   

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Shops,ShopsAdmin)