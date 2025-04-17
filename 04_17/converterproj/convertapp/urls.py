from django.urls import path
from . import views
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('converter')  # redirects to /converter

urlpatterns = [
    path('', home_redirect),  # <--- this line
    path('converter', views.converter, name='converter'),
    path('timer', views.timer, name='timer'),
]