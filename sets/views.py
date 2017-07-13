from django.shortcuts import render, get_object_or_404
from sets.manager import Get_Sets
from sets.models import Set
from cards.models import Card


def Index_View(request):
    if request.method == 'GET':
        sets = Set.objects.all()
        for set in sets:
            print(set.pk)
        context = {
            'sets': sets
        }
        return render(request, 'sets/index.html', context=context)


def Details_View(request, pk):
    if request.method == 'GET':
        current_set = get_object_or_404(Set, pk=pk)
        cards = Card.objects.filter(set_name=pk)
        mythics = []
        rares = []
        uncommons = []
        commons = []
        for card in cards:
            if card.rarity == 'Mythic Rare':
                mythics.append(card)
            elif card.rarity == 'Rare':
                rares.append(card)
            elif card.rarity == 'Uncommon':
                uncommons.append(card)
            elif card.rarity == 'Common':
                commons.append(card)
        cards = {
            'mythics': mythics,
            'rares': rares,
            'uncommons': uncommons,
            'commons': commons
        }
        context = {
            'set': current_set,
            'cards': cards
        }
        return render(request, 'sets/details.html', context=context)
