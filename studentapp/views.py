from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.htm")

def student_data(request):
    try:
        if request.method == "POST":
            values ={
                "name" : request.POST.get('name'),
                "address":request.POST.get('address'),
                "mobileNo":int(request.POST.get('mobileNo')),
                "email":request.POST.get('email'),
                "age":int(request.POST.get('age')),
                "education":request.POST.get('education')

            }
    except:
        pass
    return render(request,"student-info.htm",values)
    # return HttpResponse(request)