from django.shortcuts import render
from cards.packs import get_set


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
