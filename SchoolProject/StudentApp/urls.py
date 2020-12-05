from django.urls import path
from StudentApp.views import index
from . import views

urlpatterns = [
    path('',views.index),
    path('all_student/',views.all_student),
    path('<int:student_id>/',views.detail,name='detail'),
    path('add_student/',views.add_student),
    path('add/', views.add),
    path('<int:student_id>/delete_student/',views.delete_student,name='delete_student'),
    #django-rest-framework
    path('student_api/students/',views.student_list),
    path('student_api/students/<int:pk>/',views.student_detail),
]