from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet

router = routers.DefaultRouter()
router.register("student", StudentViewSet, "student")

urlpatterns = [
    path('', include(router.urls))
]
