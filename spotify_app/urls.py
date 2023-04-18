from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('main/', views.main_page, name='main_page' ),
    # path('search/<slug:slug>/', views.search, name='search'),
    # path('sorting/<slug:slug>', views.sorting, name='sorting'),
    # path('category/<slug:slug>/',views.category_detail, name='category_detail_url'),
    # path('register/', views.register, name= 'register'),
    # path('authorisation/', views.authorisation, name= 'authorisation'),
]
