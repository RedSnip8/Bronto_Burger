from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Items, Diet_Restriction



def index(request):
    product_list = Items.objects.all()

    # Filter if restrition set by least common to most common
    if 'restr' in request.GET:
        restritions = set(request.GET.getlist('restr'))
        # Egg-free Filter
        if 'eggF' in restritions:
            product_list.filter(diet_restriction__diet_restriction='eggf')

        # Soy-free filter
        if 'soyF' in restritions:
            product_list.filter(diet_restriction__diet_restriction='soyF')
        # Nut-Free Filter
        if 'nutF' in restritions:
            product_list.filter(diet_restriction__diet_restriction='nutF')
        # Gluten-Free Filter
        if 'glutF' in restritions:
            product_list.filter(diet_restriction__diet_restriction='glutF')
        # Lactose-Free Filter
        if 'lactF' in restritions:
            product_list.filter(diet_restriction__diet_restriction='Lactose-Free')
        # Vegan filter
        if 'vegan' in restritions:
            product_list.filter(diet_restriction__diet_restriction='vegan')
        # Vegetarian filter
        if 'vegtrn' in restritions:
            product_list.filter(diet_restriction__diet_restriction='vegtrn')

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
