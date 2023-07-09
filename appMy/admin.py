from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','user', 'category', 'stars')


@admin.register(ProductImg)
class ProductImgAdmin(admin.ModelAdmin):
    list_display = ('product', 'id')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','slug')
    
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','slug')
    
@admin.register(SizeNumber)
class SizeNumberAdmin(admin.ModelAdmin):
    list_display = ('product','id', 'color', 'size', 'stok')


@admin.register(SizeLetter)
class SizeLetterAdmin(admin.ModelAdmin):
    list_display = ('product','id', 'color', 'size','stok')


@admin.register(ProductStok)
class ProductStokAdmin(admin.ModelAdmin):
    list_display = ('product','id')

@admin.register(Gander)
class GanderAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')

@admin.register(Size2)
class Size2Admin(admin.ModelAdmin):
    list_display = ('title', 'id')



@admin.register(Shopbasket)
class ShopbasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_letter',
                    'price_all', 'count', 'id')
    
    



  
admin.site.register(ZWhey)    
admin.site.register(ZCasein)    
admin.site.register(ZSoya)    
admin.site.register(ZBcaa)    
admin.site.register(ZCreatin)    
admin.site.register(ZLCarnitine)    
admin.site.register(ZAminoAsit)    
admin.site.register(ZKafein)    
admin.site.register(ZVitamin)    
admin.site.register(ZAksesuar)    

# PROGRAM
admin.site.register(ZYagyakım)
admin.site.register(ZHıt)
admin.site.register(ZGuc)
admin.site.register(ZPpl)
admin.site.register(ZFull)
admin.site.register(ZIlerı)
admin.site.register(ZSecım)
admin.site.register(ZGun)
admin.site.register(ZNasıl)
admin.site.register(ZMakro)