from django.shortcuts import render
from django.http import HttpResponse

# Ensure this function exists with EXACTLY this name
def home(request):
    return HttpResponse("Hello, world. You're at the tasks homepage.")

def contact(request):
    return HttpResponse("<h1 style='color:red'>Contact us</h1>")

def show_tasks(request):
    return HttpResponse("Here are the tasks")

def show_specific_task(request,id):
    print('id:',id)
    print('type:',type(id))
    return HttpResponse(f"Here is a specific task {id}")