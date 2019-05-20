from django.http import HttpResponse,Http404
from django.template.loader import get_template
from datetime import datetime
import random
from mysite.models import Product

# Create your views here.

def index(request):
    template = get_template('index.html')
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def about(request):
    template = get_template('about.html')
    quotes =[
        '今日事，今日毕',
        '知识就是力量'
    ]
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)

def listing(request):
    template = get_template('listing.html')
    product = Product.objects.all()
    html = template.render(locals())
    return HttpResponse(html)

def disp_detail(request,sku):
    template = get_template('disp_detail.html')
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定产品')
    template = get_template('disp_detail.html')
    html = template.render({'product':p})

    return HttpResponse(html)

