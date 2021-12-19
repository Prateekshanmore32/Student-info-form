from typing import NamedTuple
from django.shortcuts import render,HttpResponse
from studentapp.models import Student
# Create your views here.
def home(request):
    return render(request,"index.htm")

def student_data(request):
    # print(request.POST)
    # print("Hello")
    print(request.POST.get('qualification'))
    try:
        if request.method == "POST":
            values ={
                "name" : request.POST.get('name'),
                "address":request.POST.get('address'),
                "mobileNo":int(request.POST.get('mobileNo')),
                "email":request.POST.get('email'),
                "age":int(request.POST.get('age')),
                "education":request.POST.get('education'),
                "qualification":request.POST.getlist('qualification'),
                "university":request.POST.getlist('university'),
                "insti":request.POST.getlist('insti'),
                "yop":request.POST.getlist('yop'),
                "percentage":request.POST.getlist('percentage'),
            }
            student_doc = request.file('document')
            
        instance = Student(name=values["names"], address = values["address"], mobileNo = values["mobileNo"], email =values["email"], age=values["age"], education=values["education"])
        instance.save()
        
    except:
        pass
    print(values["qualification"])
    return render(request,"student-info.htm",values)
