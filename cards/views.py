from django.shortcuts import render
from cards.packs import Booster
from cards.models import Card, Battle_Pack, Battle


def Index_View(request):
    return render(request, 'cards/index.html')


def Set_View(request):
    if request.method == 'GET':
        card_set = get_set('AVR')
        context = {
            'card_set': card_set
        }
        return render(request, 'cards/set.html', context=context)
    elif request.method == 'POST':
        card_set = request.POST.set
        return render(request, 'cards/set.html')


def Booster_View(request):
    sets = Card.objects.values('set_name').distinct()
    sets = [set['set_name'] for set in sets]
    if request.method == 'GET':
        context = {
            'sets': sets
        }
        return render(request, 'cards/boosterform.html', context=context)
    elif request.method == 'POST':
        current_set = request.POST['set']
        amount = int(request.POST['packtype'])
        boosters = Booster(current_set, amount)
        # Decide what page is presented to the user
        if 'battle' in request.POST:
            boosters.battle_pack()
            context = {
                'packs': boosters.battle_packs,
                'sets': sets,
            }
            return render(request, 'cards/battle.html', context=context)
        else:
            context = {
                'boosters': boosters.packs,
                'sets': sets,
            }
            return render(request, 'cards/booster.html', context=context)


def Individual_Packs(set_name, amount):
    boosters = []
    for p in range(amount):
        booster = Booster_Pack(set_name)
        boosters.append(booster.cards)
    return boosters


def Battle_List_View(request):
    if request.method == 'GET':
        battles = Battle.objects.all()
        context = {
            'battles': battles
        }
        return render(request, 'cards/battle_list.html', context=context)


def Battle_View(request, pk):
    if request.method == 'GET':
        battle = Battle.objects.get(pk=pk)
        packs = Battle_Pack.objects.filter(battle=battle)
        context = {
            'packs': packs,
        }
        return render(request, 'cards/battle.html', context=context)
