from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Items, Egg_Free, Gluten_Free, Lactose_Free, Nut_Free, Soy_Free, Vegan, Vegetarian

DIET_RESTRICTIONS = {
    Egg_Free:'Egg-Free', Gluten_Free: 'Gluten-Free', Lactose_Free: 'Lactose-Free',
    Nut_Free: 'Nut-Free', Soy_Free: 'Soy-Free', Vegetarian:'Vegetarian', Vegan:'Vegan'
    }


def index(request):
    products = Items.objects.order_by('')

    context = {
        'products' : products,
    }

    return render(request, 'menu/menu.html', context)

def item(request, item_id):
    item = get_object_or_404(Items, pk=item_id)

    diet_types = []

    for x,y in DIET_RESTRICTIONS.items():
        if x.objects.filter(item=item_id):
            diet_types.append(y)

    context = {
      'item' : item,
       'diet_type' : diet_types,
    }

    return render(request, 'menu/nutrition.html', context)
