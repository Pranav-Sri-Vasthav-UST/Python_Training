from django.urls import path
from . import views

urlpatterns = [
    path('', views.salary_form, name='salary_form'),  # salary form
    path('result/', views.salary_result, name='salary_result'),# result page
    path('jumble/', views.jumble_word, name='jumble_word'),# word jumble
]
