from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('rating/', views.rating, name="rating"),
    path('contacts/', views.contacts, name="contacts"),
    path('cabinet/', views.cabinet, name="cabinet"),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('film1/', views.film1, name="film1"),
    path('film2/', views.film2, name="film2"),
    path('film3/', views.film3, name="film3"),
    path('film4/', views.film4, name="film4"),


]