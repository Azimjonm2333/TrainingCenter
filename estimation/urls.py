from django.urls import path, include
from rest_framework import routers
from .views import EstimationViewSet

router = routers.DefaultRouter()
router.register("estimation", EstimationViewSet, "estimation")

urlpatterns = [
    path('', include(router.urls))
]
