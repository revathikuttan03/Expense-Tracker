from django.shortcuts import render,redirect

from etapp.models import Expense,Income

# Create your views here.

def home(request):
    ex= Expense.objects.all()
    income = Income.objects.all()
    total_ex = 0
    for i in ex:
        total_ex += i.amount
    total_income = 0
    for i in income:
        total_income += i.amount

    balance = total_income - total_ex

    expensesummery ={
        "totalexpense":total_ex,
        "totalincome":total_income,
        "balance":balance
    }

   
    return render(request,"home.html",{"d":ex,"income":income,"summery":expensesummery})
   
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