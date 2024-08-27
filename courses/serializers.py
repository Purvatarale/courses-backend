from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseInstanceSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)  # Nesting the CourseSerializer here

    class Meta:
        model = CourseInstance
        fields = '__all__'