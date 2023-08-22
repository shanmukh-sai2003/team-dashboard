from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name = "login"),
    path('', index, name = "home"),
    path('add/', add, name = "add"),
    path('update/<int:id>/', updateOperation, name = 'update'),
    path('delete/<int:id>/', deleteOperation, name = "delete"),
    path('logout/', logout_view, name = "logout")
]