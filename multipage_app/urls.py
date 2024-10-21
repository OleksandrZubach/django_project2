from django.urls import path
from . import views

app_name = "multipage"
urlpatterns = [
    path('main/', views.main, name='main'),
    path('about/',views.about, name='about'),
    path('base/',views.base, name='base')
]