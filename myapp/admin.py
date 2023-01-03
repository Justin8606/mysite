from django.contrib import admin

from myapp.models import Product,Cart

# Register your models here.

# admin.site.register(Product)

admin.site.site_header ='MySite Cart Administration'
admin.site.site_title = 'MySite'
admin.site.index_title = 'Mysite Cart'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','id','price','description',)
    search_fields = ('name',)
    
    def set_price_to_zero(self,request,queryset):
        queryset.update(price=0)
        
    def set_price_to_fiftyk(self,request,queryset):
        queryset.update(price=50000)
        
    actions = ('set_price_to_zero','set_price_to_fiftyk',)
    
admin.site.register(Product,ProductAdmin)
        
    
#Django admin panel customization  #Code keen
#Django jasmin
#gunicorn
#uwsgi


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('id','user','product','quantity')