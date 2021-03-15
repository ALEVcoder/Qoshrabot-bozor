from django.http import request
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail

def home(request):
    shoops = mahsulotlar.objects.all()
    shopp = yetishtirilayotgan_mahsulotlar.objects.all()
    
    status = {'mahsulot': shoops, 'yetish': shopp}
    return render(request, 'index.html', status)

# Create your views here.

def shop(request):
    if request.method == 'POST':
        ism = request.POST['user']
        familyasi = request.POST['familyasi']
        nomer = request.POST['nomer']
        mahsulots = request.POST['mahsulot']
        title=ism
        msg='Sizga '+ism+'dan Zakas bor'+'\nFamilyasi: '+ familyasi + ',\nMahsuloti: ``' + mahsulots + '``, \n' + '\nNomeri: ' + nomer

        print(ism, mahsulots, nomer)
        send_mail(
            ism,
            msg,
            nomer,
            ['testten475@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'checkout.html')

def blog(request):
    shopp = yetishtirilayotgan_mahsulotlar.objects.all()
    status = {'yetish': shopp}
    return render(request, 'blog-details.html', status)

def shop_details(request):
    return render(request, 'shop-details.html')

def shop_grid(request):
    return render(request, 'shop-grid.html')

def contact(request):
    if request.method == 'POST':
        ism = request.POST['user']
        xabar = request.POST['xabar']
        email = request.POST['pochta']
        title=ism
        msg='Sizga '+ism+'dan xabar bor'+'\nEmail: '+email+'\nXABAR Mazmuni:\n'+xabar

        print(ism, xabar, email)
        send_mail(
            ism,
            msg,
            email,
            ['testten475@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'contact.html')