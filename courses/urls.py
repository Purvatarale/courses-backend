from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.create_course, name='create_course'),
    path('courses/', views.list_courses, name='list_courses'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/delete/', views.delete_course, name='delete_course'),
    path('instances/', views.create_course_instance, name='create_course_instance'),
    path('instances/<int:year>/<int:semester>/', views.list_course_instances, name='list_course_instances'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', views.course_instance_detail, name='course_instance_detail'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/delete/', views.delete_course_instance, name='delete_course_instance'),
]
