from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    content = "Hello Everyone !!!!. This is StudentApp !!.<br><br>";
    content = content + "<a href='all_student/'>All Student</a><br><br>"
    content = content + "<a href='add_student/'>Add Student</a> <br>"
    return HttpResponse(content)

def all_student(request):
    latest_student_list = Student.objects.all()
    context = { 'latest_student_list' :latest_student_list } 
    return render(request,'StudentApp/latest_student_list.html',context)   

def detail(request, student_id):
    student = get_object_or_404(Student,pk=student_id)
    context = {'student':student}
    return render(request,'StudentApp/student_details.html',context) 

def add_student(request):
    return render(request,'StudentApp/add_student.html')

from django.utils import timezone

def add(request):
    name = request.POST['name']
    rollno = request.POST['rollno']
    course = request.POST['course']
    fee =  request.POST['fee']
    
    student = Student(name=name, rollno=rollno, course=course, fee=fee, pub_date=timezone.now())
    
    message = ""

    try:
        student.save()
        message = "Student data submitted !!!"
    except:
        message = "Can't save student details.Please try again !!"
    context = {'message':message}
    return render(request,'StudentApp/add_student.html',context)        

def delete_student(request, student_id):
    student = get_object_or_404(Student,pk=student_id)
    message = ""
    try:
        student.delete()
        message = "Student Record Deleted Successfully !!!" 
    except:
        message = "Can't delete student details. Please try again"
        message = message + "<br><br><a href='../../all_student/'>Back</a>";           
    return HttpResponse(message)    

#django-rest-framework
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
         data = JSONParser().parse(request)
         serializer = StudentSerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data,status=201)
         return JsonResponse(serializer.errors,status=400)          

@csrf_exempt
def student_detail(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer=StudentSerializer(student) 
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
         data = JSONParser().parse(request)
         serializer = StudentSerializer(student,data=data)
         if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data,status=201)
         return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
         student.delete()
         return HttpResponse("Record Deleted Successfully!!!")      
