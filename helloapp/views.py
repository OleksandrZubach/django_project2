from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm


def hello(request,name):
    # cook = request.COOKIES
    # if 'count_visit' in request.session:
    #     request.session['count_visit'] +=1
    # else:
    #     request.session['count_visit'] = 1
    #
    # count_visit = request.session['count_visit']
    # resp = HttpResponse(f"Hello {name} {cook} Visits: {count_visit}", )
    # resp.set_cookie('LOL',"LOLOVICH")
    # # return resp
    cook = request.COOKIES
    if 'count_visit' in request.session:
        request.session['count_visit'] += 1
    else:
        request.session['count_visit'] = 1

    count_visit = request.session['count_visit']

    books = Book.objects.all()
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    ctxt = {'form': form, 'books': books, 'name': name, 'count_visit': count_visit}
    return render(request, "helloapp/hello.html", ctxt)

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

def book_list(request, name):
    # books = [Book.name,Book.year,Book.author)
    # books = Book.objects.all()
    # print(f"@@@@@ {books}")
    # # btxt = {'books': [{"name" : "aaa", "year": 2222, "author": "bbbb"}]}
    # btxt = {'books': books}
    # return render(request, 'helloapp/hello.html', btxt )
    cxtx = {'name': name,'author': "Oleksandr",'books': Book.objects.all()}
    return render(request, 'helloapp/hello.html',cxtx)
def hello2(request):
    name = request.GET['name']
    return HttpResponse(f"Hello, {name}")

def hello_templates(request):
    return HttpResponse('')