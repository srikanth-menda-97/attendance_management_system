from django.contrib import admin
from .models import Users, Students, Faculty, Subject, Attendance, AttendanceReport
# Register your models here.
admin.site.register(Users)
admin.site.register(Students)
admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)