from typing import NamedTuple
from django.shortcuts import render,HttpResponse
from studentapp.models import Student
# Create your views here.
def home(request):
    return render(request,"index.htm")

def student_data(request):
    try:
        if request.method == "POST":
            mylist = zip(request.POST.getlist('qualification'),request.POST.getlist('university'),request.POST.getlist('insti'),request.POST.getlist('yop'),request.POST.getlist('percentage'))

            values ={
                "name" : request.POST.get('name'),
                "address":request.POST.get('address'),
                "mobileNo":int(request.POST.get('mobileNo')),
                "email":request.POST.get('email'),
                "age":int(request.POST.get('age')),
                "education":request.POST.get('education'),
                "mylist":mylist,
            }
            student_doc = request.file('document')
            
        instance = Student(name=values["names"], address = values["address"], mobileNo = values["mobileNo"], email =values["email"], age=values["age"], education=values["education"])
        instance.save()
        
    except:
        pass
    return render(request,"student-info.htm",values)
