from django.shortcuts import render
from sets.manager import Get_Sets
from sets.models import Set


def Index_View(request):
    if request.method == 'GET':
        try:
            setlist = Get_Sets()
            sets = Set.objects.filter(code__in=setlist)
        except FileNotFoundError:
            sets = Set.objects.all()
        context = {
            'sets': sets
        }
        return render(request, 'sets/index.html', content_type=context)
