from django.shortcuts import render,redirect

from etapp.models import Expense,Income

# Create your views here.

def home(request):
    ex= Expense.objects.all()
    income = Income.objects.all()
   
    return render(request,"home.html",{"d":ex,"income":income})
   
def expense(request):
    
    if request.GET.get("amount"):
        amount = request.GET.get("amount")
        description = request.GET.get("description")
        data = Expense()
        data.amount = amount
        data.description = description
        data.save()
        return redirect ("/")
    return render(request,"expense.html")
    

def income(request,):
    if request.GET.get("amount"):
        amount = request.GET.get("amount")
        description = request.GET.get("description")
        task = Income()
        task.amount = amount
        task.description = description
        task.save()
        return redirect("/")
    return render(request,"income.html")