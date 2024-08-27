from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseInstanceSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course')
    course = CourseSerializer(read_only=True)  # Nesting the CourseSerializer for the response

    class Meta:
        model = CourseInstance
        fields = ['id', 'course_id', 'course', 'year', 'semester']