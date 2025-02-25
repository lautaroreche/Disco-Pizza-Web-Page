from django.shortcuts import render
from disco_pizza_web_page_app.models import Product


def home(request):
    products = Product.objects.all()
    half = len(products) // 2
    context = {
        "products": products,
        'column_1': products[:half],
        'column_2': products[half:]
    }
    return render(request, 'index.html', context)
