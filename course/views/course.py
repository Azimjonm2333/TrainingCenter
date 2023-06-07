from rest_framework import mixins, filters
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as df

from ..serializers import CourseFullSerializer, CourseCreateSerializer, CourseShortSerializer, CourseDeleteSerializer
from course.models import Course

class CourseViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin):
    
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseShortSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'patch', 'post', 'delete']
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, df.DjangoFilterBackend]
    search_fields = ['title', 'description']
    ordering_fields = ['title',]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return CourseCreateSerializer
        if self.action == 'destroy':
            return CourseDeleteSerializer
        if self.action == 'list':
            return CourseShortSerializer
        if self.action == 'retrieve':
            return CourseFullSerializer
        return self.serializer_class
