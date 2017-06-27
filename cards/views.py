from django.shortcuts import render
from cards.packs import get_set, Booster_Box, Booster_Pack, Create_Battle_Pack
from cards.models import Card, Battle_Pack


# Create your views here.
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
    sets = Card.objects.values('set').distinct()
    sets = [set['set'] for set in sets]
    sets.sort()
    if request.method == 'GET':
        context = {
            'sets': sets
        }
        return render(request, 'cards/boosterform.html', context=context)
    elif request.method == 'POST':
        current_set = request.POST['set']
        # Decide how the booster is assembled
        if request.POST['packtype'] == 'single':
            boosters = Individual_Packs(current_set, 1)
        elif request.POST['packtype'] == 'draft':
            boosters = Individual_Packs(current_set, 3)
        elif request.POST['packtype'] == 'sealed':
            boosters = Individual_Packs(current_set, 6)
        else:
            boosters = Booster_Box(current_set).packs
        # Decide what page is presented to the user
        if request.POST['battle']:
            packs = []
            for b in boosters:
                packs.append(Create_Battle_Pack(b))

            context = {
                # 'boosters': boosters,
                'sets': sets,
            }
            return render(requets, 'cards/booster.html', context=context)
        else:
            context = {
                'boosters': boosters,
                'sets': sets,
            }
            return render(request, 'cards/booster.html', context=context)


def Individual_Packs(set_name, amount):
    boosters = []
    for p in range(amount):
        booster = Booster_Pack(set_name)
        boosters.append(booster.cards)
    return boosters
