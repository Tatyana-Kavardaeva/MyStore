from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def base(request):
    return render(request, 'main/base.html')


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main/products_list.html', context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'main/products_detail.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'main/contact.html')
