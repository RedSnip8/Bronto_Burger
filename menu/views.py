from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Items, Diet_Restriction



def index(request):
    """
    The model for diet restricitions is set with unique_together for item_ID and diet_restriction.
    It will intially gather all occurences of the restrictions sent in the GET request which will
    be stored in a list. To avoid harmful code sent to the server, the loop will only check if the
    restr values list contains any of the know restriction types. IF statements will act as a builder
    for the intial select query. Once the subquery is built the query will then count the number of
    occurenecs of an item_id by counting the diet_strictions and will be grouped by the item_ids.
    Knowing that there cannot be duplicates of a row with a given item_id and diet_restriction
    combination, the count will imply that is how many of the given restrictions are met. So if the
    count for any listed item_ids is equal to the number of restrictions it would met all restrictions.
    """

    # set a variable to store the items object. This will be filtered later
    product_list = Items.objects.all()

    # first all restrictions are gathered and stored in a list

    # the list will then be passed to an if stament to check if there are any restrictions
        # if there is a restrictions list then the following code will test for known restricitons
        # and will build a list of restrictions for the subquery as well as a list to be passed back
        # to the render so that the chosen restriction will be active on the return page

        #after the subquery is built the restrictions list will pull a list of all ids that
        # match a total count equal to the number of queries


        # this list will then be used to filter only the listed IDs from the product_list passed in
        # the context

    context = {
        'products' : product_list,
        'values': request.GET,
    }

    return render(request, 'menu/menu.html', context)

def item(request, item_id):
    # takes the given request and will 404 if there is no valid ID passed in the GET request
    item = get_object_or_404(Items, pk=item_id)

    # the diet restrictions filters out only the occurences of the request ID for use in the return
    diet_types = Diet_Restriction.objects.filter(item_id=item_id)


    context = {
      'item' : item,
       'diet_type' : diet_types,
    }

    return render(request, 'menu/nutrition.html', context)
