from rest_framework.serializers import ModelSerializer
from student.models import Student


class StudentShortSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = ("id", "name", "surname", 'email')



class StudentFullSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"



class StudentCreateSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)



class StudentDeleteSerializer(ModelSerializer):

    class Meta:
            model = Student
            fields = "__all__"

    def delete(self):
        return super().delete()