from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug("Redirecting to catalog")
    return redirect('catalog')


def show_catalog(request):
    logger.debug("Showing catalog")
    sort_option = request.GET.get('sort', 'name')
    if sort_option == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_option == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all().order_by('name')

    return render(request, 'catalog.html', {'phones': phones})


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'product.html', {'phone': phone})
