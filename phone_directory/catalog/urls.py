from django.urls import include, path
from rest_framework import routers

from .views import CompanyViewSet, ManagerViewSet, StafferViewSet

router = routers.DefaultRouter()

router.register(r'company', CompanyViewSet, basename='company')
router.register(r'manager', ManagerViewSet, basename='company')
router.register(r'staffer', StafferViewSet, basename='staffer')

urlpatterns = [
    path('', include(router.urls)),
]
