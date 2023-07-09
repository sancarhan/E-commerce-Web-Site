from django.shortcuts import render,get_object_or_404, redirect
from django.http import Http404
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def basketCount(request):
    if request.user.is_authenticated:
        return Shopbasket.objects.filter(user=request.user)
    else:
        return None
    
def index (request):
    products = ProductStok.objects.all()
    context = {"title":"Haftanın Önerilenleri"}
    query = request.GET.get("query")
    if query:
        products = products.filter(
            Q(product__title__icontains = query) |
            Q(product__brand__icontains = query) |
            Q(product__text__icontains=query) |
            Q(product__slug__icontains=query)
        )
        
    print(request.GET)
    context.update({
          "shopbasket": basketCount(request),
        "products":products,
          "products":products,
    })
    return render(request,'Anasayfa.html',context)
def ürünler (request):
    products = ProductStok.objects.all()
    context = {"title":" Ürünler"}
   
    context.update({
         
        "products":products,
          "products":products,
    })
    return render(request,'ürünler.html',context)

def iletişim (request):
    context = {
        "shopbasket": basketCount(request),
    }
    return render(request,'iletişim.html',context)

def ödeme (request):
   
    context = {
        "shopbasket": basketCount(request),
       
    }
    context = {"title":" Ödeme"}
    return render(request,'ödeme.html',context)

def sepet (request):
    sepet = Shopbasket.objects.filter(user=request.user)
    print(sepet)
    total = 0
    for i in sepet:
        total += i.price_all
        
    if request.method == "POST":
        for k, v in dict(request.POST).items():
            if k != "csrfmiddlewaretoken":
                try:
                    v[0] = int(v[0])
                except:
                    return redirect('sepet')
                
                shopb = sepet.get(id=k[5:])
                if v[0] == "0":
                    shopb.delete()
                elif v[0] > 0:
                    shopb.count = v[0]
                    shopb.price_all = shopb.product_letter.price * int(v[0])
                    shopb.save() 
                else:
                    return redirect('sepet')
                    
        return redirect('sepet')
                

    context = {
        "sepet": sepet,
        "total": total,
    }
    

    

  
    return render(request,'Sepet.html',context)

def productDetails (request,slug):
   
    context={}

    # PRODUCT 
    if ProductStok.objects.filter(product__slug = slug).exists():
        product = ProductStok.objects.get(product__slug = slug)
    elif ZAksesuar.objects.filter(slug = slug).exists():
            product = ZAksesuar.objects.get(slug = slug)
    elif ZVitamin.objects.filter(slug = slug).exists():
            product = ZVitamin.objects.get(slug = slug)
    elif ZWhey.objects.filter(slug = slug).exists():
            product = ZWhey.objects.get(slug = slug)
    elif ZSoya.objects.filter(slug = slug).exists():
            product = ZSoya.objects.get(slug = slug)
    elif ZCasein.objects.filter(slug = slug).exists():
            product = ZCasein.objects.get(slug = slug)
    elif ZBcaa.objects.filter(slug = slug).exists():
            product = ZBcaa.objects.get(slug = slug)
    elif ZCreatin.objects.filter(slug = slug).exists():
            product = ZCreatin.objects.get(slug = slug)
    elif ZLCarnitine.objects.filter(slug = slug).exists():
            product = ZLCarnitine.objects.get(slug = slug)
    elif ZAminoAsit.objects.filter(slug = slug).exists():
            product = ZAminoAsit.objects.get(slug = slug)
    elif ZKafein.objects.filter(slug = slug).exists():
            product = ZKafein.objects.get(slug = slug)
    # PRODUCT 
    
    if Product.objects.filter(slug=slug).exists():
        product = get_object_or_404(ProductStok, product__slug = slug)
         # SCTIPT 
        listprice = []
        listcolor = []
        listsize = []
        sizeprice = product.sizeletter.all()
        for i in range(len(sizeprice)):
            listprice.append(sizeprice[i].price)
            listcolor.append(sizeprice[i].color.styletitle)
            listsize.append(sizeprice[i].size.slug)
            context.update({
                "listprice": listprice,
                "listcolor": listcolor,
                "listsize": listsize,
            })
        # SCTIPT
    
   
    
    
    if request.method == "POST":
        
        submit = request.POST.get("submit")
        
        # SEPET SHOPBASKET =========
        if submit == "buy":
            color = request.POST.get("color")
            size = request.POST.get("size")
            try:
                count = int(request.POST.get("count"))
            except:
                return redirect('/Ürün/' + slug + '/')
            
            if count>0:
                prod = SizeLetter.objects.filter(product__slug=slug,color__styletitle=color, size__title=size)
                if prod.exists():
                    prod = prod.get()
                    price_all = prod.price * count
                    shopprod = Shopbasket.objects.filter(user=request.user,product_letter=prod)
                    if shopprod.exists(): # filterlanan ürün varsa true
                        shopprod = shopprod.get()
                        shopprod.count += count
                        shopprod.price_all += price_all
                        shopprod.save()
                    else:
                        shopb = Shopbasket(user = request.user, product_letter = prod,price_all=price_all, count=count )
                        shopb.save()     
            return redirect('/Ürün/'+ slug + '/')
       
        # SEPET SHOPBASKET =========
       
            
            
            
         
            
    
    context.update({
        "product":product,
        "shopbasket": basketCount(request),
        
    })
    return render(request,'product-details.html',context)


def ShopBasketDelete(request, sid):
    
    shopbasket = Shopbasket.objects.get(id=sid)
    shopbasket.delete()
    return redirect('sepet')



# ÜRÜNLER TAMAMI
def whey (request):
    
    wheys = ZWhey.objects.all()
    context = {"title":"Whey Proteinler"}
    context.update({
        
          "wheys":wheys,
    })
    return render(request,'sayfa/whey.html',context)

def casein (request):
    caseins = ZCasein.objects.all()
    context = {"title":"Kazein Proteinler"}
    context.update({
        
          "caseins":caseins,
    })
    return render(request,'sayfa/Casein.html',context)

def soya (request):
    soyas = ZSoya.objects.all()
    context = {"title":"Soya Proteinler"}
    context.update({
        
          "soyas":soyas,
    })
    return render(request,'sayfa/Soya.html',context)

def bcaa (request):
    bcaas = ZBcaa.objects.all()
    context = {"title":"BCAA"}
    context.update({
        
          "bcaas":bcaas,
    })
    return render(request,'sayfa/Bcaa.html',context)

def creatin (request):
    creatins = ZCreatin.objects.all()
    context = {"title":"CREATİN"}
    context.update({
        
          "creatins":creatins,
    })
    return render(request,'sayfa/Creatin.html',context)

def carnitine (request):
    carnites = ZLCarnitine.objects.all()
    context = {"title":"L-Carnitine"}
    context.update({
        
          "carnites":carnites,
    })
    return render(request,'sayfa/Carnitine.html',context)

def amino (request):
    aminos = ZAminoAsit.objects.all()
    context = {"title":"Amino Asitler"}
    context.update({
        
          "aminos":aminos,
    })
    return render(request,'sayfa/Amino.html',context)



def kafein (request):
    kafeins = ZKafein.objects.all()
    context = {"title":"Enerji ve Dayanıklılık"}
    context.update({
        
          "kafeins":kafeins,
    })
    return render(request,'sayfa/Kafein.html',context)



def vitamin (request):
    vitamins = ZVitamin.objects.all()
    context = {"title":"Vitaminler"}
    context.update({
        
          "vitamins":vitamins,
    })
    return render(request,'sayfa/Vitamin.html',context)




def aksesuar (request):
    aksesuars = ZAksesuar.objects.all()
    context = {"title":"Aksesuarlar"}
    context.update({
        
          "aksesuars":aksesuars,
    })
    return render(request,'sayfa/Aksesuar.html',context)

# PROGRAM
def yagyakım (request):
    yagyakıms = ZYagyakım.objects.all()
    
    paginator = Paginator(yagyakıms, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    yagyakıms = paginator.get_page(page_number)
    context = {"title":"Nasıl Yağ Yakabiliriz ?"}
    context.update({
        
          "yagyakıms":yagyakıms,
    })
    return render(request,'plan/yağyakım.html',context)

def hıt (request):
    hıts = ZHıt.objects.all()
    
    paginator = Paginator(hıts, 7)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    hıts = paginator.get_page(page_number)
    context = {"title":"Hıt Cardio Planı"}
    context.update({
        
          "hıts":hıts,
    })
    return render(request,'plan/hitcardio.html',context)

def guc (request):
    gucs = ZGuc.objects.all()
    
    paginator = Paginator(gucs, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    gucs = paginator.get_page(page_number)
    context = {"title":"Güç ve Kuvvet Antrenmanları"}
    context.update({
        
          "gucs":gucs,
    })
    return render(request,'plan/Güç.html',context)

def ppl (request):
    ppls = ZPpl.objects.all()
    
    paginator = Paginator(ppls, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    ppls = paginator.get_page(page_number)
    context = {"title":"PPL Programları"}
    context.update({
        
          "ppls":ppls,
    })
    return render(request,'plan/ppl.html',context)

def full (request):
    fulls = ZFull.objects.all()
    
    paginator = Paginator(fulls, 7)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    fulls = paginator.get_page(page_number)
    context = {"title":"Full-Body Programlar"}
    context.update({
        
          "fulls":fulls,
    })
    return render(request,'plan/full.html',context)

def ılerı (request):
    ılerıs = ZIlerı.objects.all()
    
    paginator = Paginator(ılerıs, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    ılerıs = paginator.get_page(page_number)
    context = {"title":"İleri Seviye 5x5 Programlar"}
    context.update({
        
          "ılerıs":ılerıs,
    })
    return render(request,'plan/ileriseviye.html',context)

def secım (request):
    secıms = ZSecım.objects.all()
    
    paginator = Paginator(secıms, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    secıms = paginator.get_page(page_number)
    context = {"title":"Ağırlık Seçimleri Neye Göre Olmalı ?"}
    context.update({
        
          "secıms":secıms,
    })
    return render(request,'plan/ağırlıkseçim.html',context)

def gun (request):
    guns = ZGun.objects.all()
    
    paginator = Paginator(guns, 8)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    guns = paginator.get_page(page_number)
    context = {"title":"Haftanın Kaç Günü Antrenman Yapılmalı ?"}
    context.update({
        
          "guns":guns,
    })
    return render(request,'plan/kaçgün.html',context)

def nasıl (request):
    nasıls = ZNasıl.objects.all()
    
    paginator = Paginator(nasıls, 4)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    nasıls = paginator.get_page(page_number)
    context = {"title":"Yağ Yakım Antrenmanları"}
    context.update({
        
          "nasıls":nasıls,
    })
    return render(request,'plan/nasılyağ.html',context)

def makro (request):
    makros = ZMakro.objects.all()
    
    paginator = Paginator(makros, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    makros = paginator.get_page(page_number)
    context = {"title":"Makrolar Nedir ?"}
    context.update({
        
          "makros":makros,
    })
    return render(request,'plan/makro.html',context)


