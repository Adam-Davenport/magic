from django.shortcuts import render
from sets.manager import Get_Sets
from sets.models import Set


def Index_View(request):
    if request.method == 'GET':
        setlist = Get_Sets()
        sets = Set.objects.filter(code__in=setlist)
        context = {
            'sets': sets
        }
        return render(request, 'sets/index.html', content_type=context)
