from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('faleconosco', views.faleconosco, name='faleconosco'),
    path('anuncieaqui', views.anuncieaqui, name='anuncieaqui')



]
