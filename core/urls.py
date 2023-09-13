from django.urls import path
from . import views
urlpatterns = [
    path('api', views.persons, name='person-list'),
    path('api/<int:id>', views.person_detail, name='person-detail')
]
