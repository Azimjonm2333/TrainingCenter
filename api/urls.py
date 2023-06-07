from django.urls import path, include
from rest_framework import routers
from estimation.views import EstimationViewSet
from course.views import CourseViewSet
from student.views import StudentViewSet

router = routers.DefaultRouter()
router.register("estimation", EstimationViewSet, "estimation")
router.register("course", CourseViewSet, "course")
router.register("student", StudentViewSet, "student")

urlpatterns = [
    path('', include(router.urls)),
]

