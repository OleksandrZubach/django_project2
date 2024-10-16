from django.urls import path
from . import views

urlpatterns = [
    path('hello/<name>',views.hello,name = 'name'),
    path('<number>', views.id, name = 'number'),
    path('og/<name>', views.req, name = 'req'),
    path('calc/<int:a>/<int:b>',views.calc, name = ''),
    path('hello/', views.book_list, name='book_list'),
    path('localhost:8000/hello_t/<name>', views.hello_templates,name='')
]