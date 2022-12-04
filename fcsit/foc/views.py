from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def teachers(request):
    return render(request,'teachers.html')
def contact(request):
    return render(request,'contact.html')