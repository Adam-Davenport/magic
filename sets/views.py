from django.shortcuts import render
from sets.manager import Get_Sets


def Index_View(request):
    if request.method == 'GET':
        sets = Get_Sets()
        context = {
            'sets': sets
        }
        return render(request, 'sets/index.html', content_type=context)
