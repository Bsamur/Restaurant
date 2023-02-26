from decimal import Decimal
from django.shortcuts import render, redirect
from Menu.models import *
from .forms import ImageForm
from cloudinary.forms import cl_init_js_callbacks
import pywhatkit
import datetime
# Create your views here.

def login_kasaadmin(request):
    
    return render(request, 'kasaadmin/login.html')
def whatsapp(request):
    
    if request.method == 'POST':
        userid = request.POST.get('userid')
        shopped = Shopper.objects.filter(finished = False, id = userid)
        shopped.update(finished = True, teslim = True)
        shopping = Shopper.objects.get(finished = True, id = userid)
        pywhatkit.sendwhatmsg(shopping.phone, "Merhaban Sn. {}. {} numaralı siparişiniz kuryeye teslim edilmiştir. Size iletilmek üzere yola çıkmıştır. Bizi tercih ettiğiniz için teşekkür ederiz. Afiyet olsun. USTALAR PİDE".format(shopping.name, shopping.pk), datetime.datetime.now().hour, (datetime.datetime.now().minute + 1))          
                  
    
    else:
        shopping = Shopper.objects.filter(finished = False)
        
            
    return redirect('dashboard')
def dashboard(request):
    
    shopper = Shopper.objects.filter(finished = False)
    cari = Cari.objects.all()
    tarih = datetime.datetime.now()
    shopping = Shopper.objects.filter(finished = True, date_now = tarih)
    x = 0
    for shop in shopping:
        x = x + shop.total
        
        
    cari = Cari.objects.filter(date_now = tarih)
    if cari.exists():
        cari.update(ciro = x)
    else:
        cari = Cari(ciro = x)
        cari.save()
    
    bekleyenshopp = Shopper.objects.filter(finished = False, date_now = tarih)
    bitenshopp = Shopper.objects.filter(finished = True, date_now = tarih)
    a = 0
    b = 0
    for shopp in bekleyenshopp:
        a = a + 1
        
    for shopp1 in bitenshopp:
        b = b + 1
    
    monthcari = Cari.objects.filter(month = tarih.month)
    c = 0
    for month in monthcari:
        c = c + month.ciro
    
    dairehesap = Daire.objects.filter(month = tarih.month)
    kebap = 0
    pide = 0
    diger = 0
    for daire in dairehesap:
        kebap = daire.kebaplar
        pide = daire.pideler
        diger = daire.diger
    
    tutargrafik = Cari.objects.filter(month = 1)
    ocak = 0
    for grafik in tutargrafik:
        ocak = ocak + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 2)
    subat = 0
    for grafik in tutargrafik:
        subat = subat + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 3)
    mart = 0
    for grafik in tutargrafik:
        mart = mart + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 4)
    nisan = 0
    for grafik in tutargrafik:
        nisan = nisan + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 5)
    mayis = 0
    for grafik in tutargrafik:
        mayis = mayis + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 6)
    haziran = 0
    for grafik in tutargrafik:
        haziran = haziran + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 7)
    temmuz = 0
    for grafik in tutargrafik:
        temmuz = temmuz + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 8)
    agustos = 0
    for grafik in tutargrafik:
        agustos = agustos + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 9)
    eylul = 0
    for grafik in tutargrafik:
        eylul = eylul + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 10)
    ekim = 0
    for grafik in tutargrafik:
        ekim = ekim + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 11)
    kasim = 0
    for grafik in tutargrafik:
        kasim = kasim + grafik.ciro
    tutargrafik = Cari.objects.filter(month = 12)
    aralik = 0
    for grafik in tutargrafik:
        aralik = aralik + grafik.ciro
    context = {
        'active_link': 'dashboard',
        'shopper': shopper,
        'cari': cari,
        'a' : a,
        'b' : b,
        'c': c,
        'kebap': kebap,
        'pide': pide,
        'diger': diger,
        'ocak': ocak,
        'subat': subat,
        'mart': mart,
        'nisan' : nisan,
        'mayis' : mayis,
        'haziran' : haziran,
        'temmuz' : temmuz,
        'agustos' : agustos,
        'eylul' : eylul,
        'ekim' : ekim,
        'kasim' : kasim,
        'aralik' : aralik,
        
    }
    return render(request, 'kasaadmin/index.html', context)



def productadd(request):
    form= ImageForm()   
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance
            form.save()
    context = {
        'active_link': 'productadd',
        'form' : form
    }
    return render(request, 'kasaadmin/productadd.html', context)

def productlistview(request):
    product = Product.objects.all()
    categories = Category.objects.all()
    
    context = {
        'active_link': 'productlist',
        'product' : product,
        'categories' : categories,
    }
    return render(request, 'kasaadmin/productlist.html', context)


def updateproduct(request, slug):
    product = Product.objects.get(slug = slug)
    if request.method == 'POST':
        category = request.POST.get('categoryname')
        if category == "kebaplar" or category == "pideler":
            productaci1 = True
        else:
            productaci1 = False
    
        if category == "corbalar":
            product.category_id = 1
        elif category == "kebaplar":
            product.category_id = 2
        elif category == "pideler":
            product.category_id = 3
        elif category == "tatlilar":
            product.category_id = 4
        elif category == "icecekler":
            product.category_id = 5
        product.name = request.POST.get('name')
        product.desc = request.POST.get('desc')
        product.price = request.POST.get('price')
        if request.POST.get('satis') == "satis":
            product.is_active = True
        else:
            product.is_active = False
        
        if request.POST.get('kampanya') == 'kampanya':
            product.offer = True
        else:
            product.offer = False
        product.productaci = productaci1
        product.save()
        return redirect('productlist')    
    context = {
        'htmloffer' : "Var",
        'checked' : 'checked',
        'active_link': 'updateproduct',
        'product' : product,
    }
    return render(request, 'kasaadmin/updateproduct.html', context)