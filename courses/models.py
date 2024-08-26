from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.title

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instances')
    year = models.IntegerField()
    semester = models.IntegerField()
    instance_id = models.IntegerField()  # Changed from `course_id` to `instance_id`

    def __str__(self):
        return f"{self.course.title} - {self.year} Sem {self.semester}"
