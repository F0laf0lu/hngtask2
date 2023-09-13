from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . views import PersonViewSet

router = DefaultRouter()
router.register('api', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api/', views.persons, name='person-list'),
    # path('<int:id>', views.person_detail, name='person-detail')
]
