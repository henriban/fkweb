from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.navbar, name='navbar'),
    url(r'^slideshow/', views.slideshow, name='slideshow'),
]
