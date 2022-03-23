from django.urls import path
from . import views


urlpatterns = [
    path('', views.polls_app_index, name='polls_index')
]