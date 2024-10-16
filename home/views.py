from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    content = '<h1> Home <h1>'  '<ul> <li>  <a href = "/hello/vic">Hello</a> </li>    </ul>' \
            '<ul> <li>  <a href = "/calc/10/10">Calc</a> </li>    </ul>' \
            '<ul><li><a href = /game/> Game </a></li></ul>'\
            '<ul><li><a href = /base/>Base</a></li></ul>'
    return HttpResponse(content)
