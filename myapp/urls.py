from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
#<<<<<<<<<<<<<<<<<<<<<<<<<< Admin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
path('',views.index,name='index'),
path('login/',views.logins,name='login'),
path('logout/',views.logoutt,name='logout'),
path('list/',views.listt,name='list'),
path('delete/<int:pk>',views.deletes,name='delete_hr'),
path('edit/<int:pk>',views.edit,name='update_hr'),
path('signup/',views.signupp,name='signup'),
#<<<<<<<<<<<<<<<<<<<<<<<<<<< HR >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
path('index/',views.indexx,name='index_hr'),
path('index/',views.indexx,name='index_hr'),
path('jobcreate/',views.job_create,name='job-create'),
path('listjobcreate/',views.list_job,name='list-job'),
path('jobedit/<int:pk>',views.job_edit,name='job-edit'),
path('jobdelete/<int:pk>',views.job_delete,name='job-delete'),
path('viewcandidate/<int:pk>',views.candidate_view,name='list-candidate'),
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Candidate >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
path('jobnotification/',views.job_notification,name='job-notifications'),
path('candidateprofile/<int:pk>',views.candidate_profile,name='candidate-profile'),















]