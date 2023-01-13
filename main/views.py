from django.shortcuts import render

def home(request):
    return render(request,'main/home.html')
def Senate(request):
    return render(request,'main/Senate.html')
def minutes(request):
    return render(request,'main/minutes.html')
