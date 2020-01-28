from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Items, Diet_Restriction



def index(request):
    product_list = Items.objects.all()

    # Check if restr is in the request
    if 'restr' in request.GET:

    # find all the filter option in the request store in a list
        restriction_list = request.GET.getlist('restr')
    # Find all the item_id's using the Diet_restrictions table for the
    # restrictions in gathered from the request


    # Filter out the products_list using the filter list



    context = {
        'products' : product_list,
        'values': request.GET,
    }

    return render(request, 'menu/menu.html', context)

def item(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    diet_types = Diet_Restriction.objects.filter(item_id=item_id)


    context = {
      'item' : item,
       'diet_type' : diet_types,
    }

    return render(request, 'menu/nutrition.html', context)
