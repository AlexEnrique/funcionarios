from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import EmployeeViewSet

router = SimpleRouter()
router.register("", EmployeeViewSet, basename='employees')

urlpatterns = router.urls
