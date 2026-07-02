from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def expense(request):
    return render(request,"expense.html")
    

def income(request):
    return render(request,"income.html")