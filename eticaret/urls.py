"""eticaret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *
from appUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index" ),
    path('Ürün/', ürünler, name="ürünler" ),
    path('İletişim/', iletişim,name="iletişim"),
    path('Sepet/', sepet,name="sepet"),
    path('ödeme/', ödeme,name="ödeme"),
    path('Ürün/<slug>/', productDetails,name="productDetails"),
    path('ShopBasketDelete/<sid>/', ShopBasketDelete, name="ShopBasketDelete"),
    #ÜRÜNLER TAMAMI
    path('whey/', whey,name="whey"),
    path('kazein/',casein,name="casein"),
    path('soya/',soya,name="soya"),
    path('bcaa/',bcaa,name="bcaa"),
    path('creatin/',creatin,name="creatin"),
    path('carnitine/',carnitine,name="carnitine"),
    path('amino/',amino,name="amino"),
    path('kafein/',kafein,name="kafein"),
    path('vitamin/',vitamin,name="vitamin"),
    path('aksesuar/',aksesuar,name="aksesuar"),
    # PROGRAM
    path('yağyakım/',yagyakım,name="yagyakım"),
    path('hıtcardio/',hıt,name="hıt"),
    path('güç/',guc,name="guc"),
    path('ppl/',ppl,name="ppl"),
    path('full/',full,name="full"),
    path('ılerı/',ılerı,name="ılerı"),
    path('secım/',secım,name="secım"),
    path('gun/',gun,name="gun"),
    path('nasıl/',nasıl,name="nasıl"),
    path('makro/',makro,name="makro"),
    #USER
    path('login/', loginUser, name="loginUser"),
    path('register/', RegisterUser, name="RegisterUser"),
    path('logout/',logoutUser,name='logoutUser'),
    path('changepassword/',changePasswordUser,name="changePasswordUser"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
