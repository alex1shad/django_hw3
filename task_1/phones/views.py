from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_choice = request.GET.get('sort', 'name')
    if sort_choice == 'min_price':
        sort_choice = 'price'
    elif sort_choice == 'max_price':
        sort_choice = '-price'
    phones = Phone.objects.order_by(sort_choice).all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'phone': phone[0]}
    return render(request, template, context)
