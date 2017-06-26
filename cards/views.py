from django.shortcuts import render
from cards.packs import get_set, Booster_Box
from cards.models import Card


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
        return render(request, 'cards/boosterform.html', context=context)
    elif request.method == 'POST':
        current_set = request.POST['set']
        boosters = Booster_Box(current_set)
        context = {
            'boosters': boosters.packs,
            'sets': sets,
        }
        return render(request, 'cards/booster.html', context=context)
