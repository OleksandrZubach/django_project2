from django.urls import path
from . import views

urlpatterns = [
    path('hello/<name>',views.hello,name = 'name'),
    path('<number>', views.id, name = 'number'),
    path('og/<name>', views.req, name = 'req'),
    path('calc/<int:a>/<int:b>',views.calc, name = '')
]