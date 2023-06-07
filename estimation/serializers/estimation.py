from rest_framework.serializers import ModelSerializer, ValidationError
from estimation.models import Estimation


class EstimationShortSerializer(ModelSerializer):

    class Meta:
        model = Estimation
        fields = ("id", "estimation", "course", 'student')



class EstimationFullSerializer(ModelSerializer):

    class Meta:
        model = Estimation
        fields = "__all__"



class EstimationCreateSerializer(ModelSerializer):

    class Meta:
        model = Estimation
        fields = "__all__"

    def validate_estimation(self, value):
        if int(value) > 10 or int(value) < 1:
            raise ValidationError("Оценка должна быть от 1 до 10")
        
        return value

    def create(self, validated_data):
        return super().create(validated_data)



class EstimationDeleteSerializer(ModelSerializer):

    class Meta:
            model = Estimation
            fields = "__all__"

    def delete(self):
        return super().delete()