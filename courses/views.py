from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

@swagger_auto_schema(
    method='post',
    request_body=CourseSerializer,
    responses={
        201: openapi.Response('Course Created', CourseSerializer),
        400: 'Bad Request'
    },
    operation_description="Create a new course",
)
@api_view(['POST'])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('List of Courses', CourseSerializer(many=True))
    },
    operation_description="List all available courses",
)
@api_view(['GET'])
def list_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)



@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter(
            'pk', openapi.IN_PATH, description="Course ID", type=openapi.TYPE_INTEGER
        )
    ],
    responses={
        200: openapi.Response('Course Details', CourseSerializer),
        404: 'Not Found'
    },
    operation_description="Get details of a specific course by ID",
)
@api_view(['GET'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourseSerializer(course)
    return Response(serializer.data)



@swagger_auto_schema(
    method='delete',
    manual_parameters=[
        openapi.Parameter(
            'pk', openapi.IN_PATH, description="Course ID", type=openapi.TYPE_INTEGER
        )
    ],
    responses={
        204: 'No Content',
        404: 'Not Found'
    },
    operation_description="Delete a specific course by ID",
)
@api_view(['DELETE'])
def delete_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@swagger_auto_schema(
    method='post',
    request_body=CourseInstanceSerializer,
    responses={
        201: openapi.Response('Course Instance Created', CourseInstanceSerializer),
        400: 'Bad Request'
    },
    operation_description="Create a new course instance",
)
@api_view(['POST'])
def create_course_instance(request):
    serializer = CourseInstanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('year', openapi.IN_PATH, description="Year of the course instance (YYYY)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('semester', openapi.IN_PATH, description="Semester of the course instance (1 or 2)", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: openapi.Response('List of Course Instances', CourseInstanceSerializer(many=True)),
        404: 'Not Found'
    },
    operation_description="List all course instances for a specific year and semester",
)
@api_view(['GET'])
def list_course_instances(request, year, semester):
    instances = CourseInstance.objects.filter(year=year, semester=semester)
    serializer = CourseInstanceSerializer(instances, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('year', openapi.IN_PATH, description="Year of the course instance (YYYY)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('semester', openapi.IN_PATH, description="Semester of the course instance (1 or 2)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('course_id', openapi.IN_PATH, description="Course ID", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: openapi.Response('Course Instance Details', CourseInstanceSerializer),
        404: 'Not Found'
    },
    operation_description="Get details of a specific course instance by year, semester, and course ID",
)
@api_view(['GET'])
def course_instance_detail(request, year, semester, instance_id):
    try:
        instance = CourseInstance.objects.get(year=year, semester=semester, instance_id=instance_id)
    except CourseInstance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourseInstanceSerializer(instance)
    return Response(serializer.data)



@swagger_auto_schema(
    method='delete',
    manual_parameters=[
        openapi.Parameter('year', openapi.IN_PATH, description="Year of the course instance (YYYY)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('semester', openapi.IN_PATH, description="Semester of the course instance (1 or 2)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('course_id', openapi.IN_PATH, description="Course ID", type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: 'No Content',
        404: 'Not Found'
    },
    operation_description="Delete a specific course instance by year, semester, and course ID",
)
@api_view(['DELETE'])
def delete_course_instance(request, year, semester, instance_id):
    try:
        instance = CourseInstance.objects.get(year=year, semester=semester, instance_id=instance_id)
    except CourseInstance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)