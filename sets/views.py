from django.shortcuts import render
from sets.manager import Get_Sets
from sets.models import Set


def Index_View(request):
    if request.method == 'GET':
        try:
            setlist = Get_Sets()
            sets = Set.objects.all().order_by('release_date')
            print(len(sets))
        except FileNotFoundError:
            sets = Set.objects.all()
        context = {
            'sets': sets
        }
        return render(request, 'sets/index.html', context=context)
