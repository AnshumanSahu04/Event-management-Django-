from django.shortcuts import render, HttpResponse

# Create your vie
def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("this is about page")

