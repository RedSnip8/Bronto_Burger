from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Count
from .models import Items, Diet_Restriction, DIET_TYPES, FOOD_TYPES



def index(request):
    """
    The model for diet restricitions is set with unique_together for item_ID and diet_restriction.
    Code below will intially gather all occurences of the restrictions sent in the GET request which will
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

    # first all restrictions are gathered and stored in a list, but only if the match the keys of diet types
    restrictions_list = [x for x in request.GET.getlist('restr') if x in list([x for x, y in DIET_TYPES])]
    restriction_count = len(restrictions_list)
    subquery = []
    # the list will then be passed to an if stament to check if there are any restrictions
    if restrictions_list and restriction_count < 8:
        # this will decide how many ORs need to be in the database query. Once a number is found
        # the values will be passed to a queryset
        if restriction_count == 4:
           subquery = Diet_Restriction.objects.filter(
               diet_restriction__iexact=restrictions_list[0]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[1]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[2]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[3]
               )
        elif restriction_count < 4:
            if restriction_count == 2:
                subquery = Diet_Restriction.objects.filter(
               diet_restriction__iexact=restrictions_list[0]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[1]
                   )

            elif restriction_count > 2:
                subquery = Diet_Restriction.objects.filter(
               diet_restriction__iexact=restrictions_list[0]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[1]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[2]
               )

            else:
                subquery = Diet_Restriction.objects.filter(
               diet_restriction__iexact=restrictions_list[0]
               )

        else:
            if restriction_count == 6:
                 subquery = Diet_Restriction.objects.filter(
               diet_restriction__iexact=restrictions_list[0]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[1]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[2]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[3]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[4]
                ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[5]
                )

            elif restriction_count > 6:
                subquery = Diet_Restriction.objects.filter(
               diet_restriction__iexact=restrictions_list[0]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[1]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[2]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[3]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[4]
                ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[5]
                ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[6]
                )

            else:
                 subquery = Diet_Restriction.objects.filter(
               diet_restriction__iexact=restrictions_list[0]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[1]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[2]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[3]
               ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[4]
                ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[5]
                ) | Diet_Restriction.objects.filter(
                   diet_restriction__iexact=restrictions_list[6]
                )

        #after the subquery is built the restrictions list will pull a list of all ids that
        # match a total count equal to the number of queries
        restrictionQuery = Diet_Restriction.objects.filter(
            id__in=subquery).values(
                'item_id').annotate(
                    total=Count('diet_restriction')
                    )

        # this list will then be used to filter only the listed IDs from the product_list passed in
        # the context



    context = {
        'products' : product_list,

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
