from django.shortcuts import render
from .models import Order, Product
from django.shortcuts import render
from django.shortcuts import render, redirect



from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm

def store_home(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {'products': products})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .forms import OrderForm

def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('order_success')  # تأكد أن اسم المسار مطابق في urls.py
    else:
        form = OrderForm()

    return render(request, 'store/place_order.html', {'product': product, 'form': form})


# store/views.py

def store_view(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)
    if category:
        products = products.filter(category__icontains=category)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    context = {
        'products': products,
        'query': query,
        'category': category,
        'min_price': min_price,
        'max_price': max_price,
    }

    return render(request, 'store/store.html', context)


# Create your views here.
def order_success(request):
    return render(request, 'store/order_success.html')
