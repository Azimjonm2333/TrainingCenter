from rest_framework.serializers import ModelSerializer
from course.models import Course


class CourseShortSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "title", "description", 'duration')



class CourseFullSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"



class CourseCreateSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)



class CourseDeleteSerializer(ModelSerializer):

    class Meta:
            model = Course
            fields = "__all__"

    def delete(self):
        return super().delete()