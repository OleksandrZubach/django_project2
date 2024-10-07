from django.shortcuts import render
from django.http import HttpResponse


def hello(request,name):
    cook = request.COOKIES
    if 'count_visit' in request.session:
        request.session['count_visit'] +=1
    else:
        request.session['count_visit'] = 1

    count_visit = request.session['count_visit']
    resp = HttpResponse(f"Hello {name} {cook} Visits: {count_visit}", )
    resp.set_cookie('LOL',"LOLOVICH")

    return resp


# def cokkie(request):
#     print(request.COOKIES)
#     resp = HttpResponse('C is for cookie and that is good enough for me...')
#     return resp


def id(request, number):
    return HttpResponse(f'Number {number}')


def req(request):
    name = request.GET['name']
    return HttpResponse(f'Name {name}')


def calc(request, a, b):
    return HttpResponse(f"A*B = {a*b}")

