from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
	UserName = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	UserType = models.CharField(max_length=255)
	
	def __str__(self):
		return self.UserName + '-' + self.UserType
class Students(models.Model):
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	RollNo = models.CharField(max_length=50)
	PhoneNum = models.CharField(max_length=15)
	EmailAddress = models.CharField(max_length=255)
	Department = models.CharField(max_length=100)
	Sem = models.IntegerField()
def __str__(self):
		return self.FirstName
		
class Faculty(models.Model):	
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	PhoneNum = models.CharField(max_length=15)
	EmailAddress = models.CharField(max_length=255)
	Department = models.CharField(max_length=100)
def __str__(self):
		return self.FirstName

class Subject(models.Model):
	Name = models.CharField(max_length=255)
	Sem = models.IntegerField()
	FacultyId = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	Department = models.CharField(max_length=100)
def __str__(self):
		return self.Name

class Attendance(models.Model):
	SubjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
	StudentId = models.ForeignKey(Students, on_delete=models.CASCADE)
	Sem = models.IntegerField()
	Date = models.CharField(max_length=20)
	status = models.CharField(max_length=100)

class AttendanceReport(models.Model):
	SubjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
	StudentId = models.ForeignKey(Students, on_delete=models.CASCADE)
	Sem = models.IntegerField()
	percentage = models.FloatField(max_length=20)	
