# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewset, EmployeeViewset  # Corrected import

router = DefaultRouter()
router.register(r'companies', CompanyViewset)  # Correct class name
router.register(r'employees', EmployeeViewset)

urlpatterns = [
    path('', include(router.urls)),
]
