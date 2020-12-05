from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def hello_world(request):
    msg = "<h1>Hello World</h1>";
    return HttpResponse(msg)

def index_page (request) :
    return HttpResponse("<h2>Welcome to my School Project</h2>")    

#Create views from html
def home_view(request):
    return render(request,"home.html")

def jquery_getRequest(request):
    return render(request,"jQget.html")    

class AboutUs(View):

     def get(self,request):
         return HttpResponse('<h3>Student can apply for BCA,B.Tech like courses !!!</h3>')