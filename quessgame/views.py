from django.shortcuts import render
from django.http import HttpResponse
#
def guessform(request):

    return render(request, 'quessgame/index.html')

