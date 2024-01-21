from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def demo(request):
    # name = "India"
    # return render(request, "home.html", {'obj': name})
    # return HttpResponse("Hello World") #httpview
    return render(request,"index.html")  # render


def addition(request):
    number1 = int(request.GET['num1'])
    number2 = int(request.GET['num2'])
    res = number1 + number2
    return render(request, "result.html", {'result': res})  # render

# def about(request):
#     return render(request,"about.html")  # render
#
# def contact(request):
#     return HttpResponse("Hello Contact Page")
