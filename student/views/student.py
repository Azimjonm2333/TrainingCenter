from rest_framework import mixins, filters
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as df

from ..serializers import StudentFullSerializer, StudentCreateSerializer, StudentShortSerializer, StudentDeleteSerializer
from student.models import Student

class StudentViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin):
    
    queryset = Student.objects.filter(is_active=True)
    serializer_class = StudentShortSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'patch', 'post', 'delete']
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, df.DjangoFilterBackend]
    search_fields = ['name', 'surname', 'email']
    ordering_fields = ['name',]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return StudentCreateSerializer
        if self.action == 'destroy':
            return StudentDeleteSerializer
        if self.action == 'list':
            return StudentShortSerializer
        if self.action == 'retrieve':
            return StudentFullSerializer
        return self.serializer_class
