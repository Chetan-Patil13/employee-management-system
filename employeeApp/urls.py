from django.urls import path
from .views import index,view,add,remove,filter

urlpatterns=[
    path('index/',index),
    path('view/',view),
    path('add/',add),
    path('remove/<int:i>/',remove),
    path('remove/',remove),
    path('filter/',filter),
]
