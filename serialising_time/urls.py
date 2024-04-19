  
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet
router = DefaultRouter()
urlpatterns = [
    path('', PersonViewSet.as_view(actions = {'get','list', 'post', 'create'})),
    path('<int:pk>', PersonViewSet.as_view(actions = {'get': 'retrieve',
                                             'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))
]

