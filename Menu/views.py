from django.shortcuts import render
from .models import *
import json
import pywhatkit

import datetime
# Create your views here.
shopperid = 0
def index(request):
    
    category = Category.objects.all()
    corbalar = Product.objects.filter(category__name = 'Çorbalar', is_active = True)
    kebaplar = Product.objects.filter(category__name = 'Kebaplar', is_active = True)
    pideler = Product.objects.filter(category__name = 'Pideler', is_active = True)
    tatlilar = Product.objects.filter(category__name = 'Tatlılar', is_active = True)
    icecekler = Product.objects.filter(category__name = 'İçecekler', is_active = True)
    if request.method == "POST":
        for product in products:
            id = request.POST.get('product{product.pk}')
            products = Product.objects.filter(id = id)

    context = {
        'active_link' : 'index',
        'category': category,
        'corbalar': corbalar,
        'kebaplar': kebaplar,
        'pideler': pideler,
        'tatlilar': tatlilar,
        'icecekler': icecekler,
    }
    return render(request, 'menu/index.html', context)

def corbalar(request):
    category = Category.objects.all()
    corbalar = Product.objects.filter(category__name = 'Çorbalar', is_active = True)
    
    context = {
        'active_link' : 'corba',
        'corbalar': corbalar,
        'category': category
    }
    return render(request, 'menu/corbalar.html', context)

def kebaplar(request):
    kebaplar = Product.objects.filter(category__name = 'Kebaplar', is_active = True)
    context = {
        'active_link' : 'kebap',
        'kebaplar': kebaplar
    }
    return render(request, 'menu/kebaplar.html', context)

def pideler(request):
    pideler = Product.objects.filter(category__name = 'Pideler', is_active = True)
    context = {
        'active_link' : 'pide',
        'pideler': pideler
    }
    return render(request, 'menu/pideler.html', context)

def tatlilar(request):
    tatlilar = Product.objects.filter(category__name = 'Tatlılar', is_active = True)
    context = {
        'active_link' : 'tatli',
        'tatlilar': tatlilar
    }
    return render(request, 'menu/tatlilar.html', context)

def icecekler(request):
    icecekler = Product.objects.filter(category__name = 'İçecekler', is_active = True)
    context = {
        'active_link' : 'icecek',
        'icecekler': icecekler
    }
    return render(request, 'menu/icecekler.html', context)

def sepet(request):
    category = Category.objects.all()
    products = Product.objects.all()
    corbalar = Product.objects.filter(category__name = 'Çorbalar')
    kebaplar = Product.objects.filter(category__name = 'Kebaplar')
    pideler = Product.objects.filter(category__name = 'Pideler')
    tatlilar = Product.objects.filter(category__name = 'Tatlılar')
    icecekler = Product.objects.filter(category__name = 'İçecekler')
    shopper = Shopper.objects.all()
    if request.method == 'POST':
        # set session variable
        
        
        city = request.POST.get('city')
        town = request.POST.get('town')
        suburb = request.POST.get('suburb')
        street = request.POST.get('street')
        homeno = request.POST.get('homeno')
        homename = request.POST.get('homename')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        productdetail = request.POST.get('productdetail')
        odemeturu = request.POST.get('odemeturu')
        request.session['session_id'] = phone
        # get session variable
        session_id = request.session.get('session_id', None)
        
        count = 0
        total = 0
        
        if odemeturu == 'nakit':
            nakit = True
        else:
            nakit = False
        shopper = Shopper(name = name, phone = phone, city = city, town = town, suburb = suburb, street = street, homeno = homeno, homename = homename, productdetail = productdetail, odemeturu = nakit)
        shopper.save()
        
        tarih = datetime.datetime.now()
        for product in products:
            proid = None
            proid = request.POST.get('proid{}'.format(product.pk))
            productses = Product.objects.filter(id = proid)
            dairehesap = Daire.objects.filter(month = tarih.month)
            for daire in dairehesap:
                kebaplar = daire.kebaplar
                pideler = daire.pideler
                diger = daire.diger
            if(proid != None):
                for pro in productses:
                    
                    total = total + pro.price
                    shopper.productlist.add(pro.id)
                    shopper.total = total
                    shopper.save()
                    print(str(pro.category))
                    if dairehesap == None:
                        if str(pro.category) == "Kebaplar":
                            kebaplar = kebaplar + 1
                            dairehesap = Daire(kebaplar = kebaplar)
                            
                        elif str(pro.category) == "Pideler":
                            pideler = pideler + 1
                            dairehesap = Daire(pideler = pideler)
                        else:
                            diger = diger + 1
                            dairehesap = Daire(diger = diger)
                    else:
                        if str(pro.category) == "Kebaplar":
                            kebaplar = kebaplar + 1
                            dairehesap.update(kebaplar = kebaplar)
                            
                        elif str(pro.category) == "Pideler":
                            pideler = pideler + 1
                            dairehesap.update(pideler = pideler)
                        else:
                            diger = diger + 1
                            dairehesap.update(diger = diger)
    context = {
        'active_link' : 'sepet',
        'category': category,
        'corbalar': corbalar,
        'kebaplar': kebaplar,
        'tatlilar': tatlilar,
        'icecekler': icecekler,
    }
    return render(request, 'menu/sepet.html', context)

def order(request):
    
    context = {
        
        
    }
    return render(request, 'menu/orderdetail.html', context)