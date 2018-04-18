from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .models import Users, Students, Faculty, Attendance,Subject,AttendanceReport

#def index(request):
#	all_users = Users.objects.all()
#	html = ''
#	for user in all_users:
#		url = '/portal/' + str(user.id) + '/'
#		html += '<a href="' + url + '">' + str(user.id) +'</a><br>'
#	return HttpResponse(html)
def detail1(request, subject):
	attendance_sheet = Students.objects.all()
	#for member in attendance_sheet:
	#	Attendance.objects.create(SubjectId=Subject.objects.get(Name=subject),StudentId=Students.objects.get(id=member.id),Sem="6",Date="02-04-2018",status="absent")
	#subject = Subject.objects.get(Name = subject_name)
	context ={'attendance_sheet': attendance_sheet,
			  'subject' : subject}
	return render(request, 'pages/attendance_sheet.html', context)

def AddStudent(request):
	print request.POST.get('firstname','')
	Students.objects.create(FirstName=request.POST.get('firstname',''),LastName=request.POST.get('lastname',''),RollNo=request.POST.get('rollno',''),PhoneNum=request.POST.get('phonenum',''),EmailAddress=request.POST.get('email',''),Department=request.POST.get('department',''),Sem=request.POST.get('sem',''))	
	return redirect('portal:admin')

def AddFaculty(request):
	print request.POST.get('firstname','')
	Faculty.objects.create(FirstName=request.POST.get('firstname',''),LastName=request.POST.get('lastname',''),PhoneNum=request.POST.get('phonenum',''),EmailAddress=request.POST.get('email',''),Department=request.POST.get('department',''))	
	return redirect('portal:admin')
				
def detail(request, users_id):
	return HttpResponse("<h2>Details for users:"+str(users_id)+"</h2>")

def index(request):
  return render(request,'index.html', {})
   
def Admin(request):
  return render(request,'pages/Admin.html',{})
  
def faculty(request):
  return render(request,'pages/faculty.html',{})
  
def Student(request):
  return render(request,'pages/Student.html',{})  
  
def Course(request):
  return render(request,'pages/course.html',{})  
  
def a_p(request,student_id,subject):
	at = Attendance.objects.filter(SubjectId=Subject.objects.get(Name=subject),StudentId=Students.objects.get(id=student_id),Sem="6",Date="02-04-2018")
	at[0].status = "Present" ;
	context ={'subject' : subject}
	return render(request, 'pages/attendance_sheet.html', context)
	