from rest_framework import mixins, filters
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as df

from ..serializers import EstimationFullSerializer, EstimationCreateSerializer, EstimationShortSerializer, EstimationDeleteSerializer
from estimation.models import Estimation

class EstimationViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin):
    
    queryset = Estimation.objects.all()
    serializer_class = EstimationShortSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'patch', 'post', 'delete']
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, df.DjangoFilterBackend]
    search_fields = ['student__name', 'student__surname', 'course__title']
    ordering_fields = ['student__name',]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return EstimationCreateSerializer
        if self.action == 'destroy':
            return EstimationDeleteSerializer
        if self.action == 'list':
            return EstimationShortSerializer
        if self.action == 'retrieve':
            return EstimationFullSerializer
        return self.serializer_class
