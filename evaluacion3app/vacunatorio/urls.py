from django.urls import path
from vacunatorio import views

urlpatterns =[
    path('index/',views.index),
    path('list/' ,views.list),
    path('listaction/',views.listaction),
    path('search/',views.search),
    path('searchresult/',views.searchresult),
    path('add/',views.add),
    path('addaction/',views.addaction),
]