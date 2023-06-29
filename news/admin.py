from django.contrib import admin

from news.models import Course, Teacher, Application

# Register your models here.

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Application)


