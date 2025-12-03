from django.contrib import admin
from .models import Item,Login,Category

# admin.site.register(Item)
@admin.register(Item)
class itemadmin(admin.ModelAdmin):
    list_display = ('product','price','image')
    search_fields = ('product','price')
    # view_on_site = True
    list_filter = ('price',)
    list_editable = ('price',)                      # Fields editable directly in list
    ordering = ('product',)                         # Default ordering
    readonly_fields = ('image',)

admin.site.register(Category)
    
admin.site.register(Login)
