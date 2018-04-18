from django.conf.urls import url
from . import views

app_name = "portal"

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<users_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^Admin',views.Admin, name='admin'),
	url(r'^faculty',views.faculty, name='faculty'),
	url(r'^Student',views.Student, name='student'),
	url(r'^Course',views.Course, name='course'),
    url(r'^AddStudent',views.AddStudent, name='addstudent'),
	url(r'^AddFaculty',views.AddFaculty, name='addfaculty'),
	url(r'^attendance_sheet/(?P<subject>[A-Z0-9]+)/$',views.detail1, name='attendance_sheet'),
	url(r'^attendance_sheet/(?P<subject>[A-Z0-9]+)/(?P<student_id>[0-9]+)/$', views.a_p, name='attendance_update'),
]